from django.http import JsonResponse
from .serializers import OrderSerializer
from ..ride.models import Ride
from .models import Order
from django.views.decorators.csrf import csrf_exempt
import json
import razorpay
from decouple import config
from ..utils.payment_status_constants import PAYMENT_STARTED, PAYMENT_COMPLETED
from ..utils.ride_type_constants import COMPLETED, PAID

RAZOR_KEY_ID = config('RAZOR_KEY_ID')
RAZOR_KEY_SECRET = config('RAZOR_KEY_SECRET')

# Creating our razorpay client
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

# Create your views here.


@csrf_exempt
def get_particular_order(request, order_id):
    if request.method == 'GET':
        try:
            order = Order.objects.get(
                ride__passenger__id=request.session['user']['id'], id=order_id)
            return JsonResponse({
                'success': True,
                'message': 'The particular order',
                'order': OrderSerializer(order).data
            }, status=200)
        except Order.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Order with given id does not exist'
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only send a GET request for getting particular order'
        }, status=404)


@csrf_exempt
def get_all_orders(request):
    if request.method == 'GET':
        try:
            orders = Order.objects.filter(
                ride__passenger__id=request.session['user']['id']).all()
            return JsonResponse({
                'success': True,
                'message': 'All the previous orders',
                'orders': OrderSerializer(orders, many=True).data
            }, status=200)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only send a GET request for getting all orders'
        }, status=404)


@csrf_exempt
def verify_payment_order(request, ride_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            ride = Ride.objects.get(id=ride_id)
            order = Order.objects.get(ride=ride)
            razorpay_payment_id = data['razorpay_payment_id']
            razorpay_signature = data['razorpay_signature']
            params_dict = {
                'razorpay_order_id': order.order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }
            result = client.utility.verify_payment_signature(
                params_dict)
            if result is None:
                try:
                    order.payment_id = razorpay_payment_id
                    order.signature = razorpay_signature
                    order.payment_status = PAYMENT_COMPLETED
                    order.save()
                    ride.ride_status = PAID
                    ride.save()
                    return JsonResponse({
                        'success': True,
                        'message': 'Successfully payment completed',
                        'order': OrderSerializer(order).data
                    }, status=201)
                except Exception as e:
                    return JsonResponse({
                        'success': False,
                        'message': 'Failed to capture payment',
                        'error': str(e)
                    }, status=404)
            return JsonResponse({
                'test': 'live'
            })
        except Ride.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Ride with given id does not exist'
            }, status=404)
        except Order.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Order for given ride does not exist. Please place new order'
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
            'message': 'Please only send a POST request for creating a new order with ride id in the parameter'
        }, status=404)


@csrf_exempt
def create_new_order(request, ride_id):
    if request.method == 'PUT':
        try:
            ride = Ride.objects.get(id=ride_id)
            if ride.ride_status != COMPLETED:
                return JsonResponse({
                    'success': False,
                    'message': 'Ride with given id is not completed, payment can only be done after completion of ride'
                }, status=404)
            razorpay_order = client.order.create(data={
                'amount': ride.total_cost * 100,
                'currency': 'INR',
                'payment_capture': 1
            })
            order = Order.objects.create(
                ride=ride, order_id=razorpay_order['id'], price=ride.total_cost)
            return JsonResponse({
                'success': True,
                'order_id': razorpay_order['id'],
                'price': ride.total_cost
            }, status=201)
        except Ride.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Ride with given id does not exist'
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=404)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Please only send a PUT request for creating a new order with ride id in the parameter'
        }, status=404)
