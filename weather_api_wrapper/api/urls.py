from django.urls import path,include
from .views import WeatherInfo

urlpatterns = [
    path("current-weather/",WeatherInfo.as_view()),
]