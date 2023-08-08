from rest_framework import serializers

from .unit_with_bill_serializer import UnitWithBillSerializer
from ..models import Building


class BuildingSerializer(serializers.ModelSerializer):
    units = serializers.SerializerMethodField()

    class Meta:
        model = Building
        fields = '__all__'
        depth = 1

    def get_units(self, instance):
        units = instance.units.filter(floor__gte=0).order_by('floor', 'line')
        request = self.context.get('request')
        if request is not None:
            return UnitWithBillSerializer(units, many=True, read_only=True,
                                          context={'request': self.context.get('request')}).data
        return UnitWithBillSerializer(units, many=True, read_only=True).data
