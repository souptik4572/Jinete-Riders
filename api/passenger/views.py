from django.http import JsonResponse
from .serializers import PassengerSerializer
from .models import Passenger, Token
from django.views.decorators.csrf import csrf_exempt
import json
import bcrypt
import jwt
from decouple import config
from datetime import datetime, timedelta
import os
import binascii
import pytz

utc=pytz.UTC

ACCESS_SECRET_TOKEN = config('ACCESS_SECRET_TOKEN')
BCRYPT_SALT = int(config('BCRYPT_SALT'))


def are_passwords_matching(given_password, actual_password):
    return bcrypt.checkpw(given_password.encode('utf-8'), actual_password.encode('utf-8'))

# Create your views here.

@csrf_exempt
def update_password(request):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        try:
            token = data['token']
            passenger_id = data['passenger_id']
            password = data['password']
            passenger = Passenger.objects.get(pk=passenger_id)
            password_reset_token = Token.objects.filter(
                passenger=passenger).first()
            if not password_reset_token:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid or expired password reset token'
                }, status=404)
            if utc.localize(datetime.now()) > password_reset_token.expiry_time:
                password_reset_token.delete()
                return JsonResponse({
                    'success': False,
                    'message': 'Expired password reset token'
                }, status=404)
            if not bcrypt.checkpw(token.encode('utf-8'), password_reset_token.token.encode('utf-8')):
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid or expired password reset token'
                }, status=404)
            hashed_password = str(bcrypt.hashpw(
                password.encode('utf-8'), bcrypt.gensalt(BCRYPT_SALT))).replace("b'", "").replace("'", "")
            passenger.password = hashed_password
            passenger.save()
            password_reset_token.delete()
            return JsonResponse({
                'success': True
            }, status=201)
        except Passenger.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Passenger with given id does not exist'
            }, status=404)
        except KeyError:
            return JsonResponse({
                'success': False,
                'message': 'Please provide all the fields'
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PATCH for password update with neccessary data'
        }, status=404)


@csrf_exempt
def request_password_reset(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            email = data['email']
            passenger = Passenger.objects.filter(email=email).first()
            if not passenger:
                return JsonResponse({
                    'success': False,
                    'message': 'Passenger with given email does not exist'
                }, status=404)
            token = Token.objects.filter(passenger_id=passenger.id).filter()
            if token:
                token.delete()
            reset_token = binascii.b2a_hex(os.urandom(8))
            hash = str(bcrypt.hashpw(reset_token, bcrypt.gensalt(
                BCRYPT_SALT))).replace("b'", "").replace("'", "")
            token = Token.objects.create(passenger=passenger, token=hash)
            return JsonResponse({
                'success': True,
                'passenger_id': PassengerSerializer(passenger).data['id'],
                'reset_token': str(reset_token).replace("b'", "").replace("'", "")
            }, status=200)
        except KeyError:
            return JsonResponse({
                'success': False,
                'message': 'Email data missing'
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a POST request for resetting password with email'
        }, status=404)


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
            }, status=201)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PATCH request for passenger data updation'
        }, status=404)


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
                }, status=404)
            passenger = Passenger.objects.get(email=email)
            if not are_passwords_matching(password, passenger.password):
                return JsonResponse({
                    'success': False,
                    'message': 'Passwords does not match'
                }, status=404)
            encoded_token = jwt.encode({
                'id': passenger.id,
                'user_type': 'passenger',
                'exp': datetime.now() + timedelta(days=1)
            }, ACCESS_SECRET_TOKEN, algorithm='HS512')
            return JsonResponse({
                'success': True,
                'message': 'Successfully logged in',
                'token': encoded_token
            }, status=200)
        except KeyError:
            return JsonResponse({
                'success': False,
                'message': 'Please provide both email and password for logging in'
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a POST request for login with necessary data'
        }, status=404)


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
                }, status=404)
            hashed_password = str(bcrypt.hashpw(
                password.encode('utf-8'), bcrypt.gensalt(BCRYPT_SALT))).replace("b'", "").replace("'", "")
            try:
                passenger = Passenger.objects.create(
                    name=name, email=email, phone=phone, password=hashed_password, city=city, country=country, profile_image=profile_image)
                return JsonResponse({
                    'success': True,
                    'message': 'Succesfully created passenger',
                    'passenger': PassengerSerializer(passenger).data
                }, status=201)
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': str(e)
                }, status=404)
        except KeyError:
            return JsonResponse({
                'success': False,
                'message': 'Some data missing'
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PUT request with necessary data'
        }, status=404)
