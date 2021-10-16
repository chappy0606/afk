from django.conf.global_settings import EMAIL_SSL_CERTFILE
from django.db.models.functions.datetime import TruncQuarter
from django.utils import timezone
from requests.api import delete
from rest_framework import status, viewsets
from rest_framework.generics import DestroyAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from dj_rest_auth import views
from django.contrib.auth.models import Permission, update_last_login

from accounts.models import User
from accounts.serializers import UserSerializer


class TestView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = '認証済みユーザーのみ返信してるよ'
        return Response(content)

class LoginView(views.LoginView):
    def post(self, request):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        
        self.login()
        update_last_login(None, self.user)
        
        return self.get_response()


class Test2(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = IsAdminUser
    permission_classes_by_action = {'create': [AllowAny],
                                    'list': [IsAdminUser],
                                    'destroy':[IsAuthenticated],
                                    'retrieve': [IsAuthenticated],}

    def has_permission(self):
        user = self.request.user
        if(self.get_object() == user or user.is_superuser):
            return True
        return False
    
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    # 詳細ページ
    def retrieve(self, request, *args, **kwargs):
        if(self.has_permission()):
            return super().retrieve(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def destroy(self, request, *args, **kwargs):
        if(self.has_permission()):
            instance = self.get_object()
            instance.is_active = False
            instance.deleted_at = timezone.now()
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_403_FORBIDDEN)

    


class Test3(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        request.user.is_active = False
        request.user.deleted_at = timezone.now()
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
