from django.shortcuts import render, redirect
from allauth.account.views import LogoutView as AllAuthLogoutView

class IndexRedirectView(AllAuthLogoutView):
    
    def get(self, *args, **kwargs):
        return redirect('index')
