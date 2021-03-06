from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
from uuid import uuid4

# Create your models here.


class Passenger(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=320, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=60)
    profile_image = models.CharField(max_length=256, blank=True, null=True)
    rating = models.FloatField(default=2.5, validators=[
                               MinValueValidator(0.0), MaxValueValidator(5.0)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Token(models.Model):
    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    expiry_time = models.DateTimeField(
        default=(timezone.now() + timedelta(hours=1)))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
