from rest_framework import serializers
from .models import Order
from ..ride.serializers import RideSerializer


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    ride = RideSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'order_id', 'payment_id', 'signature',
                  'price', 'payment_status', 'ride')
