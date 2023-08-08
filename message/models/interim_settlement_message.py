from django.db import models
from user.models import User
from villa.models import Unit, Villa, Building

class InterimSettlementMessage(models.Model):

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE) 
    sent_date = models.DateField(auto_now_add=True)
    message = models.TextField()
    villa = models.ForeignKey(
        Villa, on_delete=models.SET_NULL, null=True)
    building = models.ForeignKey(
        Building, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(
        Unit, on_delete=models.SET_NULL, null= True)
    target_date = models.DateField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)



