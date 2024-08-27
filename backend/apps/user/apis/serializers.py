from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.user.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        if password1 != password2:
            raise serializers.ValidationError({"password2": "Passwords Must Match"})

        try:
            validate_password(password1)
        except serializers.ValidationError as exception:
            raise serializers.ValidationError({"password1": list(exception.messages)})

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password1")

        user = User(username=validated_data.get("username"), email=validated_data.get("email"), first_name=validated_data.get("first_name", ""), last_name=validated_data.get("last_name", ""))
        user.set_password(password)
        user.save()

        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token
