from django.db import models
from villa.models import Villa, Building, Unit


class ImposeFeeOnUnit(models.Model):
    villa = models.ForeignKey(
        Villa, on_delete=models.CASCADE)
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE)
    villa_fee = models.ForeignKey('fee.VillaFee', on_delete=models.CASCADE, related_name='imposing_units')
    do_impose = models.BooleanField(null=False, default=True)

    class Meta:

        unique_together = ['villa', 'building', 'unit', 'villa_fee']

    def __str__(self):
        return '{}. {} {}동 {} '.format(self.id, self.villa.name, self.building.building_number, self.unit.unit_number,
                                         )
