from . import views
from django.urls import path

urlpatterns = [
    path('relics', views.RelicView.as_view()),
]