from rest_framework import serializers
from ..models import FeeType
from villa.models import Villa

class FeeTypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = FeeType 
        fields = '__all__'

