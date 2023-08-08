from rest_framework import serializers
from ..models import AnnouncementMessage 

class AnnouncementMessageSerializer(serializers.ModelSerializer):

    class Meta:

        model = AnnouncementMessage 
        fields = '__all__' 
        extra_kwargs = {'rep':{'read_only': True,},}
