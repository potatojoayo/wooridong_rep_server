from rest_framework import serializers
from ..models import UnitFee
from .fee_type_serializer import FeeTypeSerializer
from .unit_bill_serializer import UnitBillSerializer

class UnitFeeSerializer(serializers.ModelSerializer):

    fee_type = FeeTypeSerializer(read_only=True)
    unit_bill = UnitBillSerializer(read_only=True)

    class Meta:

        model =  UnitFee
        fields = '__all__'
