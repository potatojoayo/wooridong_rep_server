from rest_framework import serializers
from ..models import ImposeFeeOnUnit
from villa.serializers.unit_serializer import UnitSerializer

class ImposeFeeOnUnitCreateSerializer(serializers.ModelSerializer): 
    
    class Meta:

        model = ImposeFeeOnUnit
        fields = '__all__'


