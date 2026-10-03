
from django.urls import path

from . import views

app_name = "enquiries"

urlpatterns = [
    path(
        "enquiry/",
        views.enquiry_view,
        name="enquiry",
    ),

    path(
        "product/<slug:slug>/enquiry/",
        views.product_enquiry_view,
        name="product_enquiry",
    ),

    path(
        "contact/submit/",
        views.contact_view,
        name="contact_submit",
    ),

    path(
        "enquiry/success/",
        views.enquiry_success_view,
        name="enquiry_success",
    ),

    path(
        "contact/success/",
        views.contact_success_view,
        name="contact_success",
    ),
]