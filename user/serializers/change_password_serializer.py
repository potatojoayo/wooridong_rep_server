from rest_framework import serializers
from ..models import User

class ChangePasswordSerializer(serializers.Serializer):

    model = User 
    new_password = serializers.CharField(required=True)
