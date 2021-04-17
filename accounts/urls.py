from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('accounts/login/', TemplateView.as_view(template_name='login.html')),
    path('accounts/logout/', TemplateView.as_view(template_name='logout.html')),
    path('accounts/signup/',  TemplateView.as_view(template_name='signup.html')),
]