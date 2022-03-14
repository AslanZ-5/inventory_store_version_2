from django.shortcuts import render
from store_v2.inventory import models
from django.db.models import Count


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
    filter_values = []
    if request.GET:
        for i in request.GET.values():
            filter_values.append(i)

    data = (
        models.ProductInventory.objects.filter(product__slug=slug)
        .filter(attribute_values__attribute_value__in=filter_values)
        .annotate(num_tags=Count("attribute_values"))
        .filter(num_tags=len(filter_values))
        .values(
            "id",
            "product__name",
            "sku",
            "store_price",
            "product_inventory__units",
        )
    )
    z = (
        models.ProductTypeAttribute.objects.filter(
            product_type__product_type__product__slug=slug
        )
        .values("product_attribute__name")
        .distinct()
    )

    return render(request, "product_detail.html", {"data": data, "z": z})
