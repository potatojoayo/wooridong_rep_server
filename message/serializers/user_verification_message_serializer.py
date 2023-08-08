from rest_framework import serializers
from ..models import UserVerificationMessage 

class UserVerificationMessageSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserVerificationMessage 
        fields = '__all__' 
        extra_kwargs = {'code': {'read_only': True}, 'expiration_time': {'read_only': True}}
