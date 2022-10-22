from django.db import models
from django.contrib.auth.models import User

class TimeStamp(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name

class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
  
    title = models.CharField(max_length=100)    
    content = models.TextField()
    image = models.URLField(default='https://picsum.photos/500/300?random=1',blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    # slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.title

     # @property
    # def quiz_count(self):
    #     return self.quizz.count()  # related name varsa
        #return self.quiz_set.count() # related name yoksa classname.lower()_set

    # def comment_count(self):
    #     return self.comment_set.all().count()
        
    # def comment_count(self):
    #     return self.comment_post.all().count()
    
    # def view_count(self):
    #     return self.postview_set.all().count()
    
    # def like_count(self):
    #     return self.like_set.all().count()
    
    # def comments(self):
    #     return self.comment_set.all()

class Comment(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user", default="Anonymous User")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comment_post")

    content = models.TextField()
    
    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like_post")

    def __str__(self):
        return self.user.username
    
class PostView(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="view_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="view_user")
   
    
    def __str__(self):
        return self.user.username