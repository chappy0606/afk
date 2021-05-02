from django.contrib import admin
from .models import ChapterStage
from .models import Chapter
from .models import Stage

class ChapterStageAdmin(admin.ModelAdmin):
    list_display = ('chapter_id', 'stage_id', 'user', 'uploaded_at', 'uploaded_image')

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id',)

class StageAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(ChapterStage, ChapterStageAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Stage, StageAdmin)
