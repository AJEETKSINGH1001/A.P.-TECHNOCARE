
from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from apps.catalog.models import Product

from .forms import (
    EnquiryForm,
    ProductEnquiryForm,
    ContactMessageForm,
)
from .models import Enquiry, EnquiryItem


def enquiry_view(request):
    """Handle general customer enquiries."""

    if request.method == "POST":
        form = EnquiryForm(request.POST)

        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.source = Enquiry.Source.WEBSITE
            enquiry.save()

            messages.success(
                request,
                "Thank you! Your enquiry has been submitted successfully."
            )
            return redirect("enquiries:enquiry_success")

    else:
        form = EnquiryForm()

    return render(
        request,
        "enquiries/enquiry_form.html",
        {"form": form},
    )


def product_enquiry_view(request, slug):
    """Handle enquiries for a specific product."""

    product = get_object_or_404(
        Product,
        slug=slug,
        is_active=True,
    )

    if request.method == "POST":
        form = ProductEnquiryForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            with transaction.atomic():
                enquiry = Enquiry.objects.create(
                    name=data["customer_name"],
                    company_name=data["company_name"],
                    phone=data["phone"],
                    email=data["email"],
                    message=data["message"],
                    source=Enquiry.Source.PRODUCT_PAGE,
                )

                quantity = data["quantity"]

                if quantity and quantity > 0:
                    EnquiryItem.objects.create(
                        enquiry=enquiry,
                        product=product,
                        quantity=quantity,
                        unit=getattr(product, "unit", "") or "",
                        customer_note=data["message"],
                    )

            messages.success(
                request,
                "Your product enquiry has been submitted successfully."
            )

            return redirect("enquiries:enquiry_success")

    else:
        form = ProductEnquiryForm()

    return render(
        request,
        "enquiries/product_enquiry.html",
        {
            "form": form,
            "product": product,
        },
    )


def contact_view(request):
    """Handle website contact messages."""

    if request.method == "POST":
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Thank you! Your message has been sent successfully."
            )

            return redirect("enquiries:contact_success")

    else:
        form = ContactMessageForm()

    return render(
        request,
        "enquiries/contact_form.html",
        {"form": form},
    )


def enquiry_success_view(request):
    return render(
        request,
        "enquiries/success.html",
        {"title": "Enquiry Submitted"},
    )


def contact_success_view(request):
    return render(
        request,
        "enquiries/success.html",
        {"title": "Message Sent"},
    )