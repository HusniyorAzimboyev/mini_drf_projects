from rest_framework import viewsets
from .models import Author,Post
from .serializers import AuthorSer,PostSer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSer
    pagination_class = CustomPagination

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','body']