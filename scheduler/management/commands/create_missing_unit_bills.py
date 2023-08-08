from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore

from fee.models import UnitBill
from scheduler.management.commands._create_unit_bill_every_month import create_unit_bill_every_month


class Command(BaseCommand):
    help = '빠진 UnitBill 생성'

    def handle(self, *args, **options):

        unit_bills = UnitBill.objects.filter(date_created__year=2023, date_created__month=2)
        for unit_bill in unit_bills:
            print(unit_bill.unit.unit_number)
            UnitBill.objects.create(unit=unit_bill.unit, villa=unit_bill.villa, person_count=unit_bill.person_count, phone_number=unit_bill.phone_number, date_created=datetime(2022, 3,1))
            UnitBill.objects.create(unit=unit_bill.unit, villa=unit_bill.villa, person_count=unit_bill.person_count, phone_number=unit_bill.phone_number, date_created=datetime(2022, 4,1))

