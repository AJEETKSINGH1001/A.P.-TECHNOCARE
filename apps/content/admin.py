from django.contrib import admin

from .models import FAQ, StaticPage, Testimonial


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "slug",
        "is_published",
        "published_at",
        "updated_at",
    )

    list_filter = (
        "is_published",
        "published_at",
    )

    search_fields = (
        "title",
        "slug",
        "excerpt",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    date_hierarchy = "published_at"

    save_on_top = True


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "company_name",
        "rating",
        "is_featured",
        "is_published",
        "sort_order",
    )

    list_filter = (
        "rating",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "customer_name",
        "company_name",
        "designation",
        "message",
    )

    list_editable = (
        "rating",
        "is_featured",
        "is_published",
        "sort_order",
    )

    list_per_page = 50


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):

    list_display = (
        "question",
        "sort_order",
        "is_published",
        "updated_at",
    )

    list_filter = (
        "is_published",
    )

    search_fields = (
        "question",
        "answer",
    )

    list_editable = (
        "sort_order",
        "is_published",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )