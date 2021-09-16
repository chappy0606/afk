from rest_framework import serializers
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from dj_rest_auth.registration.serializers import RegisterSerializer
from .password_validation import CustomValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'is_staff',
                'is_active', 'last_login', 'date_joined')


class CustomRegisterSerializer(serializers.ModelSerializer, RegisterSerializer, CustomValidator):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def validate_password(self, password):
        super().password_validate(password)
        return password

    def validate(self, data):
        return data
