from django.shortcuts import render
from store_v2.inventory import models


def home(request):
    return render(request, "index.html")


def category(request):
    data = models.Category.objects.all()
    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):
    data = models.Product.objects.filter(category__name=category).values(
        "id", "name", "slug", "category__name", "product__store_price"
    )

    return render(request, "product_by_category.html", {"data": data})


def product_detail(request, slug):
    data = models.ProductInventory.objects.filter(product__slug=slug).values(
        "id",
        "product__name",
        "sku",
        "store_price",
        "product_inventory__units",
    )
    print(data)
    return render(request, "product_detail.html", {"data": data})
