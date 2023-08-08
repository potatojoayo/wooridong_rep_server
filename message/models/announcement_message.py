from django.db import models
from user.models import User
from villa.models import Unit

class AnnouncementMessage(models.Model):

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE) 
    rep = models.ForeignKey(User, on_delete=models.CASCADE) 
    sent_date = models.DateField(auto_now_add=True)
    message = models.TextField()


