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
        if not request.GET:
            return super().list(request, *args, **kwargs)

        if ('chapter_id' and 'stage_id') not in request.GET.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if not (request.GET.get('chapter_id') and request.GET.get('stage_id')):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            return super().list(request, *args, **kwargs)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if self.request.GET.get('chapter_id') and self.request.GET.get('stage_id'):
            chapter = self.request.GET.get('chapter_id')
            stage = self.request.GET.get('stage_id')
            return Post.objects.filter(
                chapter_id=chapter, stage_id=stage)
        
        return Post.objects.all()