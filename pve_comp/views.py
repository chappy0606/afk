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
            print('クエリパラメータがない')
            return super().list(request, *args, **kwargs)
        else:
            print('クエリパラメータある')
            if ('chapter_id' and 'stage_id') not in request.GET.keys():
                print('keyがない')
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                print('keyある')
                if not (request.GET.get('chapter_id') and request.GET.get('stage_id')):
                    print('両方に値がない')
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    print('両方値がある')
                    try:
                        return super().list(request, *args, **kwargs)
                    except ValueError:
                        print('値が違う')
                        return Response(status=status.HTTP_400_BAD_REQUEST)
        # if request.GET:
        #     print('クエリパラメータがある')
        #     if ('chapter_id' and 'stage_id') in request.GET.keys():
        #         print('keyが両方ある')
        #         if request.GET.get('chapter_id') and request.GET.get('stage_id'):
        #             print('両方に値がある')
        #             try:
        #                 return super().list(request, *args, **kwargs)
        #             except ValueError:
        #                 print('値が違う')
        #                 return Response(status=status.HTTP_400_BAD_REQUEST)
        #         else:
        #             print('片方or両方値がない')
        #             return Response(status=status.HTTP_400_BAD_REQUEST)
        #     else:
        #         print('keyが足りてない')
        #         return Response(status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     print('クエリパラメータない')
        #     return super().list(request, *args, **kwargs)

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
