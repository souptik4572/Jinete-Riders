from rest_framework import serializers
from .models import Ride
from ..driver.serializers import DriverSerializer
from ..passenger.serializers import PassengerSerializer


class RideSerializer(serializers.HyperlinkedModelSerializer):
    driver = DriverSerializer(read_only=True)
    passenger = PassengerSerializer(read_only=True)

    class Meta:
        model = Ride
        fields = ('id', 'source', 'destination', 'estimated_time',
                  'driver_rating', 'passenger_rating', 'passenger', 'driver', 'ride_status')
