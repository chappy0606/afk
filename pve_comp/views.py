from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from pve_comp.forms import UploadForm
from .models import ChapterStage
from django.urls import reverse_lazy


class PveCompView(TemplateView):
    template_name = 'pve_comp/pve_comp.html'

    # def get(self, request):
    #     return render(request, self.template_name)


class UploadView(CreateView):
    model = ChapterStage
    form_class = UploadForm
    template_name = 'pve_comp/upload.html'
    success_url = reverse_lazy('pve_comp:upload')
    

    # def get(self, request):
    #     return render(request, self.template_name)