from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from fee.models import UnitBill


@csrf_exempt
@api_view(['GET'])
def get_count_unpaid_unit_bills(request):
    villa = request.user.villa.get()
    count = UnitBill.objects.filter(villa=villa, paid_date__isnull=True).count()
    return Response(status=200, data={
        'count': count
    })
