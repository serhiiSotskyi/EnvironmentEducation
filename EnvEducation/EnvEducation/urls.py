"""
URL configuration for EnvEducation project.

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", include("main.urls")),
    path("educationalMaterials/", include("educationalMaterials.urls")),
    path("creativeTask/", include("creativeTask.urls")),
    path("blog/", include("blog.urls")),
    path("quiz/", include("quiz.urls")),
    path("legal/", include("legal.urls")),
    path("log/", include("log.urls")),
    path("log/", include('django.contrib.auth.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
