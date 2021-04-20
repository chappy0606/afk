from django.views.generic import TemplateView, CreateView
from django.shortcuts import redirect, render
from pve_comp.forms import UploadForm
from .models import ChapterStage
from django.urls import reverse_lazy
import datetime


class PveCompView(TemplateView):
    template_name = 'pve_comp/pve_comp.html'


class UploadView(CreateView):
    model = ChapterStage
    form_class = UploadForm
    template_name = 'pve_comp/upload.html'
    success_url = reverse_lazy('pve_comp:upload')