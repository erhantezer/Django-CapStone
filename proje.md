#### CharField 255 karaktere kadar stringler için kullanılan alan tipidir. max_length argümanı tanımlanması zorunludur. max_length argümanı alanın alabileceği maksimum karakter sayısını belirler. Ürünümüz için isim alanı ekleylim. En fazla 200 karakter alabilsin.
<hr>
 <div style="color: red;">1. verbose_name :</div> alanın admin sayfasıi form gibi çıktılarda görüntülecek adıdır. Eğer girilmezse değişken kullanılır.
<hr>
<div style="color: red;">2. default : </div> argümanına girilen değer eğer alanın değeri boş ise veritabanına eklenecek olan varsayılan değerdir.
<hr>
<div style="color: red;">3. blank:</div> argümanının veritabanı alanı ile herhangi bir ilgisi yoktur. Form validasyonu için kullanılır. Eğer True ise forma boş değer girilmesi izin verir. Aksi taktirde değer girmeye zorlar.
<hr>
<div style="color: red;">4. null: </div> argümanı eğer True ise bu alan veritabanında boş değer alabilir. Aksi taktirde alana bir değer girilmesini zorunlu tutar.
<hr>
<div style="color: red;">5. unique: </div> argümanı eğer True ise alanın benzersiz olduğunu belirtir. O alan aynı değeri sadece bir kez alabilir.
<hr>
<div style="color: red;">6. editable: </div> argümanı eğer False seçilirse ilgili alan admin paneli ve formlarda görüntülenmez. Varsayılan değeri True’dur.
<hr>
<div style="color: red;">7. db_index: </div> argümanı index oluşturulması istenilen alanlar için True seçilir.
<hr>
<div style="color: red;">8. db_column: </div> argümanı ilgili alanın veritabanında kullanılacak ismini ayarlar. Eğer girilmez ise alan adi kullanılır. Hatırlarsanız
<hr>
<div style="color: red;">9. help_text: </div> argümanı alanın formlarda görüntülecek olan ilave yardım metnidir.
<hr>

### <div style="color: blue;">SlugField, Slug oluşturmak için kullanılan alan tipidir. harf, sayı, alt çizgi ve kısa çizgi alabilir. Genellikle url için kullanılır. max_length argümanı alır. max_length default 50 olarak ayarlanmıştır. db_index argümanı default olarak True ayarlanmıştır.</div>



# <center>  FULLSTACK-PROJECT-BLOG-APP  </center>

## <center> BACKEND </center>

# <center>  INITIAL SETUP </center>

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows 👇
python -m venv env
# linux / Mac OS 👇
vitualenv env

# ACTIVATING ENVIRONMENT
# windows 👇
source env/Scripts/activate
# linux / Mac OS 👇
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install djangorestframework
pip freeze > requirements.txt
django-admin startproject main .
# alternatively python -m pip install django
pip install python-decouple
django-admin --version
```

```bash
# 💨 If you already have a requirement.txt file, you can install the packages in the file
# 💨 by entering the following commands respectively in the terminal 👇
1-python -m venv env
2-source env/Scripts/activate
3-pip install -r requirements.txt 🚀
4-python.exe -m pip install --upgrade pip
5-python manage.py migrate
6-python manage.py createsuperuser
7-python manage.py runserver
```

## Secure your project

## .gitignore

✔ Add a ".gitignore" file at same level as env folder, and check that it includes ".env" and /env lines.

🔹 Do that before adding your files to staging area, else you will need extra work to unstage files to be able to ignore them.

🔹 [On this page](https://www.toptal.com/developers/gitignore) you can create "gitignore files" for your projects.

## Python Decouple

💻 To use python decouple in this project, first install it 👇

```bash
pip install python-decouple
```

💻 Go to terminal to update "requirements.txt"  👇

```bash
pip freeze > requirements.txt
```

✔ Create a new file and name as ".env" at same level as env folder

✔ Copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks and blanks from SECRET_KEY

```python
SECRET_KEY=-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!1^ui7j
```

✔ Go to "settings.py", make amendments below 👇

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')

```

## INSTALLING DJANGO REST

 Go to terminal 👇

```bash
python manage.py makemigrations
python manage.py migrate
pip install djangorestframework
```

✔ Go to "settings.py" and add 'rest_framework' app to INSTALLED_APPS

