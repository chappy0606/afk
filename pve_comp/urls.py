from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('chapters', views.ChapterViewSet, basename='chapters')
router.register('stages', views.StageViewSet, basename='stages')
router.register('posts', views.PostViewSet)
