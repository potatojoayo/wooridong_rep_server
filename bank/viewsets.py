from rest_framework import viewsets 
from .serializers import BankSerializer
from .models import Bank

class BankViewSet(viewsets.ModelViewSet):

    serializer_class = BankSerializer
    queryset = Bank.objects.all()
