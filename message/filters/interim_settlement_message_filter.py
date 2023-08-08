from django_filters import rest_framework as filters

from ..models import InterimSettlementMessage 

class InterimSettlementMessageFilter(filters.FilterSet):

    class Meta:
        model = InterimSettlementMessage 
        fields = {
            'unit': [ 'exact'],
            'sent_date': ['gte', 'lte']
        }
