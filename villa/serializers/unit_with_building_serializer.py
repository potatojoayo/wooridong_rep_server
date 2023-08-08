from rest_framework import serializers

from .building_no_depth_serializer import BuildingNoDepthSerializer
from ..models import Unit


class UnitWithBuildingSerializer(serializers.ModelSerializer):
    building = BuildingNoDepthSerializer(read_only=True)

    class Meta:
        model = Unit
        fields = '__all__'
