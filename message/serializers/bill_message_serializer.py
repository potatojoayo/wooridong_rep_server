from rest_framework import serializers
from ..models import BillMessage


class BillMessageSerializer(serializers.ModelSerializer):

    class Meta:

        model = BillMessage
        fields = '__all__'
        extra_kwargs = {'message': {'read_only': True},
                        'sender': {'read_only': True},
                        'villa': {'read_only': True},
                        'building': {'read_only': True},
                        }
