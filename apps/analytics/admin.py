from django.contrib import admin

from .models import AnalyticsEvent


@admin.register(AnalyticsEvent)
class AnalyticsEventAdmin(admin.ModelAdmin):
    list_display = (
        "event_name",
        "event_category",
        "page_path",
        "created_at",
    )

    list_filter = (
        "event_name",
        "event_category",
        "created_at",
    )

    search_fields = (
        "event_name",
        "page_path",
    )

    readonly_fields = (
        "created_at",
    )