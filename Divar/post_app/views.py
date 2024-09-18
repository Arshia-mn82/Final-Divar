from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg
from .models import Post, Profile, Comment, Favorite, UserRating
from .serializers import PostSerializer, ProfileSerializer, CommentSerializer, FavoriteSerializer, UserRatingSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Post.objects.all()
        queryset = queryset.order_by('-is_nardeban', '-created_at')
        return queryset

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if 'is_sold' in request.data:
            instance.is_sold = request.data['is_sold']
            instance.save()
            return Response({'status': 'Post marked as sold'})
        return super().update(request, *args, **kwargs)

class CommentListCreate(ListCreateAPIView):
    queryset = Comment.objects.filter(status='approved')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentModeration(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'status' in request.data:
            instance.status = request.data['status']
            instance.save()
            return Response({'status': 'Comment status updated'})
        return super().update(request, *args, **kwargs)

class FavoriteListCreate(ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

class ProfileDetail(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class UserRatingListCreate(ListCreateAPIView):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    permission_classes = [IsAuthenticated]

class UserRatingDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    permission_classes = [IsAuthenticated]

class PostAnalytics(APIView):
    def get(self, request, format=None):
        post_count = Post.objects.count()
        average_price = Post.objects.aggregate(Avg('price'))['price__avg']
        response_data = {
            'post_count': post_count,
            'average_price': average_price,
        }
        return Response(response_data)
    
class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass
