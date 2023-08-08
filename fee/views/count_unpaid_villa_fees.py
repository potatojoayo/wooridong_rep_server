from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from fee.models import VillaFee


@csrf_exempt
@api_view(['GET'])
def get_count_unpaid_villa_fees(request):
    villa = request.user.villa.get()
    count = VillaFee.objects.filter(villa=villa, pay_date__isnull=True).count()
    return Response(status=200, data={
        'count': count
    })
