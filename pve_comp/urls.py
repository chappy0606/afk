from django.urls import path
from . import views

# app_nameとnamespaseは同じ
app_name = 'pve_comp'

urlpatterns = [
    path("", views.TranslateView.as_view(), name='pve_comp'),
]