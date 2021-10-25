from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=320, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=60)
    profile_image = models.CharField(max_length=256, blank=True, null=True)
    rating = models.FloatField(default=3)
    car_name = models.CharField(max_length=50)
    car_number = models.CharField(max_length=30)
    car_image = models.CharField(max_length=256)
    driving_license_no = models.CharField(max_length=15)

    def __str__(self):
        self.name


class Token(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    expiry_time = models.DateTimeField(
        default=(timezone.now() + timedelta(hours=1)))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.expiry_time
