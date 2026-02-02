from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')


def get_weather_details(request):
        if request.method == "GET":
             
            city_name = request.GET.get('city')

            if not city_name:
                return render(request , 'index.html',{
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

            fetch_data ={
                    "city_name": data["name"],
                    "temperature" : data["main"]["temp"],
                    "humidity" : data["main"]["humidity"],
                    "condition" :data["weather"][0]["description"],
                    "wind_speed":data["wind"]["speed"]
                }

            return render(request, 'weather_report.html' , {
                    'fetch_data' : fetch_data
                })
        
        return render(request,'index.html')
            
        
        

        
    
         
    

    


    
        
        
    # error = "City name is required"

    # if not city_name:
    #     return response(request,'index.html',
    #         {"error":error},
    #         status=400
    #     )
    
    

    
    # return response(request,'weather_report.html',{'fetch_data':fetch_data})



