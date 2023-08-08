from django.db import transaction
from rest_framework import viewsets

from utils.format_phone import format_phone
from villa.models import Villa
from ..methods import send_bill_message
from ..models import BillMessage
from fee.models import UnitBill, SentVillaFee, VillaFee, SentUnitFee, SentUnitBill
from ..serializers import BillMessageSerializer
from src.lib import message as send_message
from ..filters import BillMessageFilter
import json
import os

from datetime import datetime
from dateutil import parser


class BillMessageViewSet(viewsets.ModelViewSet):
    serializer_class = BillMessageSerializer
    filterset_class = BillMessageFilter

    def get_queryset(self):
        return BillMessage.objects.filter(villa=self.request.user.villa.get())

    @transaction.atomic()
    def perform_create(self, serializer):
        date = self.request.query_params.get('date')
        if date is None:
            date = datetime.now()
        unit = serializer.validated_data.get('unit')
        villa: Villa = unit.villa
        building = unit.building

        send_bill_message(unit=unit, date=date)
        
        serializer.save(sender=self.request.user, unit=unit,
                        building=building, villa=villa)
