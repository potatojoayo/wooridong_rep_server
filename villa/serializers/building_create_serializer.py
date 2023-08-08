from rest_framework import serializers
from ..models import Building

class BuildingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = '__all__'



        
