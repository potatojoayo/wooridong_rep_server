from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from message.methods import send_bill_message
from notification.models import Notification

from dateutil import parser


@api_view(['POST'])
@transaction.atomic()
def send_bills_to_all_units(request: Request):

    villa = request.user.villa.get()
    date = parser.parse(request.data.get('date'))
    for unit in villa.units.all():
        send_bill_message(unit=unit, date=date) 
    Notification.objects.create(user=villa.rep, target_type=0, notification_type=2,
                                message='{}년 {}월 {} 관리비 고지서를 전체 세대에게 발송했습니다.'.format(date.year, date.month, villa.name))

    return Response(200)

