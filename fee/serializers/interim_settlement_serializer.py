from rest_framework import serializers
from ..models import InterimSettlement

class InterimSettlementSerializer(serializers.ModelSerializer):

    class Meta:

        model = InterimSettlement 
        fields = '__all__'
        extra_kwargs = {'unit_bill': {'read_only': True},
                        'fees': {'read_only': True},
                        'total_fee': {'read_only': True},
                        'sent_date': {'read_only': True},
                        'paid_date': {'read_only': True},
                        'weight': {'read_only': True},
                        'phone': {'read_only': True},
                        }

