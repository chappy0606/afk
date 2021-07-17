from . models import User
from rest_framework import viewsets
from django_filters import rest_framework as filters
from accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


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