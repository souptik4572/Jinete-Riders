from django.urls import path
from .views import book_new_ride

urlpatterns = [
    path('passenger/new/', book_new_ride, name='api.book_new_ride')
]