from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view

class DefaultPagination(PageNumberPagination):
    page_size = 5

class TaskViewSet(viewsets.ModelViewSet):
    # authentication_classes = ["rest_framework_simplejwt.authentication.JWTAuthentication"]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = DefaultPagination

    permission_classes = [IsAuthenticated]

@api_view(http_method_names=["get"])
def debug(request):
    print("Authorization Header:", request.headers.get("Authorization"))  # Debugging
    return Response({"message": "Check the server logs for authorization headers!"})