from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from user.models import User


@api_view(['DELETE'])
def delete_user_view(request):
    user = request.user
    User.objects.filter(id=user.id).update(is_active=False)

    # user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
