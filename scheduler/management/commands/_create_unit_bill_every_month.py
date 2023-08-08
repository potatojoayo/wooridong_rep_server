from datetime import datetime
from dateutil import relativedelta
from fee.models import UnitBill


def create_unit_bill_every_month():
    now = datetime.now()
    previous_date = now - relativedelta.relativedelta(months=1)

    unit_bills = UnitBill.objects.filter(date_created__year=previous_date.year, date_created__month=previous_date.month)
    for unit_bill in  unit_bills:
        UnitBill.objects.create(unit=unit_bill.unit, villa=unit_bill.villa, person_count=unit_bill.person_count, phone_number=unit_bill.phone_number)