from rest_framework import serializers
from store_v2.inventory.models import Product


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
