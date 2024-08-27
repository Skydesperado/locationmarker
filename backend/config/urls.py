import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from apps.user.apis.views import RegisterAPIView, CustomTokenObtainPairAPIView

urlpatterns = [
    path(os.environ.get("ADMIN_SITE_URL", "admin/"), admin.site.urls),
    path("location/", include("apps.location.urls")),
    path("api/register/", RegisterAPIView.as_view()),
    path("api/token/", CustomTokenObtainPairAPIView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema")),
        path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
    ]
