from django.views.generic import TemplateView
from django.shortcuts import render


class TranslateView(TemplateView):
    template_name = "pve_comp/pve_comp.html"

    def get(self, request):
        return render(request, self.template_name)