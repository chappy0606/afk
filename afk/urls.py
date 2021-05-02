from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from accounts.urls import router as user_router
from pve_comp.urls import router as pve_comp_router

urlpatterns = [
    path('', TemplateView.as_view(template_name='index/index.html'), name='index'),
    path('pve_comp/', include('pve_comp.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include(user_router.urls)),
    path('api/', include(pve_comp_router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
