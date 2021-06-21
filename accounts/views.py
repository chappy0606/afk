from django.shortcuts import redirect
from allauth.account.views import LogoutView as AllAuthLogoutView
from django.views.generic import DetailView
from . models import User
from pve_comp.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets
from accounts.serializers import UserSerializer

# class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = User
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
#     context_object_name = 'user'
#     template_name = 'accounts/account/profile.html'

#     def test_func(self):
#         current_user = self.request.user
#         return current_user.username == self.kwargs['username']

#     def handle_no_permission(self):
#         return redirect('index')

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['posts'] = Post.objects.filter(
#             username=self.request.user).count
#         return context


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer