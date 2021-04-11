from django.contrib import admin
from .models import ChapterStage


class ChapterStageAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'stage', 'uploaded_at', 'uploaded_image')


admin.site.register(ChapterStage, ChapterStageAdmin)