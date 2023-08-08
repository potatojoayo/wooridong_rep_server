from django.db import models
from user.models import User
from villa.models import Unit

class RepVerificationMessage(models.Model):

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE) 
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sent_date = models.DateField(auto_now_add=True)

