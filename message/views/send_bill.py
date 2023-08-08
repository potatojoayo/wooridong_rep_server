from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from message.methods import send_bill_message
from notification.models import Notification

from dateutil import parser

from villa.models import Unit


@api_view(['POST'])
@transaction.atomic()
def send_bills(request: Request):
    villa = request.user.villa.get()
    date = parser.parse(request.data.get('date'))
    unit = Unit.objects.get(pk=request.data.get('unit'))
    send_bill_message(unit=unit, date=date)
    Notification.objects.create(user=villa.rep, target_type=2, notification_type=2,
                                message='{}년 {}월 {} {} 관리비 고지서를 발송했습니다.'.format(date.year, date.month, unit.building.building_name, unit.unit_number))

    return Response(200)

