from django.views.generic import TemplateView
from django.shortcuts import render


class TranslateView(TemplateView):
    template_name = "translate/translate.html"

    def get(self, request):
        return render(request, self.template_name)