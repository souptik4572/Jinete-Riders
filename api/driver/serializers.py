from rest_framework import serializers
from .models import Driver


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'name', 'email', 'phone',
                  'city', 'country', 'profile_image', 'rating', 'car_name', 'car_number', 'car_image', 'driving_license_no')
