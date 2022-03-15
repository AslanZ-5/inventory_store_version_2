from asyncio import mixins
from h11 import Response
from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from store_v2.drf import serializer

from store_v2.drf.serializer import AllProducts, ProductInventorySerializer
from store_v2.inventory.models import Product, ProductInventory


class AllProductsViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):

    queryset = Product.objects.all()
    serializer_class = AllProducts
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)
        serializer = AllProducts(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
