from django import forms
from django.db.models import fields
from django.forms.models import model_to_dict
from . models import ChapterStage

class UploadForm(forms.ModelForm):
    class Meta:
        model = ChapterStage
        fields = ('chapter_id', 'stage_id', 'uploaded_image',)
