from rest_framework import viewsets
from ..serializers import FeeTypeSerializer
from ..models import FeeType
from ..filters import FeeTypeFilter


class FeeTypeViewSet(viewsets.ModelViewSet): 

    queryset = FeeType.objects.all()
    serializer_class = FeeTypeSerializer
    filterset_class = FeeTypeFilter

