from rest_framework.response import Response
from pve_comp.serializers import ChapterSerializer, PostSerializer, StageSerializer
from .models import Post, Chapter, Stage
from rest_framework import serializers, viewsets
from rest_framework.exceptions import APIException, ValidationError
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

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except ValueError:
            raise serializers.ValidationError

    # def handle_exception(self, exc):
    #     try:
    #         return super(PostViewSet,self).handle_exception(exc)
    #     except ValueError:
    #         content = {'detail': '{}'.format(exc)}
    #         raise APIException
    #         # return Response(content, status=status.HTTP_404_NOT_FOUND)

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
