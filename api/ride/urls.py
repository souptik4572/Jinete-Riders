from django.urls import path
from .views import book_new_ride, get_all_upcoming_rides, get_particular_ride, get_all_accepted_rides, cancel_particular_ride, get_all_past_rides
from .views_driver import get_all_initiated_rides, accept_existing_ride, cancel_accepted_ride, get_particular_ride_driver, start_particular_ride, get_all_accepted_rides, get_all_past_rides_driver, complete_ride

urlpatterns = [
    # All ride routes on side of passenger
    path('passenger/new/', book_new_ride, name='api.book_new_ride'),
    path('passenger/upcoming-rides/', get_all_upcoming_rides,
         name='api.get_all_upcoming_rides'),
    path('passenger/past-rides/', get_all_past_rides,
         name='api.get_all_past_rides'),
    path('passenger/accepted-rides/', get_all_accepted_rides,
         name='api.get_all_accepted_rides'),
    path('passenger/<int:ride_id>/', get_particular_ride,
         name='api.get_particular_ride'),
    path('passenger/<int:ride_id>/cancel/', cancel_particular_ride,
         name='api.cancel_particular_ride'),
    # All ride routes on side of driver
    path('driver/initiated-rides/', get_all_initiated_rides,
         name='api.get_all_initiated_rides'),
    path('driver/<int:ride_id>/accept/', accept_existing_ride,
         name='api.accept_existing_ride'),
    path('driver/<int:ride_id>/cancel/', cancel_accepted_ride,
         name='api.cancel_accepted_ride'),
    path('driver/<int:ride_id>/', get_particular_ride_driver,
         name='api.get_particular_ride_driver'),
    path('driver/<int:ride_id>/start/', start_particular_ride,
         name='api.start_particular_ride'),
    path('driver/accepted-rides/', get_all_accepted_rides,
         name='api.get_all_accepted_rides'),
    path('driver/past-rides/', get_all_past_rides_driver,
         name='api.get_all_past_rides_driver'),
     path('driver/<int:ride_id>/complete/', complete_ride,
         name='api.complete_ride'),
]
