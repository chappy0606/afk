from rest_framework import serializers

from .models import Relic

class RelicSerializer(serializers.ModelSerializer):
    quality = serializers.StringRelatedField()
    compornent1 = serializers.StringRelatedField()
    compornent2 = serializers.StringRelatedField()
    compornent3 = serializers.StringRelatedField()
    compornent4 = serializers.StringRelatedField()

    class Meta:
        model = Relic
        fields = ('id', 'en_name', 'ja_name', 'quality',
                'compornent1', 'compornent2', 'compornent3', 'compornent4',
                'cost', 'total_price', 'icon')
