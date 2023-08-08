from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from utils.pagination import StandardResultsSetPagination
from ..models import Notification
from ..serializers import NotificationSerializer, NotificationWriteSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created')

    def get_serializer_class(self):
        if self.action == 'create':
            return NotificationWriteSerializer
        return NotificationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = NotificationSerializer
