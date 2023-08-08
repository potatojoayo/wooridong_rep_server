from rest_framework import serializers

from . import VillaSerializer
from ..models import Villa
from ..models.rep_take_over import RepTakeOver


class RepTakeOverSerializer(serializers.ModelSerializer):
    # villa_list = RepTakeOver()

    class Meta:
        model = Villa
        fields = '__all__'