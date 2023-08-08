from rest_framework import serializers
from ..models import InterimSettlementMessage


class InterimSettlementMessageSerializer(serializers.ModelSerializer):

    class Meta:

        model = InterimSettlementMessage
        fields = '__all__'
        extra_kwargs = {'message': {'read_only': True},
                        'sender': {'read_only': True},
                        'villa': {'read_only': True},
                        'building': {'read_only': True},
                        }
