from rest_framework import serializers

from ..models import Notification
from villa.serializers import UnitSerializer


class NotificationSerializer(serializers.ModelSerializer):

    target_unit = UnitSerializer(read_only=True)

    class Meta:

        model = Notification
        fields = '__all__'
        extra_kwargs = {'user':{'read_only':True}}



