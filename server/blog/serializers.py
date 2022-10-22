from unicodedata import category
from rest_framework import serializers
from .models import (
    Category,
    Post,
    Comment,
    Like,
    PostView
)



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields =(
            "id",
            "name"
        )

class PostSerializers(serializers.ModelSerializer):
    comment_post = CommentSerializers(many=True, read_only=True)
    like_post = LikeSerializers(many=True, read_only=True)
    view_user = PostSerializers(many=True, read_only=True)
    # category = serializers.StringRelatedField()
    # category_id = serializers.IntegerField()
    author = serializers.StringRelatedField()
    author_id = serializers.IntegerField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    post_view_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "author",
            "author_id",
            # "category_id",
            "category",
            "content",
            "image",
            "published_date",
            "last_updated",
            "status",
            # "slug",
            "like_count",
            "comment_count",
            "post_view_count",
            "comment_post",
            "like_post",
        )
        read_only_fields = (
            "published_date",
            "updated_date",
            # "slug",
            "author",
            "author_id"
        )

    def get_like_count(self, obj):
        return Like.objects.filter(post=obj.id).count()

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj.id).count()

    def get_post_view_count(self, obj):
        return Post.objects.filter(post=obj.id).count()


class CommentSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField()
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = "__all__"


class LikeSerializers(serializers.ModelSerializer):
    # like_user = AllUserSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "user_id",
            "post",
            # "like_user"
        )
        
class PostViewSerializers(serializers.ModelSerializer):
    # like_user = AllUserSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField()

    class Meta:
        model = PostView
        fields = "__all__"
          











# ! Object-level validation  

#   """
#   SerializerMethodField() methodu kullandık, bu method, modelden gelen tabloya serializers işlemi uygularken ek olarak veri eklemek için kullanılıyor
#   """

#! Field-level validation
#   def validate_task(self,value):
#     if value.lower() =="angular" and  value.lower() =="vue" :
#         raise serializers.ValidationError("angular and value can not be our blogapp")

#! Category içerisindeki tüm postlara ulaşmak için related name =categorys için categorys=PostSerializers(many=True) # tüm postları getirebiliriz

#! timezone
# Postun yayınlanma süresini from django.utils.timezone import  ederek days=serializers.SerializerMethodField() kullanarak
#  def get_days(self,obj):
# return (now() - obj.publishdate).days ile bulabiliriz.

#! StringRelatedField()
# category=serializers.StringRelatedField()
  # 🍵 buradaki category post modelindeki filed default id, biz __str__ methodundaki veriyi böylece çağırdık artık field category_name olarak gelir.