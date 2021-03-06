from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
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
    driver_rating = models.FloatField(
        default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    passenger_rating = models.FloatField(
        default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    ride_status = models.IntegerField(
        choices=RIDE_STATUS_TYPES, default=INITIATED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.source} to {self.destination}"
