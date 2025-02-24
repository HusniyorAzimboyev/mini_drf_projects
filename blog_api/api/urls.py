from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet,PostViewSet

router = routers.DefaultRouter()
router.register(r"author",AuthorViewSet)
router.register(r"post",PostViewSet,basename="post")

urlpatterns = [
    path("",include(router.urls))
]