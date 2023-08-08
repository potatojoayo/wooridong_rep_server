from rest_framework import viewsets

from ..models import Building 
from ..serializers import BuildingSerializer,BuildingCreateSerializer



class BuildingViewSet(viewsets.ModelViewSet): 
    

    def get_queryset(self):
        return Building.objects.filter(villa=self.request.user.villa.get())

    def get_serializer_class(self):
        if self.action == 'create':
            return  BuildingCreateSerializer
        return BuildingSerializer 



