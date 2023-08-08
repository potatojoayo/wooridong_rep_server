from django.db import models

from user.models import User
from bank.models import Bank
from .address import Address


class Villa(models.Model):
    name = models.CharField(max_length=20, null=False)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    rep = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='villa', null=True, blank=True)
    bank_account = models.CharField(max_length=50, null=True, blank=True)
    bank = models.ForeignKey(Bank, null=True, on_delete=models.CASCADE, blank=True)
    account_owner = models.CharField(null=True, default='account_owner_not_set', max_length=50, blank=True)
    building_count = models.IntegerField(default=1, null=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)
