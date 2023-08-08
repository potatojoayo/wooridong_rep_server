from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore

from scheduler.management.commands._create_unit_bill_every_month import create_unit_bill_every_month


class Command(BaseCommand):
    help = 'APScheduler 시작'

    def handle(selfself, *args, **options):

        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), 'default')

        scheduler.add_job(
            create_unit_bill_every_month,
            trigger=CronTrigger(day=1, hour=0, minute=0, second=0),
            id='유닛빌 생성',
            max_instances=1,
            replace_existing=True
        )

        print('유닛빌 생성 스케쥴러 추가')

        try:
            print('스케쥴러 시작...')
            scheduler.start()
        except:
            print('스케줄러 중지중...')
            scheduler.shutdown()
            print('스케줄러 중지됨')
