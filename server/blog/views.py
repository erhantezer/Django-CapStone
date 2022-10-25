from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework import  generics, status
from .pagination import CustomLimitOffsetPagination
from .permissions import IsAdminUserOrReadOnly, IsPostOwnerOrReadOnly
from .serializers import BlogPostSerializer, CategorySerializer, CommentSerializer,LikeSerializer
from rest_framework.response import Response
from blog.models import (
    BlogPost, 
    Category, 
    Post_view, 
    Comment, 
    Like
)

#! model (db) deki bütün verileri queryset olarak al serializers te oluşturduğumuz db oluşturulan tablonun json veri tipindeki verileri serializer_class olarak al. bunları hem listele hemde oluşturma işlemi generics.ListCreateAPIView ile yap
# ListCreateAPIView(mixins.ListModelMixin,
                        # mixins.CreateModelMixin,
                        # GenericAPIView):
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]



class BlogPostView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = CustomLimitOffsetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = [IsPostOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Post_view.objects.get_or_create(user=request.user, post=instance)
        Post_view.objects.create(user=request.user, post=instance)
        return Response(serializer.data)



class CommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print(self.kwargs)
        slug = self.kwargs.get('slug')
        blog = get_object_or_404(BlogPost, slug=slug)
        user = self.request.user
        comments = Comment.objects.filter(post=blog, user=user)
        if comments.exists():
            raise ValidationError(
                "You can not add another comment, for this Post !")
        serializer.save(post=blog, user=user)


class LikeView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        user = request.data.get('user')
        post = request.data.get('post')
        serializer = self.get_serializer(data=request.data)
        exists_like = Like.objects.filter(user=user, post=post)
        serializer.is_valid(raise_exception=True)
        if exists_like:
            exists_like.delete()
        else:
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)