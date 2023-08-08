from rest_framework import serializers

from .unit_fee_no_depth_serializer import UnitFeeNoDepthSerializer
from ..models import UnitBill


class UnitBillDepthOneSerializer(serializers.ModelSerializer):
    unit_fees = serializers.SerializerMethodField()

    class Meta:
        model = UnitBill
        fields = '__all__'

    def get_unit_fees(self, instance):
        unit_fees = instance.unit_fees.all().order_by('pk')
        return UnitFeeNoDepthSerializer(unit_fees, many=True, read_only=True).data