## PostgreSQL Setup

 To get Python working with Postgres, you will need to install the “psycopg2” module👇

```bash
pip install psycopg2
```

 Go to terminal to update requirements.txt  👇

```bash
pip freeze > requirements.txt
```

✔ Go to settings.py and add '' app to INSTALLED_APPS

##  Install Swagger

🔹 Explain a [sample API reference documentation](https://shopify.dev/api)

🔹 Swagger is an open source project launched by a startup in 2010. The goal is to implement a framework that will allow developers to document and design APIs, while maintaining synchronization with the code.

🔹 Developing an API requires orderly and understandable documentation.

🔹 To document and design APIs with Django rest framework we will use drf-yasg which generate real Swagger/Open-API 2.0 specifications from a Django Rest Framework API.

📜 You can find the documentation [here](https://drf-yasg.readthedocs.io/en/stable/readme.html).

###  Go to terminal for installation 👇

```bash
pip install drf-yasg
```

💻 Go to terminal to update requirements.txt  👇

```bash
pip freeze > requirements.txt
```

✔ Go to "settings.py" and add 'drf_yasg' app to INSTALLED_APPS

## ✔ Here is the updated "urls.py" file for swagger. In swagger documentation, those patterns are not up-to-date 👇

```python
from django.contrib import admin
from django.urls import path
# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Flight Reservation API",
        default_version="v1",
        description="Flight Reservation API project provides flight and reservation info",
        terms_of_service="#",
        contact=openapi.Contact(
            email="rafe@clarusway.com"),  # Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("admin/", admin.site.urls),
    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)",
         schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schemaredoc"),
]
```

##  MIGRATE 👇

```bash
python manage.py migrate
```

##  RUNSERVER 👇

```bash
python manage.py runserver
```

##  If you have this problem 👉 ( return Database.Cursor.execute(self, query, params) sqlite3.OperationalError:) when you create "superuser" you should write this command 👇

```bash
python manage.py migrate --run-syncdb
```

### ✔ After running the server, go to [swagger page](http://127.0.0.1:8000/swagger/) and [redoc page](http://localhost:8000/redoc/) of your project!

## INSTALL DEBUG TOOLBAR 👇

🔹 The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content.

📜 See the Django Debug Toolbar [documentation page](https://django-debug-toolbar.readthedocs.io/en/latest/).

##  For Installation go to terminal 👇

```bash
pip install django-debug-toolbar
```

 Go to terminal to update "requirements.txt"  👇

```bash
pip freeze > requirements.txt
```

✔ Go to "settings.py" and add 'debug_toolbar' app to INSTALLED_APPS

## Add django-debug-toolbar’s URLs to your project’s URLconf 👇

```python
from django.urls import include
urlpatterns = [
# ...
path('__debug__/', include('debug_toolbar.urls')),
]
```

## Add the middleware to the top 👇

```python
MIDDLEWARE = [
"debug_toolbar.middleware.DebugToolbarMiddleware",
# ...
]
```

## Add configuration of internal IPs to "settings.py" 👇

```python
INTERNAL_IPS = [
    "127.0.0.1",
]
```

## ADDING AN APP

💻 Go to terminal 👇

```bash
python manage.py startapp blog
```

✔ Go to "settings.py" and add 'blog' app to "INSTALLED_APPS"

## 💻 INSTALL [DJ-REST-AUTH](https://dj-rest-auth.readthedocs.io/en/latest/)

```bash
pip install dj-rest-auth
```

💻 Go to terminal to update "requirements.txt"  👇

```bash
pip freeze > requirements.txt
```

## Add "dj_rest_auth" app to "INSTALLED_APPS" in your django "base.py" 👇

```python
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
```

## Go to "main/urls.py" and add the path 👇

```python
path('auth/', include('user.urls'))
```

## ✔ Create "api" folder under "blog" App. 👉 Then create "urls.py", "serializers.py" and "views.py" files under "api" folder 👇

## Go to "users/urls.py" and add 👇

```python
from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]
```

##  Migrate your database

```bash
python manage.py migrate
```

## Start Models in "Blog" app 👇

```python
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    STATUS = (
        ("d", "DRAFT"),
        ("p", "PUBLISHED"),
    )
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name="post_user", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="post_category", on_delete=models.CASCADE)
    content = models.TextField()
    image = models.URLField(max_length=200, blank=True, default="https://robohash.org/9c681a48b0ef374675df3ca8d6b014a5?set=set4&bgset=&size=400x400")
    published_date = models.DateTimeField(auto_now_add=True, blank=True)
    last_updated_date = models.DateTimeField(auto_now=False, blank=True)
    status = models.CharField(max_length=50, choises=STATUS)
    #! We use slug for the fields we want to appear instead of ID 👇
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, related_name="like_user", on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, related_name="like_post", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, related_name="comment_user", on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, related_name="comment_post", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post_view(models.Model):
    user = models.ForeignKey(User, related_name="post_viewed_user", on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, related_name="viewed_post", on_delete=models.CASCADE)
    viewed_date_time = models.DateTimeField(auto_now_add=True, blank=True)
```

## Migrate your database 👇

```bash
python manage.py migrate
```

## Create "user" app and  add "INSTALLED_APP"

## Go to "models.py" in "user" app and add 👇

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.URLField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
```

## Register the model in "admin.py" 👇

```python
from django.contrib import admin
from .models import User

admin.site.register(User)
```

## Go "main/settings.py" and add 👇

```python
AUTH_USER_MODEL = 'user.User'
```

## Create "serializers.py" file under "user" app and add 👇

```python
from rest_framework import serializers, validators
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password1',
            'image',
            'bio'
        )
    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(
                {"password": "Password didn't match..... "}
            )
        return data
    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop('password1')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )
class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = (
            'key',
            'user'
        )
```

##  [SIGNALS](https://docs.djangoproject.com/en/4.1/topics/signals/) 👇

🔹 Django include  a “signal dispatcher” which helps decoupled applications get notified when actions occur elsewhere in the framework.

🔹 In   nutshell, signals allow certain senders to notify a set of receivers that some action has taken place.

🔹 They’re especially useful when many pieces of code may be interested in the same events.

##  Listening to signals 👉 Parameters:

🔹 <b>receiver</b>: The callback function which will be connected to this signal. See Receiver functions for more information.

🔹 <b>sender</b>: Specifies a particular sender to receive signals from. See Connecting to signals sent by specific senders for more information.

🔹 <b>weak</b>: Django stores signal handlers as weak references by default. Thus, if your receiver is a local function, it may be garbage collected. To prevent this, pass weak=False when you call the signal’s connect() method.

🔹 <b>dispatch_uid</b>: A unique identifier for a signal receiver in cases where duplicate signals may be sent. See Preventing duplicate signals for more information.

## Create "signals.py" file under "user" app and add 👇

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

## Go to "apps.py" and add this under UsersConfig() 👇

```python
def ready(self):
    import user.signals
```

## Go to "views.py" and create RegisterView() 👇

```python
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user)
            data['token'] = token.key
        else:
            data['error'] = 'User dont have token. Please login'
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
```

## Create "urls.py" file under "user" app and add 👇

```python
from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view())
]
```

## ✔ Create "serializers.py" file under "User" app and add 👇

```python
from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        required = True,
        write_only = True,
        validators = [validate_password],
        style = {"input_type":"password"}
    )
    password1 = serializers.CharField(
        required = True,
        write_only = True,
        validators = [validate_password],
        style = {"input_type":"password"}
    )
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password1",
        )
    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError(
                {"password": "Password must be same with above !..."}
            )
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password1")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
```

## Go to "user/api/views.py" and create RegisterView() 👇

```python
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user):
            token = Token.objects.get(user=user)
            data['token'] = token.key
        else:
            data['error'] = 'User does not have token . Try again ...'
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
```

## Go to "urls.py" and add the path 👇

```python
from users.api.views import RegisterView

