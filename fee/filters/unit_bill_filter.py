from django_filters import rest_framework as filters

from ..models import UnitBill

class UnitBillFilter(filters.FilterSet):

    class Meta:

        model = UnitBill
        fields = {
            'date_created': ['month', 'year'],
            'unit': ['exact'],
        }



