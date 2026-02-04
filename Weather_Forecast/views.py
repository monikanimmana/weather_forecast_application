from django.shortcuts import render
import requests
from django.conf import settings
from datetime  import datetime

# Create your views here

def get_weather_details(request):
        if request.method == "GET":
             
            city_name = request.GET.get('city')

            if not city_name:
                return render(request , 'weather_report.html',{
                    "error":"City name does not exist"
                })

            url = (
                f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.WEATHER_API_KEY}&units=metric"
            )

            response = requests.get(url)

            if response.status_code != 200:
                return render(request , 'weather_report.html', {
                     "error":" Please enter a vaild city name"
                })
            
        
            data = response.json()

            rain =0
            if rain in data:
                rain = data["rain"].get("1h", data["rain"].get("3h",0))


            fetch_data ={
                    "city_name": data["name"],
                    "temperature" : data["main"]["temp"],
                    "humidity" : data["main"]["humidity"],
                    "condition" :data["weather"][0]["description"],
                    "wind_speed":data["wind"]["speed"],
                    "sunrise":datetime.fromtimestamp(data["sys"]["sunrise"]),
                    "sunset":datetime.fromtimestamp(data["sys"]["sunset"]),
                    "visibility":data.get("visibility",0)/1000,
                    "rain":rain,

                }

            return render(request, 'weather_report.html' ,fetch_data)
        
        # return render(request,'weather_report.html')
              
        



