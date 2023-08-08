from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..filters import UnitBillFilter
from ..models import UnitBill, UnitFee
from ..serializers import UnitBillDepthOneSerializer, UnitBillSerializer

from django.core.exceptions import ObjectDoesNotExist

class UnitBillViewSet(viewsets.ModelViewSet):
    filterset_class = UnitBillFilter
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.query_params.get('no_depth'):
            return UnitBillSerializer
        if self.action == 'list' or self.action == 'retrieve':
            return UnitBillDepthOneSerializer
        return UnitBillSerializer

    def partial_update(self, request, *args, **kwargs):

        kwargs['partial'] = True
        instance = self.get_object()

        paid_date = request.data.get('paid_date')

        now = datetime.now()

        now = datetime(now.year, now.month, 1)

        # 미납금 수금
        if instance.date.month < now.month:

            pay = None

            if paid_date is not None and instance.paid_date is None:
                pay = True
            elif paid_date is None and instance.paid_date is not None:
                pay = False

            unit_bill = instance
            total_fee = unit_bill.total_fee

            while True:

                next_month = unit_bill.date + relativedelta(months=+1)
                next_month_unit_bill = UnitBill.objects.get(unit=unit_bill.unit, date_created__year=next_month.year,
                                                            date_created__month=next_month.month)

                print(next_month_unit_bill)
                try:
                    unpaid_unit_fee = UnitFee.objects.get(unit_bill=next_month_unit_bill, fee_type_id=29)
                except:
                    unpaid_unit_fee = UnitFee.objects.create(unit_bill=next_month_unit_bill, fee_type_id=29,
                                                             villa_fee=None, building=unit_bill.unit.building,
                                                             unit=unit_bill.unit, fee=0, date=next_month, pay_date=None)
                    # 과거 미납금 수금 완료 시
                if pay == True:
                    next_month_unit_bill.total_fee -= total_fee
                    unpaid_unit_fee.fee = 0

                # 과거 미납금 수금 미완료 시
                else:
                    next_month_unit_bill.total_fee += total_fee
                    unpaid_unit_fee.fee = total_fee

                next_month_unit_bill.save()
                unpaid_unit_fee.save()

                if next_month_unit_bill.paid_date != None or (
                        next_month.year == now.year and next_month.month == now.month):
                    print('미수금 계산 종료')
                    break

                else:
                    unit_bill = next_month_unit_bill

        return self.update(request, *args, **kwargs)

    def get_queryset(self):

        if self.request.user.is_anonymous:
            return UnitBill.objects.all().order_by('-date_created')
        # return UnitBill.objects.filter(villa=self.request.user.villa.get()).order_by('-date')
        try:
            self.request.user.villa.get()
        except ObjectDoesNotExist:
            return UnitBill.objects.filter(villa=self.request.user.my_unit.get().villa).order_by('-date_created')
        else:
            return UnitBill.objects.filter(villa=self.request.user.villa.get()).order_by('-date_created')
