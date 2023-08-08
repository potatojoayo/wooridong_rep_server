from rest_framework import serializers

from ..models import UnitBill


class UnitBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitBill
        fields = '__all__'
