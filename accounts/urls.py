from django.db import router
from . import views
from rest_framework import routers


# app_name = 'accounts'
router = routers.DefaultRouter()
router.register('test2', views.Test2)