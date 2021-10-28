from django.db import models
from ..ride.models import Ride
from ..utils.payment_status_constants import PAYMENT_STATUS_TYPES, PAYMENT_STARTED

# Create your models here.


class Order(models.Model):
    ride = models.ForeignKey(
        Ride, on_delete=models.SET_NULL, blank=True, null=True)
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField()
    payment_status = models.CharField(
        max_length=50, choices=PAYMENT_STATUS_TYPES, default=PAYMENT_STARTED)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ride.passenger.name)