path('register/', RegisterView.as_view()),
```

## Go to "user/api/serializers.py" and add UpdateUserSerializer👇

```python
class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            "username",
            "id",
            "email",
            "first_name",
            "last_name",
            "profile_pic",
            "biography",
        )
```

## Go to user/api/views.py and add "UpdateUserView" 👇

```python
class UpdateUserView(generics.RetrieveUpdateAPIView):
    #! We used RetrieveUpdateAPIView so that the user can only update. 👆
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
```

## 👇 Go to "user/api/urls.py" and add the path 👇

```python
path('update-profile/<int:pk>', UpdateUserView.as_view()),
```

## ✏ Create "api" folder under "blog" app and add the "views, serializers, urls" files.

## Create models in "models.py" under "blog" app 👇

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from blog.api.utils import get_random_code

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    STATUS = (
        ("d", "DRAFT"),
        ("p", "PUBLISHED"),
    )
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, related_name="post_user", on_delete=models.PROTECT, default='Anonymous User')
    category = models.ForeignKey(
        Category, related_name="post_category", on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    image = models.URLField(max_length=200, blank=True,
                            default="https://gravatar.com/avatar/2074b7945e3c6c493b0b2b94b24c35c2?s=400&d=robohash&r=x")
    published_date = models.DateTimeField(auto_now_add=True, blank=True)
    last_updated_date = models.DateTimeField(auto_now=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(
        User, related_name="like_user", on_delete=models.PROTECT)
    post = models.ForeignKey(
        BlogPost, related_name="like_post", on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Comment(models.Model):
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, related_name="comment_user",
                             on_delete=models.PROTECT, default='Anonymous User')
    post = models.ForeignKey(
        BlogPost, related_name="comment_post", on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Post_view(models.Model):
    user = models.ForeignKey(
        User, related_name="post_viewed_user", on_delete=models.PROTECT)
    post = models.ForeignKey(
        BlogPost, related_name="viewed_post", on_delete=models.CASCADE)
    viewed_date_time = models.DateTimeField(auto_now_add=True, blank=True)
```

