from rest_framework import routers
from django.urls import path, include
from .views import PassengerViewSet, register_passenger

router = routers.DefaultRouter()

router.register(r'', PassengerViewSet)

urlpatterns = [
    path('register/', register_passenger, name='api.register_passenger'),
    path('', include(router.urls))
]
