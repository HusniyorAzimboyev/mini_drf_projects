from rest_framework import views
from rest_framework.response import Response
from .models import Requests
from .serializers import RequestSerializer

class RequestView(views.APIView):
    def get(self, request):
        requests = Requests.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        request = request.data.get('request')
        response = request.data.get('response')
        request = Requests(request=request, response=response)
        request.save()
        serializer = RequestSerializer(request)
        return Response(serializer.data)