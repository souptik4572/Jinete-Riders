from django.db.models import Q
from django.http import JsonResponse
from .serializers import RideSerializer
from .models import Ride
from ..passenger.models import Passenger
from django.views.decorators.csrf import csrf_exempt
import json
from ..utils.ride_type_constants import ACCEPTED, CANCELLED


# Create your views here.

@csrf_exempt
def get_all_upcoming_rides(request):
    if request.method == 'GET':
        try:
            upcoming_rides = Ride.objects.filter(
                passenger__id=request.session['user']['id'], ride_status__lte=ACCEPTED)
            return JsonResponse({
                'success': True,
                'message': 'All the incoming rides',
                'rides': RideSerializer(upcoming_rides, many=True).data
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a GET request'
        }, status=404)


@csrf_exempt
def get_all_past_rides(request):
    if request.method == 'GET':
        past_rides = Ride.objects.filter()
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a GET request'
        }, status=404)


@csrf_exempt
def book_new_ride(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            source = data['source']
            destination = data['destination']
            total_cost = data['total_cost']
            estimated_time = data['estimated_time']
            passenger = Passenger.objects.get(pk=request.session['user']['id'])
            ride = Ride.objects.create(source=source, destination=destination,
                                       total_cost=total_cost, estimated_time=estimated_time, passenger=passenger)
            return JsonResponse({
                'success': True,
                'message': 'Succesfully booked new ride',
                'passenger': RideSerializer(ride).data
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
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PUT for booking new ride with required data'
        }, status=404)
