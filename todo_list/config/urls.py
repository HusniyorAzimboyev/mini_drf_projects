from django.contrib import admin
from django.urls import path,include
from django.urls import path, re_path
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        security_definitions = super().get_security_definitions()
        security_definitions['Bearer'] = {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
        return security_definitions
schema_view = get_schema_view(
    openapi.Info(
        title="ToDo List API",
        default_version='v1',
        description="Tasks crud function",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="husniyor09@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=JWTSchemaGenerator
)



urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("auth/",include("djoser.urls")),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get access & refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh expired access token

    path('admin/', admin.site.urls),
    path('',include("tasks.urls")),
]
