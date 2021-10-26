from django.urls import path
from .views import book_new_ride, get_all_upcoming_rides, get_particular_ride, get_all_accepted_rides, cancel_particular_ride, get_all_past_rides

urlpatterns = [
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
]