## Register the models in "admin.py" 👇

```python
from django.contrib import admin

from blog.models import BlogPost, Category, Comment, Like, Post_view

admin.site.register(Category)
admin.site.register(Like)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Post_view)
```

## Create "signals.py" file under "blog/api" folder and add 👇

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from blog.models import BlogPost
from .utils import get_random_code

@receiver(pre_save, sender=BlogPost)
def pre_save_create_slug(sender, instance,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + " " + get_random_code())
```

## Create "utils.py" file under "blog/api" folder and add 👇

```python
import uuid
#! 👆 user uniqe id => Slug field must be uniqe

def get_random_code():
    code = str(uuid.uuid4())[:11].replace("-","")
    return code
```

##  Customize the BlogConfig() in "apps.py" in "blog"app 👇

```python
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    def ready(self):
        import blog.api.signals
```

## Go to "api/serializers.py" under "blog" app 👇

```python
from rest_framework import serializers
from blog.models import BlogPost, Category, Comment, Like, Post_view
from users.api.serializers import UserSerializer
from django.contrib.auth import get_user_model
# User = settings.AUTH_USER_MODEL
User = get_user_model()

# class AllUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = User
#         fields = (
#             "username",
#             "first_name",
#             "last_name",
#             "profile_pic",
#             "biography"
#         )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class CommentSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    # user_id = serializers.IntegerField()
    # post = serializers.StringRelatedField()
    # post_id = serializers.IntegerField()

    # class Meta:
    #     model = Comment
    #     fields = "__all__"

# kimin yorum yaptığını belirtmek için ilave edildi
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "time_stamp",
            "user",
        )

class LikeSerializer(serializers.ModelSerializer):
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


class BlogPostSerializer(serializers.ModelSerializer):
    comment_post = CommentSerializer(many=True, read_only=True)
    like_post = LikeSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.IntegerField(read_only=True)
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    post_view_count = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "author",
            "author_id",
            "category_id",
            "category",
            "content",
            "image",
            "published_date",
            "last_updated_date",
            "status",
            "slug",
            "like_count",
            "comment_count",
            "post_view_count",
            "comment_post",
            "like_post",
        )
        read_only_fields = (
            "published_date",
            "updated_date",
            "slug",
        )

    def get_like_count(self, obj):
        return Like.objects.filter(post=obj.id).count()

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj.id).count()

    def get_post_view_count(self, obj):
        return Post_view.objects.filter(post=obj.id).count()

```

## Go to "api/views.py" under blog app 👇

```python
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework import  generics, status
from blog.api.pagination import CustomLimitOffsetPagination
from blog.api.permissions import IsAdminUserOrReadOnly, IsPostOwnerOrReadOnly
from blog.api.serializers import BlogPostSerializer, CategorySerializer, CommentSerializer,LikeSerializer
from rest_framework.response import Response
from blog.models import BlogPost, Category, Post_view, Comment, Like


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
        user = request.data.get('user_id')
        post = request.data.get('post')
        serializer = self.get_serializer(data=request.data)
        exists_like = Like.objects.filter(user_id=user, post=post)
        serializer.is_valid(raise_exception=True)
        if exists_like:
            exists_like.delete()
        else:
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
```

## Create "permissions.py" file under "api" folder in the "blog" app and add 👇

```python
from rest_framework import permissions

