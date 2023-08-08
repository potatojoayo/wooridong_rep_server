from django_filters import rest_framework as filters

from ..models import Unit

class UnitFilter(filters.FilterSet):

    class Meta:
        model = Unit 
        fields = '__all__'
