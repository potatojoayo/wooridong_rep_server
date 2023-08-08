from rest_framework import serializers

from fee.models import VillaFee
from fee.serializers import FeeTypeSerializer


class VillaFeeDepthOneSerializer(serializers.ModelSerializer):
    fee_type = FeeTypeSerializer(read_only=True)

    class Meta:
        model = VillaFee
        fields = '__all__'
