from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ..models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def check_phone_number_view(request):
    user = User.objects.get(identification=request.data['identification'])
    if user.phone_number == request.data['phone_number']:
        return Response(data={'correct': True})
    else:
        return Response(data={'correct': False})
