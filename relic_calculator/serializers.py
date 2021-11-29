from rest_framework import fields, serializers
from .models import Relic


class RelicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relic
        fields = ('__all__')
