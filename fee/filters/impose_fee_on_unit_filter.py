from django_filters import rest_framework as filters

from ..models import ImposeFeeOnUnit 


class ImposeFeeOnUnitFilter(filters.FilterSet):

    class Meta:
        model = ImposeFeeOnUnit 
        fields = {
            'villa_fee_id': ['exact']
        }
