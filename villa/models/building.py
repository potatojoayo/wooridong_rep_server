from django.db import models
from .villa import Villa


class Building(models.Model):

    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='buildings')
    building_number = models.IntegerField(null=False, default=0)
    building_name = models.CharField(null=True, max_length=10, blank=True)
    has_elevator = models.BooleanField(default=False)
    floors = models.IntegerField(null = False, default= 5)
    lines = models.IntegerField(null= False, default = 2) 

    class Meta:

        unique_together = ['villa','building_number']

    def __str__(self):
        return '{} {} / id={}'.format(self.villa.name, self.building_name,self.id)
    

