from rest_framework import serializers
from ..models import Unit, Building


class UnitSerializer(serializers.ModelSerializer):

    building_name = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_building_name(self,obj):
        building = Building.objects.get(pk=obj.building_id)
        return building.building_name
