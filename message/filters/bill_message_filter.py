from django_filters import rest_framework as filters

from ..models import BillMessage 

class BillMessageFilter(filters.FilterSet):

    class Meta:
        model = BillMessage 
        fields = {
            'unit': [ 'exact'],
            'sent_date': ['gte', 'lte']
        }
