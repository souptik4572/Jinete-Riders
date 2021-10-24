from django.urls import path
from .views import register_passenger, login_passenger

urlpatterns = [
    path('register/', register_passenger, name='api.register_passenger'),
    path('login/', login_passenger, name='api.login_passenger'),
]
