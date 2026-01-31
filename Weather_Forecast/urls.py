from django.urls import path
from .views import *

urlpatterns = [
    path('weather/', get_weather_details , name="weather"),
]