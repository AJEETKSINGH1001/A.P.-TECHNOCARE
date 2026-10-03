from django.urls import path

from . import views


urlpatterns = [
    path(
        "products/",
        views.product_list,
        name="products",
    ),

    path(
        "products/category/<slug:slug>/",
        views.category_products,
        name="category_products",
    ),

    path(
        "products/<slug:slug>/",
        views.product_detail,
        name="product_detail",
    ),

    path(
        "search/",
        views.product_search,
        name="search",
    ),
]