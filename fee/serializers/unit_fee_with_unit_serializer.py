from rest_framework import serializers
from ..models import UnitFee
from .fee_type_serializer import FeeTypeSerializer
from .unit_bill_serializer import UnitBillSerializer
from villa.serializers.unit_serializer import UnitSerializer

class UnitFeeWithUnitSerializer(serializers.ModelSerializer):

    fee_type = FeeTypeSerializer(read_only=True)
    unit_bill = UnitBillSerializer(read_only=True)
    unit = UnitSerializer(read_only=True)

    class Meta:

        model =  UnitFee
        fields = '__all__'
