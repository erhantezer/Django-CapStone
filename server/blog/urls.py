from .views import (
    CategoryView,
    BlogPostView,
    BlogPostDetailView,
    CommentView,
    LikeView,
    UserAllPosts
)
from django.urls import path
from rest_framework import routers


urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("like/", LikeView.as_view()),
    path("posts/", BlogPostView.as_view()),
    path("posts/<str:slug>/", BlogPostDetailView.as_view()),
    path("posts/<str:slug>/add_comment/", CommentView.as_view()),
    path("all-posts/", UserAllPosts.as_view()),

]


