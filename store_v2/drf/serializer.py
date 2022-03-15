from rest_framework import serializers
from store_v2.inventory.models import Product, ProductInventory


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = "__all__"
        read_only = True
        depth = 4
