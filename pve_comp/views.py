from django_filters import rest_framework as filters
from rest_framework.decorators import action
from pve_comp.serializers import ChapterSerializer, PostSerializer, StageSerializer
from .models import Post, Chapter, Stage
from rest_framework import viewsets
from rest_framework.response import Response


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class PostFilter(filters.FilterSet):
    chapter_id = filters.NumberFilter(lookup_expr='exact')
    stage_id = filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Post
        fields = ['chapter_id', 'stage_id']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_class = PostFilter

    @action(methods=['post'], detail=False)
    def test(self, request):
        content = 'postされたよーーー'
        return Response(content)
    
    @action(methods=['get'], detail=False)
    def test2(self, request):
        content = 'getされたよーーー'
        return Response(content)
