from django.urls import path
from . import views

# app_nameとnamespaseは同じ
app_name = 'pve_comp'

urlpatterns = [
    path('', views.PveCompView.as_view(), name='pve_comp'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('result/', views.ResultView.as_view(), name='result'),
]