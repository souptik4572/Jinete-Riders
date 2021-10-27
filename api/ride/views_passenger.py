from django.db.models import Avg
from django.http import JsonResponse
from .serializers import RideSerializer
from .models import Ride
from ..passenger.models import Passenger
from django.views.decorators.csrf import csrf_exempt
import json
from ..utils.ride_type_constants import ACCEPTED, CANCELLED, STARTED, COMPLETED

# Create your views here.


@csrf_exempt
def rate_the_driver(request, ride_id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        try:
            ride = Ride.objects.get(
                passenger__id=request.session['user']['id'], id=ride_id, ride_status__gte=COMPLETED)
            ride.driver_rating = data['rating']
            ride.save()
            driver = ride.driver
            driver.rating = Ride.objects.filter(
                driver__id=driver.id, ride_status__gte=COMPLETED).aggregate(rating=Avg('driver_rating'))['rating']
            driver.save()
            return JsonResponse({
                'success': True,
                'message': 'Successfully submitted rating',
            })
        except Ride.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Ride with given id does not exist'
            })
        except KeyError:
            return JsonResponse({
                'success': False,
                'message': 'Please provide all the fields'
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PATCH request with ride id in the parameter'
        }, status=404)


@csrf_exempt
def cancel_particular_ride(request, ride_id):
    if request.method == 'DELETE':
        ride = Ride.objects.filter(
            passenger__id=request.session['user']['id'], id=ride_id).first()
        if not ride:
            return JsonResponse({
                'success': False,
                'message': 'Ride with given id does not exist'
            }, status=404)
        ride.ride_status = CANCELLED
        ride.save()
        return JsonResponse({
            'success': True,
            'message': 'Details of ride having given id',
            'ride': RideSerializer(ride).data
        })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a DELETE request with ride id in the parameter'
        }, status=404)


@csrf_exempt
def get_particular_ride(request, ride_id):
    if request.method == 'GET':
        ride = Ride.objects.filter(
            passenger__id=request.session['user']['id'], id=ride_id).first()
        if not ride:
            return JsonResponse({
                'success': False,
                'message': 'Ride with given id does not exist'
            }, status=404)
        return JsonResponse({
            'success': True,
            'message': 'Details of ride having given id',
            'ride': RideSerializer(ride).data
        })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a GET request with ride id in the parameter'
        }, status=404)


@csrf_exempt
def get_all_accepted_rides(request):
    if request.method == 'GET':
        try:
            accepted_rides = Ride.objects.filter(
                passenger__id=request.session['user']['id'], ride_status=ACCEPTED)
            return JsonResponse({
                'success': True,
                'message': 'All the accepted rides',
                'rides': RideSerializer(accepted_rides, many=True).data
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
def get_all_upcoming_rides(request):
    if request.method == 'GET':
        try:
            upcoming_rides = Ride.objects.filter(
                passenger__id=request.session['user']['id'], ride_status__lte=ACCEPTED)
            return JsonResponse({
                'success': True,
                'message': 'All the upcoming rides',
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
        try:
            past_rides = Ride.objects.filter(
                passenger__id=request.session['user']['id'], ride_status__gt=STARTED)
            return JsonResponse({
                'success': True,
                'message': 'All the past rides',
                'rides': RideSerializer(past_rides, many=True).data
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
