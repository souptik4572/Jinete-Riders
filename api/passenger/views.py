from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import PassengerSerializer
from .models import Passenger
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


@csrf_exempt
def register_passenger(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            name = data['name']
            email = data['email']
            phone = data['phone']
            password = data['password']
            city = data['city']
            country = data['country']
            profile_image = data['profile_image']
            print(data)
            return JsonResponse({
                'success': True
            })
        except KeyError:
            return JsonResponse({
                'success': False,
                'message': 'Some data missing'
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PUT request with necessary data'
        })


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all().order_by('id')
    serializer_class = PassengerSerializer
