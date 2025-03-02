from rest_framework import viewsets,permissions,authentication,response,filters,pagination
from .models import Post
from .serializers import PostSer
from django_filters import rest_framework as django_filters
from functools import reduce
from operator import or_
from django.db.models import Q

class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
class PostFilter(django_filters.FilterSet):
    author = django_filters.NumberFilter(field_name='author__id')  
    published = django_filters.DateFromToRangeFilter()
    tags = django_filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Post
        fields = ["tags",'author', 'published']

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSer
    
    filter_backends = (filters.SearchFilter,django_filters.DjangoFilterBackend)
    filterset_class = PostFilter
    search_fields = ['title','body']

    def retrieve(self,request,*args,**kwargs):
        object = self.get_object()
        serializer = self.get_serializer(object)
        search_tags = object.tags.split(", ")
        print(f"database - {search_tags}")
        related_posts = Post.objects.filter(reduce(or_, [Q(tags__icontains=tag) for tag in search_tags])).exclude(id=object.id)
        return response.Response({
            "post":serializer.data,
            "related_posts":PostSer(related_posts,many=True).data
        })


