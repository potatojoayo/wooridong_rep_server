from django.db import models
from villa.models import Building, Unit
from . import SentUnitBill, UnitFee
from .fee_type import FeeType


class SentUnitFee(models.Model):
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, related_name='sent_unit_fees')
    fee_type = models.ForeignKey(FeeType, on_delete=models.CASCADE)
    fee = models.FloatField(null=False)
    date = models.DateField(auto_now_add=True)
    sent_villa_fee = models.ForeignKey('fee.SentVillaFee', null=True, blank=True, on_delete=models.CASCADE,
                                       related_name='sent_unit_fees')
    pay_date = models.DateField(null=True, blank=True)
    sent_unit_bill = models.ForeignKey(
        SentUnitBill,
        null=True,
        blank=True,
        related_name='sent_unit_fees', on_delete=models.CASCADE
    )
    unit_fee = models.OneToOneField(UnitFee, on_delete=models.PROTECT, related_name='sent_unit_fee')

    def __str__(self):
        return '{}. {}년{}월 {}동 {} - {}'.format(self.id, self.date.year, self.date.month, self.building.building_number,
                                               self.unit.unit_number, self.fee_type.name)
