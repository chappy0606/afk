from django.shortcuts import render
from allauth.account.views import LogoutView as AllAuthLogoutView

class LogoutView(AllAuthLogoutView):
    template_name = 'index/index.html'