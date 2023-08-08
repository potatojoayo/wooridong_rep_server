from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_user_view(request):
    user = request.user
    return Response(data={'identification': user.identification, 'name': user.name, 'phone_number': user.phone_number,
                          'id': user.id, 'is_active': user.is_active,
                          })
