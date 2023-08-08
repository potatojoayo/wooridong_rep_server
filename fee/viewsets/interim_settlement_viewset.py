import math
from calendar import monthrange
from datetime import datetime,timedelta
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from ..models import InterimSettlement
from ..serializers import InterimSettlementSerializer
from ..filters import InterimSettlementFilter 
from src.lib import message as send_message
import json


from ..models import UnitBill,UnitFee


class InterimSettlementViewSet(ModelViewSet): 

    permission_classes = [AllowAny]

    filterset_class = InterimSettlementFilter
    serializer_class = InterimSettlementSerializer

    def get_queryset(self):

        #return InterimSettlement.objects.filter(unit__villa=self.request.user.villa.get())
        return InterimSettlement.objects.all()

    def perform_create(self,serializer): 

        now = datetime.now()
        target_date = serializer.validated_data.get('target_date')
        days = monthrange(target_date.year, target_date.month)[1]
        day_ratio = target_date.day / days
        unit = serializer.validated_data.get('unit')
        weight = float(self.request.query_params.get('weight'))
        before_4_month = now.replace(day=1) - timedelta(days=110)
        before_4_month = before_4_month.replace(day=1)
        unit_bill = UnitBill.objects.get(unit=unit,date__year=now.year,date__month=now.month) 
        past_unit_bills = UnitBill.objects.filter(unit=unit,date__gte=before_4_month,date__lt=now.replace(day=1)) 
        fees = {}
        total_fee = 0
        if len(past_unit_bills) > 0: 
            for past_unit_bill in past_unit_bills:
                for uf in past_unit_bill.unit_fees.all():
                    if uf.villa_fee is None:
                        continue
                    if uf.villa_fee.fee <= 0:
                        continue
                    if uf.villa_fee.fee_type.name == '미납금':
                        continue
                    if not uf.villa_fee.individual:
                        if uf.fee_type.name in fees:
                            fees[uf.fee_type.name] += uf.fee
                        else:
                            fees[uf.fee_type.name] = uf.fee
            for key in reversed(list(fees.keys())):
                fees[key] = math.ceil(((fees[key]//len(past_unit_bills))*day_ratio) * float(weight)/10)*10 
                total_fee += fees[key] 
        else:
            for uf in unit_bill.unit_fees.all():
                if uf.villa_fee is None:
                    continue 
                if uf.villa_fee.fee <= 0:
                    continue
                if uf.villa_fee.fee_type.name == '미납금':
                    continue
                if not uf.villa_fee.individual:
                    if uf.fee_type.name in fees:
                        fees[uf.fee_type.name] += uf.fee
                    else:
                        fees[uf.fee_type.name] = uf.fee
            for key in reversed(list(fees.keys())):
                fees[key] = math.ceil((fees[key]*day_ratio) * float(weight)/10)*10 
                total_fee += fees[key] 
        for uf in unit_bill.unit_fees.all(): 
            if uf.villa_fee is None:
                continue
            if uf.villa_fee.individual:
                fees[uf.fee_type.name] = uf.fee
                total_fee += uf.fee



        serializer.save(unit_bill=unit_bill,fees=fees,total_fee=math.ceil(total_fee/10)*10)


    def partial_update(self, request, *args, **kwargs): 

        kwargs['partial'] = True
        instance = self.get_object() 
        now = datetime.now() 

        cancel_date = self.request.data.get('cancel_date')
        if cancel_date is not None:

            unit = instance.unit
            target_date = instance.target_date
            villa = unit.villa
            building = unit.building
            unit_bill = UnitBill.objects.get(
                unit=unit, date_created__year=now.year, date_created__month=now.month)
            unit_fees = unit_bill.unit_fees.all()
            interim_settlement = instance 

            message = '{} {} {}\n{}년 {}월 {}일 중간정산이 취소되었습니다.\n\n'.format(villa.name, building.building_name, unit.unit_number, target_date.year, target_date.month,target_date.day ) 


            data = {
                'message': {
                    'to': unit.phone_number,
                    'from': '16602606',
                    'kakaoOptions': {
                    'pfId': 'KA01PF220417023828732kAeE8jCxWjw',
                    'templateId': 'KA01TP2205180404494953ke5TtPhAws',

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



        return self.update(request, *args, **kwargs)

         
        
        
        
        
        








    

