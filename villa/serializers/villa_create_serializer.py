from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from ..models import Villa
from .address_serializer import AddressSerializer


class VillaCreateSerializer(WritableNestedModelSerializer):

    address = AddressSerializer()

    class Meta:
        model = Villa
        fields = '__all__'
        extra_kwargs = {'rep': {'read_only': True}}

