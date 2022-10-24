
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view


#! URL de oluşturulan endpointe göre buradaki fonksiyonu çalıştırarak dj_rest_auth otomatik olarak kendi gömülü view çalıştırdık register özelleştirdiğimiz için registeri burada registerview olarak oluşturduk. Burada User içindeki verileri queryset (Bir QuerySet, bir veritabanından bir veri topluluğudur. Bir QuerySet, nesnelerin bir listesi olarak oluşturulur.) queryset içine User içindeki verilerin tamamını attık serializer_class a ise serializer.py deki RegisterSerializers clasını attık.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    
# def get_serializer(self, *args, **kwargs):
#         """
#         Return the serializer instance that should be used for validating and
#         deserializing input, and for serializing output.
#         """
#         serializer_class = self.get_serializer_class()
#         kwargs.setdefault('context', self.get_serializer_context())
#         return serializer_class(*args, **kwargs)
#! Yukarıda yeşil yorum kısmında get_serializer ın bütün verileri alıp bizim serializer_class(RegisterSerializers) daki verilerin tamamını aldığı görülüyor getirme isteğini datasını dataya atarak çağırma işlemi yaptık ve bunu serializer e attık serialezer içindeki veriler doğrumu diye kontrol edip hata varsa belirt dedik serializeri kaydetip user a attık serializer içindeki data yı da data ya attık ardından Token (inherit edilen token) obje içindeki önceden giridğimiz user ile sonradan girdiğimiz user filtreleyerek bakar exists() ile Token içinde varmı yokmu karşılaştırır varsa user eşit olanın keyini token değişkenine attık ardından data içindeki key(token) value olarak token attık data["token"] = token yoksa eğer hata döndürdük cevap olarak datayı statusu ve headers i cevap olarak dödük

#? BURADAKİ ASIL MESELEMİZ DATA İÇNDEKİ VE SERİALİZER İÇİNDEKİ VERİLERİN ENDPOİNTE ÇAĞRILDIĞINDA DATALARIN GELMESİDİR İŞİDİR
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user).key
            data["token"] = token
        else:
            data["token"] = "No token created for this user.... :))"
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    
# @api_view(['POST'])
# def logout(request):
#     request.user.auth_token.delete()
#     data = {'message': 'succesfully logout'}
#     return Response(data,status=status.HTTP_200_OK)