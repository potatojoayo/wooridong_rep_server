from dateutil import parser

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from fee.serializers import UnitBillWithUnitSerializer


@csrf_exempt
@api_view(['POST'])
def unit_bills(request: Request):
    user = request.user
    date = parser.parse(request.data['date'])
    villa = user.villa.get()
    buildings = villa.buildings.all()
    data = []

    for building in buildings:
        obj = {}
        building_name = building.building_name if building.building_name else '{}'.format(str(building.building_number) + '동')
        obj['building_name'] = building_name
        obj['unit_bills'] = []

        units = building.units.filter(does_exist=True).order_by('floor', 'line')
        unit_bills = []

        for unit in units:
            unit_bill = unit.unit_bills.get(date_created__year=date.year, date_created__month=date.month)
            serializer = UnitBillWithUnitSerializer(unit_bill)
            unit_bills.append(serializer.data)

        obj['unit_bills'] = unit_bills
        data.append(obj)


    return Response(status=200, data=data)
