from django.contrib import admin

from .models import ContactMessage, Enquiry, EnquiryItem


class EnquiryItemInline(admin.TabularInline):
    model = EnquiryItem
    extra = 0


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company_name",
        "phone",
        "email",
        "status",
        "source",
        "assigned_to",
        "created_at",
    )

    list_filter = (
        "status",
        "source",
        "created_at",
    )

    search_fields = (
        "name",
        "company_name",
        "phone",
        "email",
        "message",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "ip_address",
        "user_agent",
        "referrer",
    )

    inlines = [
        EnquiryItemInline,
    ]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    readonly_fields = (
        "created_at",
    )