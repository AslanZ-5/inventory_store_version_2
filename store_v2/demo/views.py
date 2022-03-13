from django.shortcuts import render
from store_v2.inventory import models


def home(request):
    return render(request, "index.html")


def category(request):
    data = models.Category.objects.all()
    print(data)
    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):
    data = models.Product.objects.filter(category__name=category).values(
        "id", "name", "category__name", "product__store_price"
    )
    print(data)
    return render(request, "product_by_category.html", {"data": data})
