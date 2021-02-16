from django.urls import path
from .views import UserViewset
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', UserViewset)

urlpatterns = [
    path('', include( router.urls)),
]
