from django.urls import path
from .views import Current_celcius,get_current_celsius_info
from django.urls import path, re_path


urlpatterns = [
    path("current-celsius/",Current_celcius.as_view()),
    path("current-celsius/<city>",get_current_celsius_info),
]