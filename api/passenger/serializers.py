from rest_framework import serializers
from .models import Passenger


class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passenger
        fields = ('id', 'name', 'email', 'phone',
                  'city', 'country', 'profile_image', 'rating')
