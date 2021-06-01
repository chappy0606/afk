from django.urls import path
from . import views
from rest_framework import routers

# app_nameとnamespaseは同じ
app_name = 'pve_comp'

router = routers.DefaultRouter()
router.register('chapter', views.ChapterViewSet)
router.register('stage', views.StageViewSet)
router.register('chapter_stage', views.PostViewSet)