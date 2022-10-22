from django.contrib import admin

from blog.models import (
    BlogPost, 
    Category, 
    Comment, 
    Like, 
    Post_view
)

admin.site.register(Category)
admin.site.register(Like)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Post_view)
# Register your models here.

#! Modelleri admin ile ulaşabilmek için admin girip istekte neleri görmek istediğimizi kaydederiz