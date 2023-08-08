import sys

from django.apps import AppConfig


class BankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bank'

    def ready(self):
        if 'runserver' in sys.argv:
            from .models import Bank
            banks = {
                "산업은행": ["002", "/media/images/bank/sanup.png"],
                "기업은행": ["003", "/media/images/bank/giup.png"],
                "국민은행": ["004", "/media/images/bank/kookmin.png"],
                "수협중앙회": ["007", "/media/images/bank/suhyup.png"],
                "농협은행": ["011", "/media/images/bank/nonghyup.png"],
                "지역농축협": ["012", "/media/images/bank/nonghyup.png"],
                "우리은행": ["020", "/media/images/bank/woori.png"],
                "SC은행": ["023", "/media/images/bank/sc.png"],
                "한국씨티은행": ["027", "/media/images/bank/citi.png"],
                "대구은행": ["031", "/media/images/bank/daegu.png"],
                "부산은행": ["032", "/media/images/bank/pusan.png"],
                "광주은행": ["034", "/media/images/bank/kwangju.png"],
                "제주은행": ["035", "/media/images/bank/jeju.png"],
                "전북은행": ["037", "/media/images/bank/jeonbook.png"],
                "경남은행": ["039", "/media/images/bank/kyungnam.png"],
                "새마을금고": ["045", "/media/images/bank/saemaul.png"],
                "신협": ["048", "/media/images/bank/sinhyupjungang.png"],
                "우체국": ["071", "/media/images/bank/uchegook.png"],
                "하나은행": ["081", "/media/images/bank/hana.png"],
                "신한은행": ["088", "/media/images/bank/shinhan.png"],
                "K뱅크": ["089", "/media/images/bank/kay.png"],
                "카카오뱅크": ["090", "/media/images/bank/kakao.png"],
                "토스뱅크": ["092", "/media/images/bank/toss.png"],
            }

            for key, value in banks.items():
                if not Bank.objects.filter(name=key).exists():
                    Bank(name=key, code=value[0], image_url=value[1]).save()
