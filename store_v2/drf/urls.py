from django.urls import path, include
from rest_framework import routers
from . import views
from store_v2.search.views import SearchProductInventory

router = routers.DefaultRouter()
router.register(r"api", views.AllProductsViewSet, basename=("allproducts"))
router.register(
    r"product/(?P<slug>[^/.]+)",
    views.ProductInventoryView,
    basename=("products"),
)

urlpatterns = [
    path("", include(router.urls)),
    path("search/<str:query>/", SearchProductInventory.as_view()),
]
