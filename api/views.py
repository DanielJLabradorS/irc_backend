from rest_framework import viewsets
from django.contrib.auth.models import User
from django.shortcuts import render

from .serializers import UserSerializer
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })