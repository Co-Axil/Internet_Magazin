"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from apps import users

urlpatterns = [
    # admin
    path(os.environ.get("ADMIN_URL"), admin.site.urls),
    # swagger
    path(
        'os.environ.get("SWAGGER_DOWNLOAD_URL")',
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        os.environ.get("SWAGGER_URL"),
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        os.environ.get("REDOC_URL"),
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # local apps
    path("users/", include("apps.users.urls", namespace="users")),
    path("users/", include("apps.users.urls", namespace="users")),
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('', include('apps.onlinemarket.urls')),
    path('users/', include('apps.users.urls')),
    path('', include('admin_tabler.urls')),
    path('', TemplateView.as_view(template_name="base.html"), name="home"),  # Bosh sahifa
    path('products/', include('apps.onlinemarket.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
