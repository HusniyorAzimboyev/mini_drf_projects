from rest_framework import views, decorators
from rest_framework.response import Response
from .services import get_weather
from .models import Requests_data
from .serializers import RequestSerializer
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ValidationError

class CustomPagination(PageNumberPagination):
    page_size = 5

class Current_celcius(views.APIView):
    def post(self, request):
        city = request.data.get("city")
        response = get_weather(city=city)

        Requests_data.objects.create(request=request.path,response=response[0],data_from_api=response[1])

        return Response(response[0])
    def get(self,request):
        return Response({"message":f"Please send POST request and provide your city in your data or make get request to {request.build_absolute_uri()}<city_name>"})
@decorators.api_view(http_method_names=["get"])
def get_current_celsius_info(request,city):
    city = city
    response = get_weather(city=city)

    Requests_data.objects.create(request=request.path,response=response[0],data_from_api=response[1])

    return Response(response[0])

class RequestHistory(views.APIView):
    pagination_class = CustomPagination
    def get(self,request):
        # if ValidationError:
        #     print(Requests_data.objects.all()[0])
        #     return Response({"error":"Some data is not valid."},status=400)
        queryset = Requests_data.objects.all()
        serializer = RequestSerializer(data=queryset,many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response({"message":"Something went wrong("})