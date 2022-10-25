from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
    
    def ready(self):
        import blog.signals
#! signals kullandığımızda signalın hazır olduğu methodu BlogConfig clasında oluştururuz ve import olarak blog uygulamasındaki signals diye belirtiriz
