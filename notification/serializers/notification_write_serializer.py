from rest_framework import serializers

from ..models import Notification
from villa.serializers import UnitSerializer

class NotificationWriteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Notification
        fields = '__all__'
        extra_kwargs = {'user':{'read_only':True}}



