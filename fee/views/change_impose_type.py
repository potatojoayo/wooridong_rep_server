from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from fee.methods import update_fee_when_villa_fee_changes
from fee.models import VillaFee, ImposeType


@csrf_exempt
@api_view(['PATCH'])
def change_impose_type(request: Request):
    villa_fee_id = request.data.get('villa_fee_id')
    impose_type_name = request.data.get('impose_type_name')
    print(impose_type_name)
    villa_fee = VillaFee.objects.get(pk=villa_fee_id)
    impose_type = ImposeType.objects.get(name=impose_type_name)
    villa_fee.impose_type = impose_type
    villa_fee.save()
    update_fee_when_villa_fee_changes(villa_fee=villa_fee)
    print(villa_fee.impose_type)
    return Response(status=200)
