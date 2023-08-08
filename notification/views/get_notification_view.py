import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import datetime

from notification.models.notification import Notification
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
def get_notification(request):
    data = json.loads(request.body)
    print(data)
    message_type = data['message_type']
    target_type = data['target_type']
    now = datetime.now()
    start_day = datetime(now.year, now.month, 1, 0, 0, 0)

    notification = Notification.objects.filter(user=request.user, notification_type=message_type,
                                               target_type=target_type,
                                               created__range=(start_day, now)).order_by('-created')[:1]

    date_data = ''
    if notification.__len__() > 0:
        date_data = notification[0].date_created

    return Response(status=200, data={'date': date_data})
