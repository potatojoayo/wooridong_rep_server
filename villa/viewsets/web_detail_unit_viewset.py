from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Unit
from ..serializers import WebUnitDetailSerializer



class WebDetailUnitViewSet(viewsets.ModelViewSet): 


    permission_classes = [AllowAny]

    queryset = Unit.objects.all()
    serializer_class = WebUnitDetailSerializer



    

    

