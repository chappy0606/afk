from django.contrib import admin
from .models import Post, Chapter, Stage

class ChapterStageAdmin(admin.ModelAdmin):
    list_display = ('chapter_id', 'stage_id', 'user', 'uploaded_at', 'uploaded_image')

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id',)

class StageAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Post, ChapterStageAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Stage, StageAdmin)
