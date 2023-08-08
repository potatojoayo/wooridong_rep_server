from django.db import models

from user.models import User
from villa.models import Villa


class RepTakeOver(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, null=False)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='villa_list')
    is_takeover = models.BooleanField(default=False)