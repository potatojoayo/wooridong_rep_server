from django.db import models

from user.models import User
from villa.models import Unit


class Notification(models.Model):
    class TargetType(models.IntegerChoices):
        ALL = 0
        BUILDING = 1
        UNIT = 2
        REP = 3
        PUSH = 4

    class NotificationType(models.IntegerChoices):
        PAY_VILLA_FEE = 0
        UNIT_BILL_PAID = 1
        SEND_BILL = 2
        BEFORE_PAY_VILLA_FEE = 3
        VILLA_FEE_REGISTER_SUCCESS = 4
        VILLA_FEE_REGISTER_FAILED = 5

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_type = models.IntegerField(choices=TargetType.choices)
    target_unit = models.ForeignKey(Unit, null=True, blank=True, on_delete=models.CASCADE)
    notification_type = models.IntegerField(choices=NotificationType.choices)
    message = models.TextField()
    contents = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    read_datetime = models.DateTimeField(null=True, blank=True)
