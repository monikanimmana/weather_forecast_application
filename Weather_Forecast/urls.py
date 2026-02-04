from django.urls import path
from .views import *

urlpatterns = [
    path('',get_weather_details,name="weather"),
    
]