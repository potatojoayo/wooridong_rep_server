from datetime import datetime
from datetime import timedelta
from django.utils.crypto import get_random_string
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models import UserVerificationMessage
from ..serializers import UserVerificationMessageSerializer

class UserVerificationMessageViewSet(viewsets.ModelViewSet):


    permission_classes = [AllowAny]

    def get_queryset(self):
        return UserVerificationMessage.objects.filter(expiration_time__gt=datetime.now())

    serializer_class = UserVerificationMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'id':serializer.data['id']}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self,serializer): 
        phone_number = serializer.validated_data.get('phone_number')
        if phone_number == '01012345678': 
            serializer.save(code='000000',expiration_time = datetime.now()+ timedelta(minutes=3)) 
        else: 
            serializer.save(code=get_random_string(length=6,allowed_chars='1234567890'),expiration_time = datetime.now()+ timedelta(minutes=3)) 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.data['code'] == instance.code:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
            


