from rest_framework import serializers
from .models import Author

class AuthorSer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"