from datetime import datetime

import math
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from bank.models import Bank
from villa.models import Villa, Unit
from .impose_fee_on_unit import ImposeFeeOnUnit
from .unit_bill import UnitBill
from .unit_fee import UnitFee
from .fee_type import FeeType
from .impose_type import ImposeType


class VillaFee(models.Model):

    villa = models.ForeignKey(
        Villa, null=False, on_delete=models.CASCADE, related_name='villa_fees')

    fee_type = models.ForeignKey(FeeType, null=False, on_delete=models.PROTECT, related_name='villa_fee')
    fee = models.FloatField(blank=True, default=0)

    date_created = models.DateTimeField(auto_now_add=True)

    imposing_unit_count = models.IntegerField(default=0, blank=True)
    imposing_person_count = models.IntegerField(default=0, blank=True)
    impose_type = models.ForeignKey(ImposeType, on_delete=models.PROTECT, blank=True, null=True)
    fixed = models.BooleanField(blank=True, default=False)
    individual = models.BooleanField(blank=True, default=False)

    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, null=True, blank=True)
    account_number = models.CharField(max_length=20, null=True, blank=True)

    def save(
            self, *args, **kwargs
    ):
        if not self.pk:
            now = datetime.now()
            self.impose_type = ImposeType.objects.get(name='세대별부과')
            super(VillaFee, self).save(*args, **kwargs)
            units = Unit.objects.filter(villa=self.villa, does_exist=True)
            for unit in units:
                # VillaFee 부과 유닛 수 증가
                self.imposing_unit_count += 1
                if unit.person_count is not None:
                    # VillaFee 부과 인원 수 증가
                    self.imposing_person_count += unit.person_count

                # 2. ImposeFeeOnUnit 생성
                ImposeFeeOnUnit.objects.create(villa=self.villa, villa_fee=self, building=unit.building,
                                               unit=unit,
                                               do_impose=True)

                # 3-2. UnitFee 생성
                unit_bill = UnitBill.objects.get(unit=unit, date_created__year=now.year, date_created__month=now.month)
                unit_bill.total_fee += math.ceil(self.fee / len(units))
                unit_bill.save()
                UnitFee.objects.create(fee_type=self.fee_type, building=unit.building, unit=unit,
                                                  fee=math.ceil(self.fee / len(units)),
                                                  unit_bill=unit_bill)
        from ..methods import update_fee_when_villa_fee_changes
        update_fee_when_villa_fee_changes(villa_fee=self)
        return super(VillaFee, self).save(force_update=True)

    def delete(self, *args, **kwargs):
        villa_fee = self
        if villa_fee.individual:
            for unit_fee in villa_fee.unit_fees.all():
                unit_bill = unit_fee.unit_bill
                unit_bill.total_fee -= unit_fee.fee
                unit_bill.save()
                unit_fee.delete()
            return super(VillaFee, self).delete()

        villa = villa_fee.villa
        ImposeFeeOnUnit.objects.filter(villa=villa, villa_fee=villa_fee).delete()

        now = datetime.now()

        for building in villa.buildings.all():
            for unit in building.units.filter(does_exist=True):
                try:
                    unit_fee = UnitFee.objects.get(fee_type=villa_fee.fee_type, building=building, date_created__month=now.month,
                                                   date_created__year=now.year, unit=unit)
                except ObjectDoesNotExist:
                    continue
                unit_bill = unit_fee.unit_bill
                unit_bill.total_fee -= unit_fee.fee
                unit_bill.save()
                unit_fee.delete()

        return super(VillaFee, self).delete()
    def __str__(self):
        return '{}.  {} - {}'.format(self.id,  self.villa.name,
                                           self.fee_type.name)
