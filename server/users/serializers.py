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
#! yukarıda yazdığımız User içerisindeki register içindeki  email, password, pasword1 yada password2 de diyebilirdik özelleştirdik
#! password ekledik ayrıca email = models.EmailField(_("email address"), blank=True) özelleştirdik


    class Meta:
#! Burada User u inherit ederek içindeki fields kullanarak ve özelleştirdiğimiz verileri RegisterSerializer içine attık
        model =User
        fields= [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password1"
        ]
        
  # Passwordu validate yani User dan inherit ettiğimiz  data içerisinden (fields) getirip password değişkeni içerisine atttık ve validate içerisinden password1 i pop ile sildik  kalan datayı create edip user değişkeni içerisine attık user değişkeni içerisindeki getirdiğimiz password değişkeni içerisindeki passwordu user içindeki passworda make_password(password) olarak yeni password değeri yaptık
    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError({"password":"Password fields didn't match"})
        return data
#! yukarıda  password ile pasword1 doğruluğunu karşılaştırdık       
        
              
        
        
#!  dogrulanan veri (validated_data) meta da eklenmiş fields lerin içinde yani RegisterSerializer içindeki passwordu get ile çağırıp bir password değişkenine atıyoruz aynı zamanda validate data içindeki password1 i siliyoruz ki passwordu data da görmeyelim çünkü herkes görmüş olur data içinde kalırsa User object lerin içine vaalidate_data create edip gönderdik ve bunu user değişkenine attık user değişkeninin içindeki passwordu make_password fonksiyonu içindeki password değişkeni şeklinde oluşturmuş olduk
    def create(self,validated_data): 
        password = validated_data.get("password")
        validated_data.pop("password1")
        user = User.objects.create(**validated_data)
        user.password = make_password(password)
        user.save()
        return user
    
  

#! kendimize göre yeni bir User dan inherit ederek field lerini kullanarak ve fullname ekleyerek bir methodfield yazarak serializer yazdık  
#? AMACIMIZ KULLANICI BİLGİLERİNİN TAMAMINI GÖRMEK VE BUNLARI KULLANABİLMEK 
#############! BU KISIMDAN İTİBAREN LOGİN İŞLEMLERİ İÇİN VERİLERİ GÖRMEK İÇİN YAZDIK ###############
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
#!KEY YANİ TOKEN ARDINDAN DA USERSERİALİZER İÇİNDEKİ VERİLER user İÇİNDE OLUŞTURULDU "http://127.0.0.1:8000/users/auth/login/" BURADAN BAKINIZ
class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        model = Token
        fields = ("key", "user")    