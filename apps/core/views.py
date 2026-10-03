
from django.shortcuts import render

from apps.content.models import Testimonial
from apps.catalog.models import Category


def home(request):
    navigation_categories = Category.objects.filter(
        is_active=True,
        parent__isnull=True,
    ).order_by("sort_order", "name")[:8]

    testimonials = Testimonial.objects.filter(
        is_published=True,
    ).order_by("sort_order", "-created_at")

    context = {
        "navigation_categories": navigation_categories,
        "testimonials": testimonials,
    }

    return render(
        request,
        "core/home.html",
        context,
    )


def products_placeholder(request):
    return render(
        request,
        "core/placeholder.html",
        {
            "page_title": "Products",
            "page_description": (
                "Our product catalogue is being prepared."
            ),
        },
    )


from .models import CompanyProfile


def about_placeholder(request):
    company_profile = CompanyProfile.objects.filter(
        is_published=True
    ).first()

    return render(
        request,
        "core/about.html",
        {
            "company_profile": company_profile,
        },
    )


def contact_placeholder(request):
    return render(
        request,
        "core/placeholder.html",
        {
            "page_title": "Contact Us",
            "page_description": (
                "The enquiry and contact workflow will be "
                "implemented in the next phase."
            ),
        },
    )
def privacy_policy(request):
    return render(
        request,
        "core/privacy_policy.html",
    )

def terms_conditions(request):
    return render(
        request,
        "core/terms_conditions.html",
    )

def search_placeholder(request):
    query = request.GET.get("q", "").strip()

    return render(
        request,
        "core/placeholder.html",
        {
            "page_title": "Search",
            "page_description": (
                f'Search results for "{query}"'
                if query
                else "Search products and services."
            ),
        },
    )