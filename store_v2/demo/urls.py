from django.urls import path, include
from . import views

app_name = "demo"

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.category, name="categories"),
]
