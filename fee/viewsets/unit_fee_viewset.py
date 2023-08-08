from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response
from villa.models.building import Building
from ..models import UnitFee, VillaFee, ImposeFeeOnUnit, UnitBill
from ..serializers import UnitFeeSerializer,UnitFeeCreateSerializer 
from ..filters import UnitFeeFilter
from datetime import datetime
import math

class UnitFeeViewSet(viewsets.ModelViewSet):

    queryset = UnitFee.objects.all()
    filterset_class = UnitFeeFilter 

    def perform_create(self, serializer): 
        now = datetime.now()
        unit_bill = UnitBill.objects.get(date_created__year=now.year, date_created__month = now.month,unit=self.request.data.get('unit'))
        unit_fee = serializer.save(unit_bill=unit_bill)

        try:
            villa_fee = unit_fee.villa_fee
            villa_fee.imposing_person_count += 1
            villa_fee.fee += unit_fee.fee
            villa_fee.save()
        except ObjectDoesNotExist:
            pass
        unit_bill.total_fee += unit_fee.fee
        unit_bill.save()

        return unit_fee 

    def get_serializer_class(self):

        if self.action == 'update' or self.action == 'create' or self.request.method == 'PATCH':
            return UnitFeeCreateSerializer 
        return UnitFeeSerializer 

    def perform_destroy(self, instance): 
        
        unit_fee = instance
        now = datetime.now()
        unit_bill = UnitBill.objects.get(date_created__year=now.year, date_created__month = now.month,unit=unit_fee.unit)
        unit_bill.total_fee -= unit_fee.fee
        unit_bill.save()
        instance.delete()



    def partial_update(self, request, *args, **kwargs):

        kwargs['partial'] = True

        unit_fee = self.get_object() 
        fee = request.data.get('fee')


        if fee is not None and unit_fee.fee != fee: 
            diff = unit_fee.fee - fee
            try:
                villa_fee = unit_fee.villa_fee
                villa_fee.fee -= diff
                villa_fee.save()
            except ObjectDoesNotExist:
                pass

            now = datetime.now()
            unit_bill = UnitBill.objects.get(date_created__year=now.year, date_created__month = now.month,unit=unit_fee.unit)
            unit_bill.total_fee -= diff 
            unit_bill.save()

        return self.update(request, *args, **kwargs)


