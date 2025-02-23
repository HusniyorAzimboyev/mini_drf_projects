from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSer