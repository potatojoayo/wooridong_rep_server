from rest_framework import serializers
from ..models import VillaFee 
from .fee_type_serializer import FeeTypeSerializer 
from .impose_type_serializer import ImposeTypeSerializer

class VillaFeeCreateSerializer(serializers.ModelSerializer):

    class Meta:

        fields='__all__'
        model = VillaFee 

