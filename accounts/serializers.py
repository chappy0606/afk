from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from rest_framework.fields import CharField
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from string import ascii_uppercase, ascii_lowercase, digits

try:
    from allauth.account import app_settings as allauth_settings
except ImportError:
    raise ImportError('allauth needs to be added to INSTALLED_APPS.')


class UserSerializer(serializers.ModelSerializer):
    user_name = CharField(source='username')

    class Meta:
        model = User
        fields = ('id', 'user_name', 'is_active')
        extra_kwargs = {
            'is_active': {'write_only': True}
        }

class CustomLoginSerializer(UserSerializer, LoginSerializer):

    class Meta(UserSerializer.Meta):
        fields = ('user_name', 'password')


def contain_any(target, condition_list):
    return any([i in target for i in condition_list])

class CustomRegisterSerializer(UserSerializer, RegisterSerializer):
    email = serializers.EmailField(
        required=allauth_settings.EMAIL_REQUIRED, allow_blank=True)

    class Meta(UserSerializer.Meta):
        fields = ('user_name', 'password', 'email')

    def validate_password(self, password):
        if not all([contain_any(password, ascii_lowercase),
                    contain_any(password, ascii_uppercase),
                    contain_any(password, digits),
                    len(password) >= 8]):

            raise ValidationError("パスワードは(大小英字、数字）全てを組み合わせて8文字以上に設定してください。")
        return password

    def validate(self, data):
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
        }
