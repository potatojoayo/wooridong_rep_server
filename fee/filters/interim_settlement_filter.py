from django_filters import rest_framework as filters

from ..models import InterimSettlement

class InterimSettlementFilter(filters.FilterSet):

    class Meta:

        model = InterimSettlement
        fields = {
            'sent_date': ['gte','lte'],
            'target_date': ['gte','lte'],
            'unit': ['exact'],
        }



