from django.db import models


# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=3, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)
