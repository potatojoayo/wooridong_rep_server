from datetime import datetime
from datetime import timedelta
from django.utils.crypto import get_random_string
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models import RepVerificationMessage
from ..serializers import RepVerificationMessageSerializer

class RepVerificationMessageViewSet(viewsets.ModelViewSet):

    queryset = RepVerificationMessage.objects.all()
    serializer_class = RepVerificationMessageSerializer 

    def perform_create(self,serializer): 
        serializer.save(rep=self.request.user) 
            


