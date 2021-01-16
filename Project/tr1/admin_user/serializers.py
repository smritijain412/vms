from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import CreateUser


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateUser
        fields = ('id', 'username', 'email', 'passwowrd', 'password2')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateUser
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True},
                        'password2': {'write_only': True}}

    def create(self, validated_data):
        user = CreateUser.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user
