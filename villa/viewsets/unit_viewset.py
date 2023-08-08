from rest_framework import viewsets
from datetime import datetime

from fee.models.unit_bill import UnitBill
from ..models import Unit
from ..serializers import UnitSerializer

from django.core.exceptions import ObjectDoesNotExist


class UnitViewSet(viewsets.ModelViewSet):
    serializer_class = UnitSerializer

    def get_queryset(self):
        try:
            self.request.user.villa.get()
        except ObjectDoesNotExist:
            return Unit.objects.filter(villa=self.request.user.my_unit.get().villa, floor__gte=0)
        else:
            return Unit.objects.filter(villa=self.request.user.villa.get(), floor__gte=0)

    def perform_create(self, serializer):

        now = datetime.now()
        unit = serializer.save(rep=self.request.user)
        UnitBill.objects.create(
            unit=unit, total_fee=0, villa=self.request.user.villa.get())
        unit.save()

        return unit

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        now = datetime.now()
        changing_person_count = request.data.get('person_count')
        changing_phone_number = request.data.get('phone_number')
        update_fee = request.data.get('update_fee')

        # 전화번호 변경 시 이번 달 UnitBill 전화번호도 변경
        if changing_phone_number is not None:
            ub = UnitBill.objects.get(
                date_created__year=now.year, date_created__month=now.month, unit=instance)
            ub.phone_number = changing_phone_number
            ub.save()

            # Unit update
            unit = instance
            unit.phone_number = changing_phone_number
            unit.save()

        # 세대 구성원 수 변경 시 요금 재계산
        if changing_person_count is not None:
            from fee.methods import update_fee_when_villa_fee_changes

            changing_person_count = int(changing_person_count)

            ub = UnitBill.objects.get(
                date_created__year=now.year, date_created__month=now.month, unit=instance)
            ub.person_count = changing_person_count
            ub.save()

            if instance.person_count is None:
                difference = changing_person_count
            else:
                difference = changing_person_count - instance.person_count

            instance.person_count = changing_person_count
            instance.save()
            villa_fees = instance.villa.villa_fees.filter(
                date_created__year=now.year, date_created__month=now.month)
            for villa_fee in villa_fees:
                villa_fee.imposing_person_count += difference
                villa_fee.save()
                if update_fee is True and not villa_fee.individual:
                    update_fee_when_villa_fee_changes(villa_fee)

        return self.update(request, *args, **kwargs)
