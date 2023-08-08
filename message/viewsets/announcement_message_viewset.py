from rest_framework import viewsets
from ..models import AnnouncementMessage
from ..serializers import AnnouncementMessageSerializer


class AnnouncementMessageViewSet(viewsets.ModelViewSet):
    queryset = AnnouncementMessage.objects.all()
    serializer_class = AnnouncementMessageSerializer

    def perform_create(self, serializer):
        serializer.save(rep=self.request.user)
