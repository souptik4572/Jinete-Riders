from django.urls import path
from .views import register_passenger, login_passenger, edit_passenger_data

urlpatterns = [
    path('register/', register_passenger, name='api.register_passenger'),
    path('login/', login_passenger, name='api.login_passenger'),
    path('update-profile/', edit_passenger_data, name='api.edit_passenger_data'),
]
