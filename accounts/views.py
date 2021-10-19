from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from dj_rest_auth import views
from django.contrib.auth.models import update_last_login

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
    permission_classes = [IsAdminUser]
    permission_classes_by_action = {'create': [AllowAny],
                                    'list': [IsAdminUser],
                                    'destroy':[IsAuthenticated],
                                    'retrieve': [IsAuthenticated],
                                    'partial_update': [IsAuthenticated], }

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

    def partial_update(self, request, *args, **kwargs):
        if(self.has_permission()):
            return super().partial_update(request, *args, **kwargs)

        return Response(status=status.HTTP_403_FORBIDDEN)
    
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
