from rest_framework import serializers
from ..models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True)

    class Meta:
        model = User
        fields = ('name', 'password', 'identification', 'phone_number', 'id')

    def create(self, validated_data):
        user = User.objects.create_user(
            identification=validated_data['identification'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
