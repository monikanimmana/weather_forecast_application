from django.shortcuts import render
import requests
from django.conf import settings
from datetime  import datetime

# Create your views here

def get_weather_details(request):
             
            city_name = request.GET.get('city')

            bg_image = "https://images.pexels.com/photos/186980/pexels-photo-186980.jpeg"

            if not city_name:
                return render(request , 'weather_report.html',{
                    "error":"City name does not exist",
                    "bg_image": bg_image,
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
            if "rain" in data:
                rain = data["rain"].get("1h", data["rain"].get("3h",0))


            fetch_data ={
                    "city_name": data["name"],
                    "temperature" : data["main"]["temp"],
                    "humidity" : data["main"]["humidity"],
                    "condition" :data["weather"][0]["description"],
                    "wind_speed":data["wind"]["speed"],
                   "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p"),
                    "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p"),
                    "visibility":data.get("visibility",0)/1000,
                    "rain":rain,

                }
            
# ===================== UNSPLASH API =====================================
            unsplash_url = "https://api.unsplash.com/search/photos"

            params = {
                  "query" : f"{city_name} city skyline",
                  "per_page" : 1
            }

            headers = {
                  "Authorization" : f"Client-ID {settings.UNSPLASH_API_KEY}"
            }

            unsplash_response = requests.get(unsplash_url,params=params,headers=headers).json()

            if unsplash_response.get("results"):
                  bg_image = unsplash_response["results"][0]["urls"]["regular"]

            fetch_data["bg_image"] = bg_image

            return render(request, 'weather_report.html' ,fetch_data)
        
        # return render(request,'weather_report.html')
              
        



