from rest_framework import serializers
from ..models import ImposeType
from villa.models import Villa

class ImposeTypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = ImposeType 
        fields = '__all__'

