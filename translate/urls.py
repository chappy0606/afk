from django.urls import path
from . import views

app_name = 'translate'

urlpatterns = [
    path("", views.TranslateView.as_view(), name='translate'),
]