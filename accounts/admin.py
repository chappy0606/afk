from django.contrib import admin
from . models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

# Register your models here.
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',),
        }),
        (_('Important dates'), {
         'fields': ('last_login', 'created_at', 'deleted_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'is_staff', 'is_active','is_superuser')
    search_fields = ('username',)
    ordering = ('username',)

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
