import logging

from django.conf import settings

from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from notification.methods.before_pay_villa_fee import before_pay_villa_fee

logger = logging.getLogger(__name__)


@util.close_old_connections
def start():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), 'default')

    scheduler.add_job(
        before_pay_villa_fee,
        trigger=CronTrigger(year='*', month='*', day='*', hour=10),
        id='before_pay_villa_fee',
        max_instances=1,
        replace_existing=True
    )
    logger.info('공과금 결제 3일 전 알림')

    try:
        scheduler.start()
        logger.info('스케쥴러 시작')
    except (SystemExit):
        logger.info('스케쥴러 정지중..')
        scheduler.shutdown()
        logger.info('스케쥴러 성공적으로 정지')
