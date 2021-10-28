from django.urls import path
from .views import create_new_order, verify_payment_order, get_all_orders, get_particular_order

urlpatterns = [
    path('<int:order_id>/', get_particular_order,
         name='api.get_particular_order'),
    path('all/', get_all_orders, name='api.get_all_orders'),
    path('<int:ride_id>/create-order/',
         create_new_order, name='api.create_new_order'),
    path('<int:ride_id>/verify-order/', verify_payment_order,
         name='api.verify_payment_order'),
]
