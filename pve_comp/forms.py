from django import forms
from . models import ChapterStage
from django import forms

class UploadForm(forms.ModelForm):
    class Meta:
        model = ChapterStage
        fields = ('chapter_id', 'stage_id', 'uploaded_image')

class SelectForm(forms.ModelForm):
    class Meta:
        model = ChapterStage
        fields = ('chapter_id', 'stage_id')