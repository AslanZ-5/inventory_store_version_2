from os import read
from rest_framework import serializers
from store_v2.inventory.models import Product


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]
        read_only = True
        editable = False