class IsPostOwnerOrReadOnly(permissions.BasePermission):
    #! If the request.user is the same as the author, it can update/delete. Otherwise can view 👇
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    #! "Admin" can do any action. If not it can only view 👇
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin
```

## Create "pagination.py" file under "api" folder in the "blog" app and add 👇

```python
from rest_framework.pagination import LimitOffsetPagination

#! For 6 posts to appear on each page 👇
class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 6
```

##  Go to "blog/api/urls.py" and add the path 👇

```python
from .views import (
    CategoryView,
    BlogPostView,
    BlogPostDetailView,
    CommentView,
    LikeView
)
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("posts/", BlogPostView.as_view()),
    path("like/", LikeView.as_view()),
    path("posts/<str:slug>/", BlogPostDetailView.as_view()),
    path("posts/<str:slug>/add_comment/", CommentView.as_view()),
]
```

##  Do not forget to check the endpoints you wrote in [Postman](https://www.postman.com/).

## <center> END OF THE  BACKEND 🥳</center>

<hr>

# <center> FOR DJANGO DEPLOYMENT YOU CAN USE "PYTHON ANY WHERE"</center>

## 💻 Commands for setup 👇

```bash
    git clone https://github.com/githubUserName/projectName.git
    cd projectName
    python -m venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    echo SECRET_KEY=write_random_chars_to_here > .env
    python manage.py migrate
    $ python manage.py createsuperuser # optional
```

## Command for learn to current path 👇

```bash
    pwd
```

- "Add New Web App" with ManualConfigration with Python_LastVersion

- Set "Source Code" with "Main Path" (example: /home/anyWhereUserName/ProjectName)

- Set "Working Directory" with "Main Path" (example: /home/anyWhereUserName/ProjectName)

- Set "VirtualEnv" with "Env Path" (example: /home/anyWhereUserName/ProjectName/env)

## pythonanywhere/Web -> WSGI Configuration File(pythonanywhere_com_wsgi.py) 👇

```python
    import os
    import sys

    # Set: Project Main Path:
    path = '/home/anyWhereUserName/ProjectName'

    if path not in sys.path:
        sys.path.append(path)

    # Set: Where is settings.py:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'projectFolderName.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
```

##  Finished 

## ‼ Don't forget 👉 click to 'Reload' button before publish.

    if error, checking:

        settting.py:

            ALLOWED_HOSTS = ['*']

            # folder -> static-files-path:
            STATIC_URL = 'static/'
            # root -> static-files-path:
            STATIC_ROOT = BASE_DIR / STATIC_URL
            # Alternates:
            # if in base folder -> STATIC_ROOT = BASE_DIR / 'static/'
            # if in app folder -> STATIC_ROOT = BASE_DIR / 'appFolderName/static/'

        urls.py:

            from django.conf import settings
            from django.conf.urls.static import static
            # url -> static-files-path:
            urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

<hr>

# <center> FOR REACT CONFIGURATION <center>

## 💻 Install "cors-headers" for connecting with Frontend 👇

# <center>✔ DJANGO-CORS-HEADERS ✔</center>

<hr>

🔑 A Django App that adds [Cross-Origin Resource Sharing (CORS)](https://github.com/adamchainz/django-cors-headers) headers to responses.

🔑 This allows in-browser requests to your Django application from other origins.

🔑 Adding CORS headers allows your resources to be accessed on other domains.

🔑 It's important you understand the implications before adding the headers, since you could be unintentionally opening up your site's private data to others.

## 💻 To install cors-headers 👇

```bash
pip install django-cors-headers
```

## ✔ Add 'corsheaders' to "INSTALLED_APPS" in "settings.py" file.

## You will also need to add a middleware class to listen in on responses 👇

```python
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    ...,
]
```

## To allow all origins; add 👇

```python
CORS_ALLOW_ALL_ORIGINS=True
```

## Add a list of HTTP verbs that are allowed for the actual request 👇

```python
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
```

## Runserver 👇

```bash
python manage.py runserver
```

## Open the React Project and start it 👇

