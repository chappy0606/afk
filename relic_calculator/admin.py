from django.contrib import admin
from .models import Quality, Relic

class QualityAdmin(admin.ModelAdmin):
    list_display = ('id', 'type',)


class RelicAdmin(admin.ModelAdmin):
    list_display = ('id', 'en_name', 'ja_name','quality', 'component1',
                    'component2', 'component3', 'component4', 'cost', 'total_price')


admin.site.register(Quality, QualityAdmin)
admin.site.register(Relic, RelicAdmin)
