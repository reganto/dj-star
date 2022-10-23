from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView

from .models import Post, Rating
from .serializers import PostSerializer, RatingSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRatingView(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
