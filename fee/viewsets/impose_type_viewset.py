from rest_framework import viewsets
from ..serializers import ImposeTypeSerializer 
from ..models import ImposeType 

class ImposeTypeViewSet(viewsets.ModelViewSet): 

    queryset = ImposeType.objects.all()
    serializer_class = ImposeTypeSerializer 



