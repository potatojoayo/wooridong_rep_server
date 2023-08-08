from django.db import models

from fee.models import UnitBill
from villa.models.unit import Unit
from villa.models.villa import Villa


class SentUnitBill(models.Model):
    date = models.DateField()
    paid_date = models.DateTimeField(null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='sent_unit_bills')
    total_fee = models.IntegerField(default=0)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='sent_unit_bills')
    person_count = models.IntegerField(default=0, null=True)
    phone_number = models.CharField(max_length=12, default='')
    unit_bill = models.OneToOneField(UnitBill, on_delete=models.PROTECT, related_name='sent_unit_bill')

    def __str__(self):
        return '{}. {}년{}월 {} - {}'.format(self.id, self.date.year, self.date.month, self.unit.__str__(),
                                           self.total_fee)
