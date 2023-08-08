from rest_framework import serializers
from ..models import Villa


class VillaNoDepthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Villa
        fields = '__all__'


