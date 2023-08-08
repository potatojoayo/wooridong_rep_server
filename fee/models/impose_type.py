from django.db import models


class ImposeType(models.Model):

    name = models.CharField(max_length=20, null=False) 
    description = models.CharField(max_length = 50, null= False)

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)
