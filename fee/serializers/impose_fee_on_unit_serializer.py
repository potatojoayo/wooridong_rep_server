from rest_framework import serializers
from ..models import ImposeFeeOnUnit
from villa.serializers.unit_serializer import UnitSerializer

class ImposeFeeOnUnitSerializer(serializers.ModelSerializer):

    unit = UnitSerializer(read_only=True)
    
    class Meta:

        model = ImposeFeeOnUnit
        fields = '__all__'


