from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Message

from .serializers import UserSerializer
from .serializers import MessageSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('id')

    serializer_class = MessageSerializer


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })