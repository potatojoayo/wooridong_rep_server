import os

from celery import Celery
from firebase_admin import messaging
from rest_framework.utils import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
import django

django.setup()

from chat.serializers.chat_message_member_serializers import ChatMessageMemberSerializer
from chat.models import ChatMessageMember, Room, Member, ChatMessage
from user.models import User

app = Celery("tasks")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task
def send_to_token(fcm_token, title, body, url, chat_message_member_json):
    if fcm_token is None or fcm_token == '':
        return

    # See documentation on defining a message payload.
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        data={
            'url': url,
            'push_type': 'chat',
            'chat_message_member': chat_message_member_json,
        },
        token=fcm_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)


@app.task
def save_message_to_all_member(identification, room_name, chat_message_id):
    user = User.objects.get(identification=identification)
    room = Room.objects.get(name=room_name)
    members = Member.objects.filter(room=room)
    sender = Member.objects.filter(room=room, user=user).get()
    for member in members:
        ChatMessageMember(message_id=chat_message_id, room=room, member=member,
                          sender=sender).save()


@app.task
def send_notification(identification, room_name, message):
    user = User.objects.get(identification=identification)
    chat_message = ChatMessage.objects.create(text=message)
    room = Room.objects.get(name=room_name)
    members = Member.objects.filter(room=room)
    sender = Member.objects.filter(room=room, user=user).get()
    for member in members:
        # send notification
        chat_message_member_json = json.dumps(ChatMessageMemberSerializer(
            ChatMessageMember.objects.filter(message=chat_message, room=room, member=member,
                                             sender=sender).first()).data)
        send_to_token(member.user.fcm_token, 'chat', message, '/chat/chatting',
                      chat_message_member_json)


@app.task
def unread_to_read_message(identification, room_name, chat_message_pk):
    user = User.objects.get(identification=identification)
    room = Room.objects.get(name=room_name)
    member = Member.objects.get(room=room, user=user)

    if chat_message_pk is not None:
        chat_message = ChatMessage.objects.get(pk=chat_message_pk)
        ChatMessageMember.objects.filter(member=member, message=chat_message, room=room,
                                         unread=True).update(unread=False)
    else:
        ChatMessageMember.objects.filter(member=member, room=room, unread=True).update(
            unread=False)
