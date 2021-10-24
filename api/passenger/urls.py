from rest_framework import routers
from django.urls import path, include
from .views import PassengerViewSet

router = routers.DefaultRouter()

router.register(r'', PassengerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
