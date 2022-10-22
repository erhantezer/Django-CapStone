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