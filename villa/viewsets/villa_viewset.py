from rest_framework import viewsets

from ..models import Villa
from ..serializers import VillaSerializer, VillaCreateSerializer, VillaUpdateSerializer

from django.core.exceptions import ObjectDoesNotExist


class VillaViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Villa.objects.filter(rep=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return VillaCreateSerializer
        if self.request.method == 'PATCH':
            return VillaUpdateSerializer
        return VillaSerializer

    def perform_create(self, serializer):
        villa = serializer.save(rep=self.request.user)
        return villa
