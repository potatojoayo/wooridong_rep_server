from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from fee.methods import update_fee_when_villa_fee_changes
from fee.models import ImposeFeeOnUnit, VillaFee
from villa.models import Unit


@csrf_exempt
@api_view(['POST'])
def change_do_impose(request: Request):
    villa_fee_id = request.data['villa_fee_id']
    unit_do_imposes = request.data['unit_do_impose']
    villa_fee = VillaFee.objects.get(pk=villa_fee_id)
    for unit_do_impose in unit_do_imposes:
        unit_id =  unit_do_impose['unit_id']
        do_impose = unit_do_impose['do_impose']
        impose_fee_on_unit = ImposeFeeOnUnit.objects.get(unit_id=unit_id,
                                                         villa_fee_id=villa_fee_id)
        impose_fee_on_unit.do_impose = do_impose
        impose_fee_on_unit.save()
    imposing_unit_count = 0
    imposing_person_count = 0
    impose_fee_on_units = ImposeFeeOnUnit.objects.filter(villa_fee_id=villa_fee_id)
    for impose_fee_on_unit in impose_fee_on_units:
        if impose_fee_on_unit.do_impose:
            imposing_unit_count += 1
            imposing_person_count += impose_fee_on_unit.unit.person_count if impose_fee_on_unit.unit.person_count else 0
    villa_fee.imposing_person_count = imposing_person_count
    villa_fee.imposing_unit_count = imposing_unit_count
    villa_fee.save()
    update_fee_when_villa_fee_changes(villa_fee=villa_fee)
    return Response(status=200)