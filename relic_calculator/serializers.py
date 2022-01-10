from rest_framework import serializers

from .models import Relic

class RelicSerializer(serializers.ModelSerializer):
    quality = serializers.StringRelatedField()
    component1_relic = serializers.StringRelatedField()
    component2_relic = serializers.StringRelatedField()
    component3_relic = serializers.StringRelatedField()
    component4_relic = serializers.StringRelatedField()

    class Meta:
        model = Relic
        fields = ('id', 'en_name', 'ja_name', 'quality',
                'component1', 'component2', 'component3', 'component14',
                'cost', 'total_price', 'icon')
