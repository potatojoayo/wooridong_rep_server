from rest_framework import viewsets 
from rest_framework.permissions import AllowAny
from ..models import User
from ..serializers import UserSerializer


class UserAllowAnyViewSet(viewsets.ModelViewSet): 
    

    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer 




    
