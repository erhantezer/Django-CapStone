
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class RegisterSerializers(serializers.ModelSerializer):
    email =serializers.EmailField(
       required=True,
       validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        required =True,
        write_only=True,
        style={"input_type":"password"},
        
    )
    
    class Meta:
        model:User
        