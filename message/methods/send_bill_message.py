import os
from datetime import datetime

from fee.models import UnitBill
from message.models import BillMessage
from utils.format_phone import format_phone
from villa.models import Villa, Unit
from src.lib import message as send_message


def send_bill_message(unit: Unit, date=None,):
    #
    # for villa_fee in villa_fees:
    #     try:
    #         SentVillaFee.objects.create(
    #             villa=villa,
    #             fee_type=villa_fee.fee_type,
    #             fee=villa_fee.fee,
    #             due_date=villa_fee.due_date,
    #             imposing_unit_count=villa_fee.imposing_unit_count,
    #             imposing_person_count=villa_fee.imposing_person_count,
    #             individual=villa_fee.individual,
    #             bank=villa_fee.bank,
    #             account_number=villa_fee.account_number,
    #             villa_fee=villa_fee
    #         )
    #     except:
    #         pass
    #
    # sent_unit_bill = SentUnitBill.objects.create(
    #     date=unit_bill.date,
    #     unit=unit,
    #     total_fee=unit_bill.total_fee,
    #     villa=villa,
    #     person_count=unit_bill.person_count,
    #     phone_number=unit_bill.phone_number,
    #     unit_bill=unit_bill
    # )
    #
    # unit_fees = unit_bill.unit_fees.all()
    # for unit_fee in unit_fees:
    #     SentUnitFee.objects.create(
    #         building=unit_fee.building,
    #         unit=unit,
    #         fee_type=unit_fee.fee_type,
    #         fee=unit_fee.fee,
    #         date=unit_fee.date,
    #         sent_unit_bill=sent_unit_bill,
    #         sent_villa_fee=SentVillaFee.objects.get(
    #             villa=villa,
    #             due_date__year=now.year,
    #             due_date__month=now.month,
    #             fee_type=unit_fee.fee_type,
    #         ),
    #         unit_fee=unit_fee,
    #     )

    villa = unit.villa
    print(villa)
    building = unit.building
    unit_bill = UnitBill.objects.get(unit=unit, date_created__year=date.year, date_created__month=date.month)

    data = {
        'message': {
            'to': unit.phone_number,
            'from': '16602606',
            'kakaoOptions': {
                'pfId': 'KA01PF220417023828732kAeE8jCxWjw',
                'templateId': 'KA01TP230210021053303U2lSrNlBaGI',
                'variables': {
                    '#{건물이름}': villa.name,
                    '#{동이름}': building.building_name if building.building_name else '{}동'.format(
                        building.building_number + 1),
                    '#{호이름}': unit.unit_number,
                    '#{동대표이름}': villa.rep.name,
                    '#{동대표번호}': format_phone(villa.rep.phone_number),
                    '#{년월}': '{}년 {}월'.format(date.year, date.month),
                    '#{아이디}': unit_bill.id,
                    '#{도메인}': os.getenv('BASE_URL')
                }
            },
        }
    }

    now = datetime.now()

    BillMessage.objects.create(target_type=0, sent_date=now, unit=unit, villa=villa, building=building)

    send_message.send_one(data)

