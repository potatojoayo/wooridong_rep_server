from rest_framework import viewsets
from ..models import User
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'identification'
    serializer_class = UserSerializer
    lookup_value_regex = "[^/]+"

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)
