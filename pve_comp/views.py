from copy import error
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from pve_comp.serializers import ChapterSerializer, PostSerializer, StageSerializer
from .models import Post, Chapter, Stage
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ChapterViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Chapter.objects.all()
        serializer = ChapterSerializer(queryset, many=True)
        return Response(serializer.data)


class StageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Stage.objects.all()
        serializer = StageSerializer(queryset, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Post.objects.all()

        if self.request.GET:
            queryset = None

        if self.request.GET.get('chapter_id') and self.request.GET.get('stage_id'):
            chapter = self.request.GET.get('chapter_id')
            stage = self.request.GET.get('stage_id')
            queryset = Post.objects.filter(
                chapter_id=chapter, stage_id=stage)

        return queryset
