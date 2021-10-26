from django.db import models
from ..driver.models import Driver
from ..passenger.models import Passenger
from ..utils.ride_type_constants import RIDE_STATUS_TYPES, INITIATED
# Create your models here.


class Ride(models.Model):
    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, related_name='driver', blank=True, null=True)
    passenger = models.ForeignKey(
        Passenger, on_delete=models.SET_NULL, related_name='passenger', blank=True, null=True)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    total_cost = models.IntegerField()
    estimated_time = models.IntegerField()  # in minutes
    driver_rating = models.IntegerField(default=0)
    passenger_rating = models.IntegerField(default=0)
    ride_status = models.IntegerField(
        choices=RIDE_STATUS_TYPES, default=INITIATED)

    def __str__(self):
        return f"{self.source} to {self.destination}"
