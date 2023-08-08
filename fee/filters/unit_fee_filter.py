from django_filters import rest_framework as filters

from ..models import UnitFee 

class UnitFeeFilter(filters.FilterSet):

    class Meta: 
        model =  UnitFee 
        fields = {
            'date_created': ['month', 'year'],
            'unit': ['exact'],
            'fee_type': ['exact'],
        }
