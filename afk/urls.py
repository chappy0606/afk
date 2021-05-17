from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from accounts.urls import router as user_router
from pve_comp.urls import router as pve_comp_router

urlpatterns = [
    # path('accounts/', include('accounts.urls')),
    # path('accounts/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/', include(user_router.urls)),
    path('api/v1/', include(pve_comp_router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
