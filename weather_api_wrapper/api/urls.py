from django.urls import path,include
from .views import WeatherInfo,get_weather_info

urlpatterns = [
    path("current-weather/",WeatherInfo.as_view()),
    path("current-weather/<city>",get_weather_info),
]