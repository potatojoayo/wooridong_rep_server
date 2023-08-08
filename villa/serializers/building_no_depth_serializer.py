from rest_framework import serializers
from ..models import Building

class BuildingNoDepthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = '__all__'



        
