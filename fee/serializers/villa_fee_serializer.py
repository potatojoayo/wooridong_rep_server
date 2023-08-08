from rest_framework import serializers
from ..models import VillaFee 
from .fee_type_serializer import FeeTypeSerializer 
from .impose_type_serializer import ImposeTypeSerializer
from .unit_fee_with_unit_serializer import UnitFeeWithUnitSerializer 

class VillaFeeSerializer(serializers.ModelSerializer):

    fee_type = FeeTypeSerializer(read_only=True)
    impose_type = ImposeTypeSerializer(read_only=True)
    unit_fees = UnitFeeWithUnitSerializer(read_only=True,many=True)

    class Meta:

        fields='__all__'
        model = VillaFee 

