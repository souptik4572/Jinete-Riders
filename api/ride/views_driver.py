from django.http import JsonResponse
from rest_framework.fields import NOT_READ_ONLY_REQUIRED
from .serializers import RideSerializer
from .models import Ride
from ..driver.models import Driver
from django.views.decorators.csrf import csrf_exempt
import json
from ..utils.ride_type_constants import ACCEPTED, CANCELLED, INITIATED, STARTED

@csrf_exempt
def get_all_past_rides_driver(request):
    if request.method == 'GET':
        try:
            past_rides = Ride.objects.filter(
                driver__id=request.session['user']['id'], ride_status__gt=STARTED)
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
def get_all_accepted_rides(request):
    if request.method == 'GET':
        try:
            accepted_rides = Ride.objects.filter(
                driver__id=request.session['user']['id'], ride_status=ACCEPTED)
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
def start_particular_ride(request, ride_id):
    if request.method == 'PATCH':
        ride = Ride.objects.get(
            driver__id=request.session['user']['id'], id=ride_id)
        if not ride:
            return JsonResponse({
                'success': False,
                'message': 'Ride with given id does not exist'
            }, status=404)
        if ride.ride_status != ACCEPTED:
            return JsonResponse({
                'success': False,
                'message': 'Ride with given id cannot be started as it is not accepted'
            }, status=404)
        ride.ride_status = STARTED
        ride.save()
        return JsonResponse({
            'success': True,
            'message': 'Successfully changed ride status to started',
            'ride': RideSerializer(ride).data
        })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PATCH request with ride id in the parameter'
        }, status=404)


@csrf_exempt
def get_particular_ride_driver(request, ride_id):
    if request.method == 'GET':
        ride = Ride.objects.filter(
            driver__id=request.session['user']['id'], id=ride_id).first()
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
def cancel_accepted_ride(request, ride_id):
    if request.method == 'PATCH':
        try:
            ride = Ride.objects.get(
                driver__id=request.session['user']['id'], id=ride_id)
            if ride.ride_status != ACCEPTED:
                return JsonResponse({
                    'success': False,
                    'message': 'Ride with given id is not accepted and cannot be cancelled'
                })
            ride.ride_status = INITIATED
            ride.driver = None
            ride.save()
            return JsonResponse({
                'success': True,
                'message': 'Successfully cancelled the ride',
                'ride': RideSerializer(ride).data
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PATCH request for cancelling accepted ride'
        })


@csrf_exempt
def accept_existing_ride(request, ride_id):
    if request.method == 'PATCH':
        try:
            ride = Ride.objects.get(id=ride_id)
            if ride.ride_status != INITIATED:
                return JsonResponse({
                    'success': False,
                    'message': 'Ride with given id cannot be accepted'
                })
            driver = Driver.objects.get(id=request.session['user']['id'])
            ride.ride_status = ACCEPTED
            ride.driver = driver
            ride.save()
            return JsonResponse({
                'success': True,
                'message': 'Successfully accepted the ride',
                'ride': RideSerializer(ride).data
            })
        except Ride.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Ride with given id does not exist'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a PATCH request for accepting the given ride'
        })


@csrf_exempt
def get_all_initiated_rides(request):
    if request.method == 'GET':
        try:
            initiated_rides = Ride.objects.filter(ride_status=INITIATED).all()
            return JsonResponse({
                'success': True,
                'message': 'All initiated rides',
                'rides': RideSerializer(initiated_rides, many=True).data
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only provide a GET request for all initiated rides'
        })
