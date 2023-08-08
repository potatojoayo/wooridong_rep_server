from django.db import models

from .villa import Villa
from .building import Building
from user.models import User


class Unit(models.Model):
    villa = models.ForeignKey(Villa, null=False, on_delete=models.CASCADE, related_name='units')
    building = models.ForeignKey(
        Building, null=False, on_delete=models.CASCADE, related_name='units')
    unit_number = models.CharField(max_length=10, null=False)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    person_count = models.IntegerField(null=True, default=0, blank=True)
    floor = models.IntegerField(null=False, default=99)
    line = models.IntegerField(null=False, default=99)
    rep = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    does_exist = models.BooleanField(null=False, default=True)

    class Meta:
        unique_together = ['villa', 'building', 'unit_number']

    def __str__(self):
        return '{}. {} {}동 {}'.format(self.id, self.villa.name, self.building.building_number, self.unit_number)
