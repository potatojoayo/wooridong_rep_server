from rest_framework import serializers
from ..models import Unit


class WebUnitDetailSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Unit
        fields = '__all__'
        depth=2


