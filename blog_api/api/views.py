from rest_framework import viewsets
from .models import Author,Post
from .serializers import AuthorSer,PostSer
from django_filters.rest_framework import DjangoFilterBackend

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSer
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSer
    
    filter_backends = [DjangoFilterBackend]
    lookup_fields = ['tags']
    filterset_fields = ['author']