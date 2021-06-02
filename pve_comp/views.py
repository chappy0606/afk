from django_filters import rest_framework as filters
from django_filters.filters import OrderingFilter
from pve_comp.serializers import ChapterSerializer, PostSerializer, StageSerializer
from .models import Post, Chapter, Stage
from rest_framework import viewsets


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer



class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = ['chapter_id', 'stage_id', 'user']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    chapter_id = filters.NumberFilter(lookup_expr='exact')
    stage_id = filters.NumberFilter(lookup_expr='exact')
    user = filters.CharFilter(lookup_expr='exact')
    filter_class = PostFilter
