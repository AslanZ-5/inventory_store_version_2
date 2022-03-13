from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include("store_v2.demo.urls", namespace="demo")),
]
