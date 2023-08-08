from datetime import datetime
import math
from django.core.exceptions import ObjectDoesNotExist

from fee.models import UnitBill
from fee.models.villa_fee import VillaFee
from fee.models.impose_fee_on_unit import ImposeFeeOnUnit
from fee.models.unit_fee import UnitFee


def update_fee_when_villa_fee_changes(villa_fee: VillaFee):
    now = datetime.now()

    villa = villa_fee.villa
    print(villa_fee)
    print(villa_fee.impose_type)
    for building in villa.buildings.all():
        for unit in building.units.filter(does_exist=True):
            print('fee_type: {}, unit: {}, now.year: {}, now.month: {}'.format(villa_fee.fee_type, unit.unit_number,
                                                                               now.year, now.month))
            try:
                unit_fee = UnitFee.objects.get(fee_type=villa_fee.fee_type, unit=unit, date_created__year=now.year,
                                           date_created__month=now.month)
            except ObjectDoesNotExist:
                continue
            # UnitBill 초기화
            unit_bill = UnitBill.objects.get(unit=unit, date_created__year=now.year, date_created__month=now.month)
            unit_bill.total_fee -= unit_fee.fee
            # UnitFee 업데이트

            impose_fee_on_unit = ImposeFeeOnUnit.objects.get(villa_fee=villa_fee, unit=unit_fee.unit)
            # 부과 대상 유닛에만 적용
            if impose_fee_on_unit.do_impose and villa_fee.fee is not None:
                # ImposeType(부과방식)에 따라 달리 계산
                if villa_fee.impose_type.name == '세대별부과':
                    try:
                        unit_fee.fee = int(math.ceil(villa_fee.fee / villa_fee.imposing_unit_count / 10) * 10)
                    except ZeroDivisionError:
                        unit_fee.fee = 0
                elif villa_fee.impose_type.name == '세대구성원별부과' and unit_fee.unit.person_count is not None:
                    try:
                        unit_fee.fee = int(math.ceil(
                            unit_fee.unit.person_count * (
                                        villa_fee.fee / villa_fee.imposing_person_count) / 10) * 10)
                    except ZeroDivisionError:
                        unit_fee.fee = 0
            else:
                unit_fee.fee = 0

            # UnitBill 업데이트
            unit_bill.total_fee += unit_fee.fee
            unit_bill.save()
            unit_fee.save()

