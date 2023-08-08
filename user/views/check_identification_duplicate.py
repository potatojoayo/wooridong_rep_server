from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist

from ..models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def check_identification_duplicate_view(request):
    try:
        user = User.objects.get(identification=request.data['identification'])
    except ObjectDoesNotExist:
        return Response(data={'duplicated': False})
    else:
        if user.is_active:
            return Response(data={'duplicated': True, 'is_active': True})
        else:
            return Response(data={'duplicated': True, 'is_active': False})
