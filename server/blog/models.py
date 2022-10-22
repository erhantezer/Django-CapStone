from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from .utils import get_random_code


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
    author = models.ForeignKey(User, related_name="post_user", on_delete=models.PROTECT, default='Anonymous User')
    category = models.ForeignKey(Category, related_name="post_category", on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    image = models.URLField(max_length=200, blank=True, default="https://picsum.photos/500/300?random=1")
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
    user = models.ForeignKey(User, related_name="comment_user", on_delete=models.PROTECT, default='Anonymous User')
    post = models.ForeignKey(BlogPost, related_name="comment_post", on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Post_view(models.Model):
    user = models.ForeignKey(User, related_name="post_viewed_user", on_delete=models.PROTECT)
    post = models.ForeignKey(BlogPost, related_name="viewed_post", on_delete=models.CASCADE)
    viewed_date_time = models.DateTimeField(auto_now_add=True, blank=True)
    
    