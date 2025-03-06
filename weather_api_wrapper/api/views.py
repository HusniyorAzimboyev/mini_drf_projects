from rest_framework import views, decorators
from rest_framework.response import Response
from .services import get_weather
from .models import Requests_data

class Current_celcius(views.APIView):
    def post(self, request):
        city = request.data.get("city")
        response = get_weather(city=city)

        Requests_data.objects.create(request=request.path,response=response[0],data_from_api=response[1])

        return Response(response[0])
    def get(self,request):
        return Response({"Error":f"Please send POST request and provide your city in it or make get request to {request.build_absolute_uri()}<city_name>"})
@decorators.api_view(http_method_names=["get"])
def get_current_celsius_info(request,city):
    city = city
    response = get_weather(city=city)

    Requests_data.objects.create(request=request.path,response=response[0],data_from_api=response[1])

    return Response(response[0])

