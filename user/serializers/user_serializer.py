from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('identification', 'name', 'phone_number', 'id', 'fcm_token', 'chat_name')
        lookup_field = 'identification'
