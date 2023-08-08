from django.db import models

from bank.models import Bank
from villa.models import Villa
from . import VillaFee
from .fee_type import FeeType
from .impose_type import ImposeType


class SentVillaFee(models.Model):
    villa = models.ForeignKey(
        Villa, null=False, on_delete=models.CASCADE, related_name='sent_villa_fees')
    fee_type = models.ForeignKey(FeeType, null=False, on_delete=models.PROTECT, related_name='sent_villa_fee')
    fee = models.FloatField(blank=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=False)
    pay_date = models.DateField(null=True, blank=True)

    imposing_unit_count = models.IntegerField(default=0, blank=True)
    imposing_person_count = models.IntegerField(default=0, blank=True)
    impose_type = models.ForeignKey(ImposeType, on_delete=models.PROTECT, blank=True, null=True)

    individual = models.BooleanField(blank=True, default=False)

    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, null=True, blank=True)
    account_number = models.CharField(max_length=20, null=True, blank=True)

    villa_fee = models.OneToOneField(VillaFee, on_delete=models.PROTECT, related_name='sent_villa_fee')

    def __str__(self):
        return '{}. {}년{}월 {} - {}'.format(self.id, self.due_date.year, self.due_date.month, self.villa.name,
                                           self.fee_type.name)
