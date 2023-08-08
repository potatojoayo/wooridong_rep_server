from rest_framework import serializers

from villa.serializers.unit_serializer import UnitSerializer
from ..models import UnitBill


class UnitBillWithUnitSerializer(serializers.ModelSerializer):

    unit = UnitSerializer(read_only=True)

    class Meta:
        model = UnitBill
        fields = '__all__'
