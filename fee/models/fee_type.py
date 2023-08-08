from django.db import models


class FeeType(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)
