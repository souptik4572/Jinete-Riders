from rest_framework import viewsets
from .serializers import PassengerSerializer
from .models import Passenger

# Create your views here.


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all().order_by('id')
    serializer_class = PassengerSerializer
