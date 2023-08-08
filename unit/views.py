import math
from django.db import transaction
from django.shortcuts import render

from fee.models import UnitBill


@transaction.atomic()
def detail_view(request, unit_bill_id=None):
    unit_bill = UnitBill.objects.get(pk=unit_bill_id)
    unit = unit_bill.unit
    villa = unit.villa
    building = unit.building
    building_name = building.building_name
    date = '{}년 {}월'.format(unit_bill.date_created.year, unit_bill.date_created.month)
    unit_fees = unit_bill.unit_fees.all()
    fee_total = unit_bill.total_fee
    for sent_unit_fee in unit_fees:
        sent_unit_fee.fee = format(math.ceil(sent_unit_fee.fee), ',d')
    price_to_pay = fee_total
    fee_total = format(fee_total, ',d')
    amount = price_to_pay
    if not building.building_name:
        building_name = str(building.building_number + 1) + '동'

    return render(request=request, template_name='unit/detail.html', context={
        'unit_fees': unit_fees,
        'date': date,
        'price_to_pay': '{:,}'.format(price_to_pay),
        'unit_bill': unit_bill,
        'unit': unit,
        'amount': amount,
        'villa': villa,
        'building_name': building_name,
        'fee_total': fee_total,
        'user': request.user
    })
