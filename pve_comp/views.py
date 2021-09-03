from django_filters import rest_framework as filters
from pve_comp.serializers import ChapterSerializer, PostSerializer, StageSerializer
from .models import Post, Chapter, Stage
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class PostFilter(filters.FilterSet):
    username = filters.CharFilter(field_name='user__username')

    class Meta:
        model = Post
        fields = ['user','username','chapter_id', 'stage_id' ]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_class = PostFilter
    permission_classes = [IsAuthenticatedOrReadOnly]