from django.shortcuts import render
import requests
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def get_weather_details(request):
    city = request.GET.get("city")

    if not city:
        return JsonResponse(
            {"error":"City name is required"},
            status=400
        )
    
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={settings.WEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse(
            {"error":"City not found"},
            status = 404
        )
    
    data = response.json()

    fetch_data ={
        "city_name": data["name"],
        "temperature" : data["main"]["temp"],
        "humidity" : data["main"]["humidity"],
        "weather" :data["weather"][0]["icon"],
        "wind_speed":data["wind"]["speed"]
    }

    return JsonResponse(fetch_data)



