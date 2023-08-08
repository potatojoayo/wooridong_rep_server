from rest_framework import serializers
from ..models import Villa
from .building_serializer import BuildingSerializer
from .address_serializer import AddressSerializer


class VillaSerializer(serializers.ModelSerializer):

    buildings = BuildingSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Villa
        fields = '__all__'
        depth = 2
