from datetime import datetime, timezone
from django.db.models.query_utils import select_related_descend
from rest_framework.response import Response
from . models import User
from rest_framework import viewsets
from django_filters import rest_framework as filters
from accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from dj_rest_auth import views
from django.contrib.auth.models import update_last_login


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = User
        fields = ['username']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = User.objects.filter(username=self.request.user)
    #     return queryset


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
