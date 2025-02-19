from .models import Task
from .serializers import TaskSerializer
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class DefaultPagination(PageNumberPagination):
    page_size = 5

class TaskAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Task.objects.all()
        serilizer = TaskSerializer(data,many=True)
        return Response(serilizer.data)
    def post(self,request):
        data = request.data.copy()
        data["user"] = request.user.id

        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)