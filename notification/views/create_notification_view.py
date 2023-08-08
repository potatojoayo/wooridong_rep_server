import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

import requests
from datetime import datetime

from notification.models.notification import Notification
from notification.serializers.notification_serializer import NotificationSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
def create_notification(request):
    data = request.body
   
    return Response(status=200)
