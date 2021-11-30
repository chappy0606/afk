from rest_framework import generics
from .models import Relic
from .serializers import RelicSerializer

class RelicView(generics.ListAPIView):
    queryset = Relic.objects.all()
    serializer_class = RelicSerializer