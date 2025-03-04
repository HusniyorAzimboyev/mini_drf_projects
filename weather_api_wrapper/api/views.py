from rest_framework import views, decorators
from rest_framework.response import Response
from .services import get_weather
from .models import Requests_data

class WeatherInfo(views.APIView):
    def post(self, request):
        city = request.data.get("city")
        current = get_weather(city=city)
        response = {"current_temp":f'{current}'}

        Requests_data.objects.create(request=request.path,response=response)

        return Response(response)
    def get(self,request):
        return Response({"Error":f"Please send POST request and provide your city in it or make get request to {request.build_absolute_uri()}<city_name>"})
@decorators.api_view(http_method_names=["get"])
def get_weather_info(request,city):
    city = city
    current = get_weather(city=city)
    response = {"current_temp":f'{current}'}

    Requests_data.objects.create(request=request.path,response=response)

    return Response(response)