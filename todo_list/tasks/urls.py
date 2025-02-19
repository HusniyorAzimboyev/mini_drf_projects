from django.urls import path,include
from .views import TaskAPIView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'task',Task)

urlpatterns = [
    path("task/",TaskAPIView.as_view())
]