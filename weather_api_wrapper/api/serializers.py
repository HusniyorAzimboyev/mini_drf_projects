from rest_framework.serializers import ModelSerializer
from .models import Requests

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'