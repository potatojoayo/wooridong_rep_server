from rest_framework import serializers
from ..models import UnitFee
from .fee_type_serializer import FeeTypeSerializer
from .unit_bill_serializer import UnitBillSerializer

class UnitFeeCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model =  UnitFee
        fields = '__all__'
