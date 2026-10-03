from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.home,
        name="home",
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
        "privacy-policy/",
        views.privacy_policy,
        name="privacy_policy",
    ),

    path(
         "terms/",
         views.terms_conditions,
         name="terms",
),
    path(
         "about/",
         views.about_placeholder,
         name="about",
),

]