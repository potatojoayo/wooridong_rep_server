from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models import InterimSettlementMessage 
from fee.models import UnitBill,VillaFee, InterimSettlement
from ..serializers import InterimSettlementMessageSerializer
from villa.models import Unit
from src.lib import message as send_message
from ..filters import InterimSettlementMessageFilter
import json

from datetime import datetime


class InterimSettlementCancleMessageViewSet(viewsets.ModelViewSet):

    serializer_class = InterimSettlementMessageSerializer
    filterset_class = InterimSettlementMessageFilter

    def get_queryset(self): 
        return InterimSettlementMessage.objects.filter(rep=self.request.user)

    def perform_create(self, serializer):
        unit = serializer.validated_data.get('unit')
        target_date = serializer.validated_data.get('target_date')
        villa = unit.villa
        building = unit.building

        message = '{} {} {}\n{}년 {}월 {}일 중간정산이 취소되었습니다.\n\n'.format(villa.name, building.building_name, unit.unit_number, target_date.year, target_date.month,target_date.day ) 


        data = {
            'message': {
                'to': unit.phone_number,
                'from': '16602606',
                'kakaoOptions': {
                'pfId': 'KA01PF220417023828732kAeE8jCxWjw',
                'templateId': 'KA01TP2205130538216260PupiLmTyYK',

                'variables':{ 
                    '#{건물이름}':villa.name, 
                    '#{동이름}': building.building_name,
                    '#{호이름}': unit.unit_number,
                    '#{년월일}': '{}년 {}월 {}일'.format(target_date.year, target_date.month, target_date.day),
                    '#{호id}': unit.id,
                }
                },
            } 
        }

        res = send_message.send_one(data)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

        serializer.save(sender=self.request.user, unit=unit,
                        building=building, villa=villa, message=message)

