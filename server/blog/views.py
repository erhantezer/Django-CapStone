from .models import (
    Category,
    Post,
    Comment,
    Like,
    PostView
)
from .serializers import (
    CategorySerializers,
    CommentSerializers,
    LikeSerializers,
    PostSerializers,
)
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError



class CategoryViews(generics.ListCreateAPIView):
    queryset=  Category.objects.all()
    serializer_class= CategorySerializers
    permission_classes = [IsAuthenticated]

    #! Login olmuş kullanıcıyı ekliyorum.
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated]
    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated]
    

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Post_view.objects.get_or_create(user=request.user, post=instance)
        PostView.objects.create(user=request.user, post=instance)
        return Response(serializer.data)


class CommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(self.kwargs)
        slug = self.kwargs.get('slug')
        blog = get_object_or_404(Post, slug=slug)
        user = self.request.user
        comments = Comment.objects.filter(blog=blog, user=user)
        if comments.exists():
             raise ValidationError("You can not add another comment, for this Post !")
        serializer.save(blog=blog, user=user)
        

class LikeView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializers

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