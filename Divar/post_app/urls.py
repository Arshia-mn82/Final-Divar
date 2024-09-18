from django.urls import path
from .views import (
    PostList,
    PostDetail,
    CommentListCreate,
    CommentModeration,
    FavoriteListCreate,
    ProfileDetail,
    UserRatingListCreate,
    UserRatingDetail,
    PostAnalytics,
    Login,
    Refresh,
)

urlpatterns = [
    path("posts/", PostList.as_view()),
    path("posts/<int:pk>/", PostDetail.as_view()),
    path("comments/", CommentListCreate.as_view()),
    path("comments/<int:pk>/moderate/", CommentModeration.as_view()),
    path("favorites/", FavoriteListCreate.as_view()),
    path("profile/", ProfileDetail.as_view()),
    path("ratings/", UserRatingListCreate.as_view()),
    path("ratings/<int:pk>/", UserRatingDetail.as_view()),
    path("analytics/", PostAnalytics.as_view()),
    path("login/" , Login.as_view()),
    path('refresh/' , Refresh.as_view()),
]
