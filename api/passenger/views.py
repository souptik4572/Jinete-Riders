from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import PassengerSerializer
from .models import Passenger
from django.views.decorators.csrf import csrf_exempt
import json
import bcrypt
import jwt
from decouple import config
from datetime import datetime, timedelta

ACCESS_SECRET_TOKEN = config('ACCESS_SECRET_TOKEN')
BCRYPT_SALT = int(config('BCRYPT_SALT'))


def are_passwords_matching(given_password, actual_password):
    return bcrypt.checkpw(given_password.encode('utf-8'), actual_password.encode('utf-8'))

# Create your views here.

@csrf_exempt
def edit_passenger_data(request):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        try:
            passenger = Passenger.objects.get(pk=request.session['user']['id'])
            if 'name' in data:
                passenger.name = data['name']
            if 'email' in data:
                passenger.email = data['email']
            if 'phone' in data:
                passenger.phone = data['phone']
            if 'city' in data:
                passenger.city = data['city']
            if 'country' in data:
                passenger.country = data['country']
            if 'profile_image' in data:
                passenger.profile_image = data['profile_image']
            passenger.save()
            return JsonResponse({
                'success': True,
                'message': 'Profile has been updated successfully',
                'passenger': PassengerSerializer(passenger).data
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PATCH request for passenger data updation'
        })


@csrf_exempt
def login_passenger(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            email = data['email']
            password = data['password']
            if not Passenger.objects.filter(email=email).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Passenger with given email does not exist'
                })
            passenger = Passenger.objects.get(email=email)
            if not are_passwords_matching(password, passenger.password):
                return JsonResponse({
                    'success': False,
                    'message': 'Passwords does not match'
                })
            encoded_token = jwt.encode({
                'id': passenger.id,
                'user_type': 'passenger',
                'exp': datetime.now() + timedelta(days=1)
            }, ACCESS_SECRET_TOKEN, algorithm='HS512')
            return JsonResponse({
                'success': True,
                'message': 'Successfully logged in',
                'token': encoded_token
            })
        except KeyError:
            return JsonResponse({
                'success': False,
                'message': 'Please provide both email and password for logging in'
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a POST request for login with necessary data'
        })


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
            if Passenger.objects.filter(email=email).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Passenger already exists'
                })
            hashed_password = str(bcrypt.hashpw(
                password.encode('utf-8'), bcrypt.gensalt(BCRYPT_SALT))).replace("b'", "").replace("'", "")
            try:
                passenger = Passenger.objects.create(
                    name=name, email=email, phone=phone, password=hashed_password, city=city, country=country, profile_image=profile_image)
                return JsonResponse({
                    'success': True,
                    'message': 'Succesfully created passenger',
                    'passenger': PassengerSerializer(passenger).data
                })
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': str(e)
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
