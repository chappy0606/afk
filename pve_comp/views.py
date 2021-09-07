from rest_framework.views import exception_handler
from pve_comp.serializers import ChapterSerializer, PostSerializer, StageSerializer
from .models import Post, Chapter, Stage
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status, viewsets
from rest_framework.response import Response


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

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs) 
        except ValueError as e:
            content = {'detail': '{}'.format(e)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Post.objects.all()
        if self.request.GET:
            if self.request.GET.get('chapter_id') and self.request.GET.get('stage_id'):
                chapter = self.request.GET.get('chapter_id')
                stage = self.request.GET.get('stage_id')
                queryset = Post.objects.filter(
                    chapter_id=chapter, stage_id=stage)
            else:
                queryset = None

        return queryset