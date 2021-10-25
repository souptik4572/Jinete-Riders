from django.urls import path
from .views import register_driver, login_driver, edit_driver_data, request_password_reset, update_password

urlpatterns = [
    path('register/', register_driver, name='api.register_driver'),
    path('login/', login_driver, name='api.login_driver'),
    path('update-password/', update_password, name='api.update_password'),
    path('update-profile/', edit_driver_data,
         name='api.edit_driver_data'),
    path('request-password-reset/', request_password_reset,
         name='api.request_password_reset'),
]
