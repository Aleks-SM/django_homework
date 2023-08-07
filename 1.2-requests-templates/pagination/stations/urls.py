from django.urls import path

from .views import index, get_bus_stations

urlpatterns = [
    path('', index, name='index'),
    path('bus_stations/', get_bus_stations, name='bus_stations'),
]
