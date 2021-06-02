from django.urls import path
from . import views
from rest_framework import routers

# app_nameとnamespaseは同じ

router = routers.DefaultRouter()
router.register('chapter', views.ChapterViewSet)
router.register('stage', views.StageViewSet)
router.register('posts', views.PostViewSet)