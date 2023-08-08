from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .viewsets import BankViewSet

router = DefaultRouter()
router.register('',BankViewSet, basename='bank')

urlpatterns = [
    path('', include(router.urls))
]
