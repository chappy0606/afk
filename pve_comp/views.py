from django.db.models import fields, query
from django.views.generic import TemplateView, CreateView, ListView
from django.shortcuts import redirect, render
from .models import ChapterStage
from django.urls import reverse_lazy
from .forms import UploadForm
from .forms import SelectForm


class PveCompView(TemplateView):
    template_name = 'pve_comp/pve_comp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SelectForm()
        return context


class UploadView(CreateView):
    model = ChapterStage
    form_class = UploadForm
    template_name = 'pve_comp/upload.html'
    success_url = reverse_lazy('pve_comp:upload')

class ResultView(ListView):
    template_name = 'pve_comp/result.html'
    model = ChapterStage
    context_object_name = 'chapter_stage_list'
    
    def get_queryset(self):
        chapter_id = self.request.GET['chapter_id']
        stage_id = self.request.GET['stage_id']
        
        queryset = ChapterStage.objects.filter(
            chapter_id = chapter_id, stage_id = stage_id)
        return queryset