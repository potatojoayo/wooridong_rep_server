from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from bank.models import Bank
from fee.models import VillaFee, FeeType, UnitFee, UnitBill
from villa.models import Unit


@csrf_exempt
@api_view(['POST'])
def create_unit_fee(request: Request):
    unit_id = request.data['unit_id']
    fee_type_name = request.data['fee_type_name']
    fee = request.data['fee']
    fee_type,_ = FeeType.objects.get_or_create(name=fee_type_name)
    unit = Unit.objects.get(pk=unit_id)
    now = datetime.now()
    unit_bill = UnitBill.objects.get(date_created__year=now.year, date_created__month=now.month, unit=unit)
    unit_bill.total_fee += fee
    unit_bill.save()
    UnitFee.objects.create(unit_id=unit_id,fee_type=fee_type,fee=fee, building=unit.building, unit_bill=unit_bill, is_individual=True)
    return Response(status=200)
