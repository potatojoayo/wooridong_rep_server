from django.db import models
from villa.models import Building, Unit
from .unit_bill import UnitBill
from .fee_type import FeeType


class UnitFee(models.Model):
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, related_name='unit_fees')
    fee_type = models.ForeignKey(FeeType, on_delete=models.CASCADE)
    fee = models.FloatField(null=False)
    date_created = models.DateField(auto_now_add=True)
    villa_fee = models.ForeignKey('fee.VillaFee', null=True, blank=True, on_delete=models.CASCADE,
                                  related_name='unit_fees')
    unit_bill = models.ForeignKey(
        UnitBill,
        null=True,
        blank=True,
        related_name='unit_fees', on_delete=models.CASCADE
    )
    is_individual = models.BooleanField(default=False)

    def __str__(self):
        return '{}. {}년{}월 {}동 {} - {}'.format(self.id, self.date_created.year, self.date_created.month, self.building.building_number,
                                               self.unit.unit_number, self.fee_type.name)
