from django_filters import rest_framework as filters
from rest_framework.response import Response
from pve_comp.serializers import ChapterSerializer, PostSerializer, StageSerializer
from .models import Post, Chapter, Stage
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ChapterViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Chapter.objects.all()
        serializer = ChapterSerializer(queryset,many=True)
        return Response(serializer.data)

class StageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Stage.objects.all()
        serializer = StageSerializer(queryset, many=True)
        return Response(serializer.data)


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
