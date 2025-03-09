from django.urls import path,include
from .views import Current_celcius,get_current_celsius_info, RequestHistoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"requests-history",RequestHistoryViewSet)

urlpatterns = [
    path("current-celsius/",Current_celcius.as_view()),
    path("current-celsius/<city>",get_current_celsius_info),
    path("",include(router.urls))
]