from . import views
from .views import UserViewset
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', UserViewset)

urlpatterns = [
    path('', include( router.urls)),
    path('<str:room_name>/', views.room, name='room'),
]
