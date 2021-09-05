from accounts.views import CustomLoginView, TestView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pve_comp.urls import router as pve_comp_router

urlpatterns = [
    
    # 削除候補
    path('api/v1/test/', TestView.as_view()),

    path('api/v1/auth/login/', CustomLoginView.as_view()),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('api/v1/campaign/', include(pve_comp_router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
