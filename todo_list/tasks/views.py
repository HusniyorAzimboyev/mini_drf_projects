from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication

class DefaultPagination(PageNumberPagination):
    page_size = 5

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = DefaultPagination

    permission_classes = [IsAuthenticated]
