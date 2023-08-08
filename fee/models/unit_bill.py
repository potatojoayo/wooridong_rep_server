from django.db import models
from villa.models.unit import Unit
from villa.models.villa import Villa


class UnitBill(models.Model):
    date_created = models.DateField(auto_now_add=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='unit_bills')
    total_fee = models.IntegerField(default=0)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='unit_bills')
    person_count = models.IntegerField(default=0, null=True)
    phone_number = models.CharField(max_length=12, default='')

    def __str__(self):
        return '{}. {}년{}월 {} - {}'.format(self.id, self.date_created.year, self.date_created.month, self.unit.__str__(),
                                           self.total_fee)
