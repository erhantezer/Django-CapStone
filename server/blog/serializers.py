from rest_framework import serializers
from blog.models import BlogPost, Category, Comment, Like, Post_view
from django.contrib.auth import get_user_model
from django.utils.timezone import now
User = get_user_model()


###########? CATEGORY COMMENT VE LİKE YUKARDA TANIMLAMAMIZIN NEDENİ AŞAĞIDAKİ POST TA KULLANMAKTIR YUKARDA TANIMLAMAZSAK HATA ALIRIZ ########
#! Category model (tablo) içindeki id ve name Json yapısına çevirir queryset olarak döner key value şeklinde verileri json formatında görmüş oluruz
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )

#! Bu serializerde farklı olarak foreignkey(OneToMany) şeklinde aldığımız user ı id değilde string şeklinde göstermek için stringRealatedfield olarak aldık
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "time_stamp",
            "user",
        )
#! Bu serializerde foreignkey(OneToMany) şeklinde aldığımız user ı id değilde string şeklinde göstermek için stringRealatedfield olarak aldık db içindeki Like tablosu içinde id, user, user_id, post u aldık 
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "user_id",
            "post",
            
        )

#!
class BlogPostSerializer(serializers.ModelSerializer):
    comment_post = CommentSerializer(many=True, read_only=True)
    like_post = LikeSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField()
    author_id = serializers.IntegerField()
    like_count = serializers.SerializerMethodField()
    days = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    post_view_count = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    
    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "author",
            "author_id",
            "category",
            "content",
            "image",
            "published_date",
            "last_updated_date",
            "days",
            "status",
            "slug",
            "like_count",
            "comment_count",
            "post_view_count",
            "comment_post",
            "like_post",
            "category_id",
        )
        read_only_fields = (
            "published_date",
            "updated_date",
            "days",
            "slug",
            "author",
            "author_id"
        )

    def get_like_count(self, obj):
        return Like.objects.filter(post=obj.id).count()

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj.id).count()

    def get_post_view_count(self, obj):
        return Post_view.objects.filter(post=obj.id).count()

    def get_days(self,obj):
        return (now() - obj.publishdate).days






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