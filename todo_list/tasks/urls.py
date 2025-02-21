from django.urls import path,include
from .views import TaskViewSet,debug
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks',TaskViewSet)

urlpatterns = [
    path("api/",include(router.urls)),
    path('debug/',debug)
]