from django.shortcuts import render
from store_v2.inventory import models


def home(request):
    return render(request, "index.html")


def category(request):
    data = models.Category.objects.all()
    print(data)
    return render(request, "categories.html", {"data": data})
