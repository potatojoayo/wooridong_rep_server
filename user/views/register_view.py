from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response

from ..models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request: Request):

    data = request.data
    User.objects.create_user(**data) 
    return Response(status=status.HTTP_200_OK)
