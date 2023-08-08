from django.db import models
from user.models import User
from villa.models import Unit

class UserVerificationMessage(models.Model):

    code = models.CharField(max_length=6, blank=True)
    expiration_time = models.DateTimeField(blank=True)
    phone_number = models.CharField(max_length=11)



