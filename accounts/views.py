from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from dj_rest_auth import views
from django.contrib.auth.models import update_last_login


class TestView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = '認証済みユーザーのみ返信してるよ'
        return Response(content)

class CustomLoginView(views.LoginView):
    def post(self, request):

        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        
        self.login()
        update_last_login(None, self.user)
        
        return self.get_response()


class AuthInfoDeleteView(views.UserDetailsView, RetrieveUpdateDestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        request.user.is_active = False
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
