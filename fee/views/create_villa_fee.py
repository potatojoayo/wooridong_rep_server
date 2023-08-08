from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from fee.models import VillaFee
from fee.serializers import VillaFeeSerializer


@csrf_exempt
@api_view(['POST'])
def create_villa_fee(request: Request):
    villa_fee = request.data['villa_fee']
    villa_fee.pop('villa_id',None)
    villa = request.user.villa.get()
    print(villa_fee)
    villa_fee = VillaFee.objects.create(villa=villa,**villa_fee)
    serializer = VillaFeeSerializer(villa_fee)
    return Response(status=200, data=serializer.data)

