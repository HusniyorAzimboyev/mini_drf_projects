from rest_framework import serializers
from .models import Author,Post

class AuthorSer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
class PostSer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
#just comment