from django.db import models
from villa.models import Villa, Building, Unit
from user.models import User


class BillMessage(models.Model):
    class TargetType(models.IntegerChoices):
        ALL = 0
        BUILDING = 1
        UNIT = 2

    target_type = models.IntegerField(choices=TargetType.choices, null=False)
    sent_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)
    villa = models.ForeignKey(
        Villa, on_delete=models.SET_NULL, null=True)
    building = models.ForeignKey(
        Building, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(
        Unit, on_delete=models.SET_NULL, null=True)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
