from rest_framework import serializers
from ..models import UnitFee
from .fee_type_serializer import FeeTypeSerializer

class UnitFeeNoDepthSerializer(serializers.ModelSerializer): 

    fee_type = FeeTypeSerializer(read_only=True)

    class Meta:

        model =  UnitFee
        fields = '__all__'
