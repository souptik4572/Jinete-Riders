from django.urls import path
from .views import register_passenger, login_passenger, edit_passenger_data, request_password_reset, update_password

urlpatterns = [
    path('register/', register_passenger, name='api.register_passenger'),
    path('login/', login_passenger, name='api.login_passenger'),
    path('update-password/', update_password, name='api.update_password'),
    path('update-profile/', edit_passenger_data,
         name='acpi.edit_passenger_data'),
    path('request-password-reset/', request_password_reset,
         name='api.request_password_reset'),
]
