from django.contrib import admin

from .models import FAQ, StaticPage, Testimonial


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "is_published",
        "published_at",
    )

    list_filter = (
        "is_published",
    )

    search_fields = (
        "title",
        "slug",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "company_name",
        "rating",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "rating",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "customer_name",
        "company_name",
        "message",
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "sort_order",
        "is_published",
    )

    list_filter = (
        "is_published",
    )

    search_fields = (
        "question",
        "answer",
    )