from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.urls import router as user_router
from pve_comp.urls import router as pve_comp_router
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/token/', obtain_jwt_token),
    path('api/v1/token/verify/', verify_jwt_token),
    path('api/v1/token/refresh/', refresh_jwt_token),
    path('api/v1/account/', include(user_router.urls)),
    path('api/v1/campaign/', include(pve_comp_router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
