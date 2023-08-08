from django_filters import rest_framework as filters

from ..models import VillaFee


class VillaFeeFilter(filters.FilterSet):
    class Meta:
        model = VillaFee
        fields = {
            'date_created': ['month', 'year'],
            'villa': ['exact'],
            'fee_type': ['exact'],
            'villa_id': ['exact']
        }
