from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('logout/', views.IndexRedirectView.as_view(), name='redirect'),
]