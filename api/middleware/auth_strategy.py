from django.http import JsonResponse
from ..passenger.models import Passenger
from ..passenger.serializers import PassengerSerializer
from ..driver.models import Driver
from ..driver.serializers import DriverSerializer
import jwt
from decouple import config

ACCESS_SECRET_TOKEN = config('ACCESS_SECRET_TOKEN')

auth_strategy_functions = {
    'edit_passenger_data', 'edit_driver_data', 'book_new_ride', 'get_all_upcoming_rides', 'get_particular_ride', 'rate_the_driver', 'get_all_accepted_rides', 'cancel_particular_ride', 'get_all_past_rides', 'get_all_initiated_rides', 'accept_existing_ride', 'cancel_accepted_ride', 'get_particular_ride_driver', 'start_particular_ride', 'get_all_accepted_rides_driver', 'get_all_past_rides_driver', 'complete_ride', 'rate_the_passenger'
}


class AuthStrategyMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__name__ in auth_strategy_functions:
            try:
                token = request.headers.get(
                    'Authorization', None).split(' ')[1]
                verified_user = jwt.decode(
                    token, ACCESS_SECRET_TOKEN, algorithms=['HS512'])
                if 'passenger' in request.path:
                    if verified_user['user_type'] == 'driver':
                        return JsonResponse({
                            'success': False,
                            'message': 'Invalid token'
                        })
                    our_model = Passenger
                    our_serializer = PassengerSerializer
                elif 'driver' in request.path:
                    if verified_user['user_type'] == 'passenger':
                        return JsonResponse({
                            'success': False,
                            'message': 'Invalid token'
                        })
                    our_model = Driver
                    our_serializer = DriverSerializer
                else:
                    return JsonResponse({
                        'success': False,
                        'message': 'Such a route does not exist'
                    }, status=404)
                request.session['user'] = our_serializer(
                    our_model.objects.get(pk=verified_user['id'])).data
            except jwt.InvalidTokenError:
                return JsonResponse({
                    'success': False,
                    'message': 'Token is invalid or expired'
                })
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': str(e)
                }, status=404)
        else:
            request.session['user'] = None
        return view_func(request, *view_args, **view_kwargs)
