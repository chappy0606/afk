from rest_framework import serializers

from .models import Relic

class RelicSerializer(serializers.ModelSerializer):
    quality = serializers.StringRelatedField()
    component1 = serializers.StringRelatedField()
    component2 = serializers.StringRelatedField()
    component3 = serializers.StringRelatedField()
    component4 = serializers.StringRelatedField()

    class Meta:
        model = Relic
        fields = ('id', 'en_name', 'ja_name', 'quality',
                'component1', 'component2', 'component3', 'component4',
                'cost', 'total_price', 'icon')
