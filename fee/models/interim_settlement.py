from django.db import models
from villa.models import Unit, Villa, Building
from fee.models import UnitBill

class InterimSettlement(models.Model):

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE) 
    unit_bill = models.ForeignKey(UnitBill, on_delete=models.CASCADE, related_name='interim_settlements',blank=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    fees = models.JSONField(blank=True)
    total_fee = models.IntegerField(blank=True)
    target_date = models.DateTimeField()
    sent_date = models.DateTimeField(auto_now_add=True,blank=True)
    paid_date = models.DateTimeField(null=True, blank=True)
    weight = models.FloatField(default=1.05, blank=True)
    cancel_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{}. {} {} / {} - {}'.format(self.id,self.unit.villa.name,self.unit.unit_number,self.total_fee,self.sent_date)
