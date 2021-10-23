from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from rest_framework.fields import CharField, SerializerMethodField
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from string import ascii_uppercase, ascii_lowercase, digits
from pve_comp.models import Post

try:
    from allauth.account import app_settings as allauth_settings
except ImportError:
    raise ImportError('allauth needs to be added to INSTALLED_APPS.')


class BaseSerializer(serializers.ModelSerializer):
    user_name = CharField(source='username')

    class Meta:
        model = User
        fields = ('id', 'user_name')


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'chapter_id', 'stage_id', 'uploaded_at')

class UserDetailSerializer(BaseSerializer):
    posts = SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'user_name', 'posts', 'is_active', 'email')
        extra_kwargs = {
            'is_active': {'write_only': True},
            'email': {'write_only': True}
        }

    def get_posts(self, obj):
        try:
            return PostsSerializer(Post.objects.filter(user=obj.id), many=True).data
        except:
            return None

class CustomLoginSerializer(BaseSerializer, LoginSerializer):

    class Meta(BaseSerializer.Meta):
        fields = ('user_name', 'password')


def contain_any(target, condition_list):
    return any([i in target for i in condition_list])

class CustomRegisterSerializer(BaseSerializer, RegisterSerializer):
    email = serializers.EmailField(
        required=allauth_settings.EMAIL_REQUIRED, allow_blank=True)

    class Meta(BaseSerializer.Meta):
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
