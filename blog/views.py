from rest_framework import viewsets
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
