from rest_framework import serializers
from accounts.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'is_staff',
                'is_active', 'last_login', 'date_joined')


class CustomRegisterSerializer(RegisterSerializer):

    def validate_username(self, username):
        print('---------------------------------')
        print('callcvalidate')
        if 'tamako' in username.lower():
            raise serializers.ValidationError('tamakoはちょっと...')
        return username