from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('chapters', views.ChapterViewSet)
router.register('stages', views.StageViewSet)
router.register('posts', views.PostViewSet)