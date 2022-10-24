from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import BlogPost
from .utils import get_random_code

@receiver(pre_save, sender=BlogPost)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + " " + get_random_code())
        
        
#! Sinyaller framework içerisinde bir işlem gerçekleştiğinde bundan haberdar olmamızı sağlayan sistemdir.

#! Django bazı işemler için built-in olarak sinyal gönderir:
#! Modelin save() methodu çağırılmadan önce ve çağırıldıktan sonra
#! Modelin delete() methodu çağırılmadan önce ve çağırıldıktan sonra
#! Modeldeki ManytoManyField değiştiğinde
#! HTTP requesti başladığında ve bittiğinde

#Sinyalleri dinlemeyi receiver() dekoratörü ile yaparız yada  Sinyalleri dinlemek için signal.connect() ile bir alıcı fonksiyonu oluşturulur. Sinyal gönderildiğinde alıcı fonksiyonu çağırılır. 

# from django.db.models.signals import post_save
# def do_something(sender, **kwargs):
#     …
# post_save.connect(do_something)