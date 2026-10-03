
from django.shortcuts import render

from .models import Testimonial
from apps.catalog.models import Category


def home(request):
    navigation_categories = Category.objects.filter(
        is_active=True,
        parent__isnull=True,
    ).order_by("sort_order", "name")[:8]

    testimonials = Testimonial.objects.filter(
        is_published=True,
        is_featured=True,
    ).order_by("sort_order", "-created_at")

    context = {
        "navigation_categories": navigation_categories,
        "testimonials": testimonials,
    }

    return render(request, "home.html", context)