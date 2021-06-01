from pve_comp.serializers import ChapterSerializer, PostSerializer, StageSerializer
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib import messages
from .models import Post, Chapter, Stage
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets


# class PveCompView(TemplateView):
#     template_name = 'pve_comp/pve_comp.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = SelectForm()

#         return context


# class UploadView(LoginRequiredMixin, CreateView):
#     model = ChapterStage
#     form_class = UploadForm
#     template_name = 'pve_comp/upload.html'
#     success_url = reverse_lazy('pve_comp:upload')

#     def form_valid(self, form):
#         form.instance.username = self.request.user
#         messages.success(self.request, 'アップロードが完了しました')

#         return super(UploadView, self).form_valid(form)


# class ResultView(ListView):
#     template_name = 'pve_comp/result.html'
#     model = ChapterStage
#     context_object_name = 'chapter_stage_list'

#     def get_queryset(self):
#         queryset = ChapterStage.objects.filter(
#             chapter_id=self.request.GET['chapter_id'],
#             stage_id=self.request.GET['stage_id'])

#         return queryset


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
