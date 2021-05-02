from django.db import router
from django.urls import path
from . import views
from rest_framework import routers


app_name = 'accounts'

urlpatterns = [
    path('logout/', views.CustomAllAuthLogoutView.as_view(),),
    path('profile/<username>/', views.UserDetailView.as_view(), name='user_detail'),
]

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
