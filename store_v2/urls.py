from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from store_v2.drf import views

router = routers.DefaultRouter()
router.register(r"api", views.AllProductsViewSet, basename=("allproducts"))

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include("store_v2.demo.urls", namespace="demo")),
    path("", include(router.urls)),
]
