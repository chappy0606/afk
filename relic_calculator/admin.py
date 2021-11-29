from django.contrib import admin
from .models import Quality, Relic

# Register your models here.

class QualityAdmin(admin.ModelAdmin):
    list_display = ('id', 'type',)


class RelicAdmin(admin.ModelAdmin):
    list_display = ('id', 'en_name', 'ja_name','quality', 'compornent1',
                    'compornent2', 'compornent3', 'compornent4', 'cost', 'total_price')


admin.site.register(Quality, QualityAdmin)
admin.site.register(Relic, RelicAdmin)