from rest_framework.serializers import ModelSerializer
from .models import Requests_data

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Requests_data
        fields = '__all__'