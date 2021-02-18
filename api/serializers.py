from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user = user)
        return user

class MessageSerializer(serializers.ModelSerializer):
    username = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = Message

        fields = ('username', 'content_message', 'timestamp')
