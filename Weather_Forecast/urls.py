from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('weather_report/',get_weather_details,name="weather_report"),
    
]