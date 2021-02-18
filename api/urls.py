from . import views
from .views import UserViewset
from .views import MessageViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', UserViewset)
router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include( router.urls)),
    path('<str:room_name>/', views.room, name='room'),
]
