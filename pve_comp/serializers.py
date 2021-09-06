from rest_framework import serializers
from .models import Chapter, Stage, Post
from accounts.serializers import UserSerializer

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id',)


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'chapter_id', 'stage_id', 'user',
                'uploaded_image', 'uploaded_at',)
