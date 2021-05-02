from rest_framework import serializers
from .models import Chapter, Stage, ChapterStage
from accounts.serializers import UserSerializer


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id',)


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id',)


class ChapterStageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = ChapterStage
        fields = ('id', 'chapter_id', 'stage_id', 'user',
                'uploaded_image', 'uploaded_at',)
