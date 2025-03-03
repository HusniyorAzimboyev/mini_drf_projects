from rest_framework import views
from rest_framework.response import Response
from .services import get_weather

class WeatherInfo(views.APIView):
    def post(self, request):
        city = request.data.get("city")
        current = get_weather(city=city)
        return Response({"current_temp":f'{current}'})
    def get(self,request):
        return Response({"message":"Please send POST request and provide your city in it"})