from django.contrib import admin

from .models import Redirect, SEOMetadata


@admin.register(SEOMetadata)
class SEOMetadataAdmin(admin.ModelAdmin):
    list_display = (
        "content_type",
        "object_id",
        "meta_title",
        "robots_index",
        "robots_follow",
    )

    list_filter = (
        "content_type",
        "robots_index",
        "robots_follow",
    )

    search_fields = (
        "meta_title",
        "meta_description",
        "canonical_url",
    )


@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    list_display = (
        "old_path",
        "new_path",
        "redirect_type",
        "is_active",
    )

    list_filter = (
        "redirect_type",
        "is_active",
    )

    search_fields = (
        "old_path",
        "new_path",
    )