from rest_framework import serializers
from datetime import datetime
from dateutil import parser
from fee.models.unit_bill import UnitBill
from fee.serializers.unit_bill_depth_one_serializer import UnitBillDepthOneSerializer
from ..models import Unit


class UnitWithBillSerializer(serializers.ModelSerializer):
    current_month_bill = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_current_month_bill(self, obj):

        request = self.context.get('request')
        date = datetime.now()
        if request is not None:
            date = request.query_params.get('bill_date')
            if date is not None:
                date = parser.parse(date)
        if date is None:
            date = datetime.now()
        current_month_bill_query_set = UnitBill.objects.get(unit=obj, date_created__month=date.month, date_created__year=date.year)
        return UnitBillDepthOneSerializer(current_month_bill_query_set).data
