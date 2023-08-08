from django.core.management.base import BaseCommand, CommandError
from fee.methods.create_new_month_fixed_fees import create_new_month_fixed_fees

class Command(BaseCommand):

    help = '새로운 달 요금 생성'

    def add_arguments(self, parser):
        parser.add_argument('villa_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for villa_id in options['villa_ids']:
            try:
                create_new_month_fixed_fees(villa_id=villa_id)
            except Exception as e:
                print(e)
                raise CommandError('새로운 달 생성 중 오류가 발생하였습니다. - villa id :',villa_id) 

        self.stdout.write(self.style.SUCCESS('새로운달 요금이 성공적으로 생성되었습니다.'))
            

