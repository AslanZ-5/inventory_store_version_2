from rest_framework import viewsets, permissions

from store_v2.drf.serializer import AllProducts
from store_v2.inventory.models import Product


class AllProductsViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()[:40]
    serializer_class = AllProducts
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
