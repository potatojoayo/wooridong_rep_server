from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from fee.models import VillaFee


@csrf_exempt
@api_view(['POST'])
def check_villa_fee_duplicated(request: Request):
    villa = request.user.villa.get()
    fee_name = request.data['fee_name']
    now = datetime.now()
    is_duplicated = VillaFee.objects.filter(
        date_created__year=now.year,
        date_created__month=now.month,
        villa=villa,
        fee_type__name=fee_name
    ).exists()
    return Response(status=200, data={
        'is_duplicated': is_duplicated
    })
