
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view


#! URL de oluşturulan endpointe göre buradaki fonksiyonu çalıştırarak dj_rest_auth otomatik çalıştırdık register özelleştirdiğimiz için registeri
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    

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