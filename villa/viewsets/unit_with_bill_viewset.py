from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Unit, Building
from fee.models.unit_fee import UnitFee
from fee.models.unit_bill import UnitBill
from fee.models.impose_fee_on_unit import ImposeFeeOnUnit
from fee.models.villa_fee import VillaFee
from ..serializers import UnitWithBillSerializer
from ..filters import UnitFilter
from datetime import datetime
import math

class UnitWithBillViewSet(viewsets.ModelViewSet):


    serializer_class = UnitWithBillSerializer
    filterset_class = UnitFilter

    def get_queryset(self):
        # return Unit.objects.filter(villa=self.request.user.villa.get(), floor__gte=0).order_by('-floor','-line')
        try:
            self.request.user.villa.get()
        except ObjectDoesNotExist:
            return Unit.objects.filter(villa=self.request.user.my_unit.get().villa, floor__gte=0).order_by('-floor',
                                                                                                           '-line')
        else:
            return Unit.objects.filter(villa=self.request.user.villa.get(), floor__gte=0).order_by('pk')




