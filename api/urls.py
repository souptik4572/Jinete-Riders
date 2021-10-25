from django.urls import path
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    path('passenger/', include('api.passenger.urls')),
    path('driver/', include('api.driver.urls')),
    # path('ride/', include('api.ride.urls'))
]
