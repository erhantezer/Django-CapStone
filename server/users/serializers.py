from rest_framework import serializers,validators
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password





class RegisterSerializers(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all(),message="Email must unique")]   
    )
    password =serializers.CharField(
        required=True,
        write_only=True,
        style={"input_type":"password"}
    )
    password1 =serializers.CharField(
        required=True,
        write_only=True,
        style={"input_type":"password"}
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

    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError({"password":"Password fields didn't match"})
        return data