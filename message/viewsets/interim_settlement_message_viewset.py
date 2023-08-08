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


class InterimSettlementMessageViewSet(viewsets.ModelViewSet):

    serializer_class = InterimSettlementMessageSerializer
    filterset_class = InterimSettlementMessageFilter

    def get_queryset(self): 
        return InterimSettlementMessage.objects.filter(rep=self.request.user)

    def perform_create(self, serializer):
        now = datetime.now() 
        unit = serializer.validated_data.get('unit')
        target_date = serializer.validated_data.get('target_date')
        villa = unit.villa
        building = unit.building
        interim_settlement = InterimSettlement.objects.filter(unit=unit,sent_date__month=now.month).order_by('-sent_date')[0]
        fee_messages = []
        for key, value in interim_settlement.fees.items(): 
            fee_messages.append('{}: {}원\n'.format(key,format(value,','))) 

        message = '{} {} {}\n{}년 {}월 {}일 중간정산\n\n'.format(villa.name, building.building_name, unit.unit_number, target_date.year, target_date.month,target_date.day )

        message += ''.join(fee_messages)

        message += '\n합계: {}원\n\n{} {}\n예금주: {}\n입금 바랍니다.\n\n상세보기\nhttps://dev.wooridong-rep.net/unit-detail-web?unit={}'.format(
            format(interim_settlement.total_fee, ','), villa.bank.name, villa.bank_account, villa.account_owner, unit.id)



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
                    '#{관리비내역}': ''.join(fee_messages) + '\n\n합계: {}원\n'.format(format(interim_settlement.total_fee,',')),
                    '#{은행}': villa.bank.name,
                    '#{계좌번호}': villa.bank_account,
                    '#{호id}': unit.id,
                    '#{예금주}': villa.account_owner,
                }
                },
            } 
        }

        res = send_message.send_one(data)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

        serializer.save(sender=self.request.user, unit=unit,
                        building=building, villa=villa, message=message)

