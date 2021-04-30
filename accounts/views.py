from allauth.account.utils import user_username
from django.core.validators import ProhibitNullCharactersValidator
from django.http import request
from django.shortcuts import redirect
from allauth.account.views import LogoutView as AllAuthLogoutView
from django.views.generic import DetailView
from . models import User
from pve_comp.models import ChapterStage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class IndexRedirectView(AllAuthLogoutView):

    def get(self, *args, **kwargs):
        return redirect('index')


class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user'
    template_name = 'accounts/account/profile.html'

    def test_func(self):
        current_user = self.request.user
        return current_user.username == self.kwargs['username']

    def handle_no_permission(self):
        return redirect('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = ChapterStage.objects.filter(username=self.request.user).count
        return context
