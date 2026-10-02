from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "products/",
        views.products_placeholder,
        name="products",
    ),

    path(
        "about/",
        views.about_placeholder,
        name="about",
    ),

    path(
        "contact/",
        views.contact_placeholder,
        name="contact",
    ),

    path(
        "search/",
        views.search_placeholder,
        name="search",
    ),
]