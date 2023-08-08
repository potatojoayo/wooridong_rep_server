from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import NotificationViewSet
from .views import get_notification_view

router = DefaultRouter()
router.register('', NotificationViewSet, 'notification')

urlpatterns = [
    path('get_one/', get_notification_view.get_notification, name='get_notification_view'),
    path('', include(router.urls)),
]
