from rest_framework import viewsets, generics
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


class BlogDeleteView(generics.DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
