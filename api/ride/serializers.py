from rest_framework import serializers
from .models import Ride


class RideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ride
        fields = ('id', 'source', 'destination', 'total_cost', 'estimated_time',
                  'driver_rating', 'passenger_rating', 'ride_status')
