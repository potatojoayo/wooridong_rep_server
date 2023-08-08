from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from ..models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def change_password_view(request):
    user = User.objects.get(identification=request.data.get('identification'))
    password = request.data.get('password')
    user.set_password(password)
    user.save()
    return Response(status=status.HTTP_200_OK)
