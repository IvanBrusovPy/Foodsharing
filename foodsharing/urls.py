from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("share_service.urls")),
    path("admin/", admin.site.urls),
]