# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.utils.datetime_safe import datetime

from .models import Message
from django.contrib.auth import get_user_model


User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(self)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        author = text_data_json['username']
        author_user = User.objects.filter(username = author) [0]
        print(text_data_json)
        message = text_data_json['message']

        Message.objects.create(
            author= author_user,
            content_message= message
        )
        now = datetime.now()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'content_message': message,
                'username': author,
                'timestamp': str(now)
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['content_message']
        username = event['username']
        timestamp = event['timestamp']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'content_message': message,
            'username': username,
            'timestamp': timestamp
        }))
