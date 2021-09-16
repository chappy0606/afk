from rest_framework import serializers
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from dj_rest_auth.registration.serializers import RegisterSerializer
from .adapter import CustomAccountAdapter


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'is_staff',
                'is_active', 'last_login', 'date_joined')


class CustomRegisterSerializer(serializers.ModelSerializer, RegisterSerializer, CustomAccountAdapter):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def validate_username(self, username):
        if 'tamako' in username.lower():
            raise serializers.ValidationError('tamakoはちょっと...')
        return super().clean_username(username)

    def validate_password(self, password):
        return super().clean_password(password)

    def validate(self, data):
        return data
