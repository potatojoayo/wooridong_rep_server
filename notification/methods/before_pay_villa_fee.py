import json
from datetime import datetime, timedelta

from notification.models import Notification
from villa.models import Villa
from src.lib import message as send_message


def before_pay_villa_fee():
    three_days_ago = datetime.today() - timedelta(days=3)
    year = three_days_ago.year
    month = three_days_ago.month
    day = three_days_ago.month
    villas = Villa.objects.all()
    for villa in villas:
        villa_fees = villa.villa_fees.filter(date_created__year=year,
                                             date_created__month=month,
                                             date_created__day=day
                                             )
        for villa_fee in villa_fees:
            wallet = villa.wallet
            pay = ''
            if wallet.balance < villa_fee.fee:
                pay = '우리동페이가 부족합니다. 충전해주세요.'
            data = {
                'message': {
                    'to': villa.rep.phone_number,
                    'from': '16602606',
                    'kakaoOptions': {
                        'pfId': 'KA01PF220417023828732kAeE8jCxWjw',
                        'templateId': 'KA01TP230116021236650CFWeCBJLWCS',
                        'variables': {
                            '#{공과금명}': villa_fee.fee_type.name,
                            '#{금액}': format(villa_fee.fee, ',d'),
                            '#{우리동페이}': pay,
                        }
                    },
                }
            }

            res = send_message.send_one(data)
            Notification.objects.create(
                user=villa.rep,
                target_type=3,
                notification_type=3,
                message='3일 후 {} {}원이 납부될 예정입니다. \n{}'.format(villa_fee.fee_type.name,
                                                              format(villa_fee.fee, ',d'),
                                                              pay
                                                              )
            )

            print(json.dumps(res.json(), indent=2, ensure_ascii=False))
