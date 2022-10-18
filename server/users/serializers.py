from rest_framework import serializers,validators
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from dj_rest_auth.serializers import TokenSerializer
from rest_framework.authtoken.models import Token



class RegisterSerializers(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all(), message="Email must unique")]   # Başka bir kullanıcının girdiği email ile aynı olmasını engelleyen doğrulayıcı (validators) yazdık
    )
    password =serializers.CharField(
        required=True,
        write_only=True,
        style={"input_type":"password"},
    )
    password1 =serializers.CharField(
        required=True,
        write_only=True,
        style={"input_type":"password"},
    )

    class Meta:
        model =User
        fields= [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password1"
        ]
    def create(self,validated_data): 
        password = validated_data.get("password")
        validated_data.pop("password1")
        
        user = User.objects.create(**validated_data)
        user.password = make_password(password)
        user.save()
        return user
    # Passwordu validate yani User dan inherit ettiğimiz  data içerisinden (fields) getirip password değişkeni içerisine atttık ve validate içerisinden password1 i pop ile sildik  kalan datayı create edip user değişkeni içerisine attık user değişkeni içerisindeki getirdiğimiz password değişkeni içerisindeki passwordu user içindeki passworda make_password(password) olarak yeni password değeri yaptık

    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError({"password":"Password fields didn't match"})
        return data
    
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            # "is_staff",# frontend kısmında butonların aktif olması için
        )
        
    def get_full_name(self,obj):
        return f"{obj.first_name.title()} {obj.last_name.upper()}"

# custom token serializer yazmak
class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        model = Token
        fields = ("key", "user")    