from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('chapter', views.ChapterViewSet)
router.register('stage', views.StageViewSet)
router.register('posts', views.PostViewSet)