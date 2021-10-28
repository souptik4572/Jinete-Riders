from django.urls import path
from .views import create_new_order, verify_payment_order

urlpatterns = [
    path('<int:ride_id>/create-order/',
         create_new_order, name='api.create_new_order'),
    path('<int:ride_id>/verify-order/', verify_payment_order,
         name='api.verify_payment_order'),
]
