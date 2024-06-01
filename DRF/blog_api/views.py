from rest_framework import generics
from blog.models import Post, Category
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.published()
    serializer_class = PostSerializer
    
class PostDetail(generics.RetrieveDestroyAPIView):
    pass