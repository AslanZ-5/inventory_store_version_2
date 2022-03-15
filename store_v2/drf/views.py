from asyncio import mixins
from cgitb import lookup
from rest_framework import viewsets, permissions, mixins

from store_v2.drf.serializer import AllProducts
from store_v2.inventory.models import Product


class AllProductsViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):

    queryset = Product.objects.all()
    serializer_class = AllProducts
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"
