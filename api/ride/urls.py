from django.urls import path
from .views import book_new_ride, get_all_upcoming_rides

urlpatterns = [
    path('passenger/new/', book_new_ride, name='api.book_new_ride'),
    path('passenger/upcoming-rides/', get_all_upcoming_rides,
         name='api.get_all_upcoming_rides')
]
