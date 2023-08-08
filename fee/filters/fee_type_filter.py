from django_filters import rest_framework as filters

from ..models import FeeType

class FeeTypeFilter(filters.FilterSet):

    class Meta:
        model =  FeeType
        fields = {
            'name': ['icontains',
                     'exact']

        }
