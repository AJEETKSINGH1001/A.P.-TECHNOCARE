from django.contrib import admin

from .models import ContactMessage, Enquiry, EnquiryItem


class EnquiryItemInline(admin.TabularInline):
    model = EnquiryItem

    extra = 0

    autocomplete_fields = (
        "product",
    )

    fields = (
        "product",
        "quantity",
        "unit",
        "customer_note",
    )


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
        "assigned_to",
        "created_at",
    )

    search_fields = (
        "name",
        "company_name",
        "phone",
        "email",
        "message",
    )

    autocomplete_fields = (
        "assigned_to",
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

    date_hierarchy = "created_at"

    list_per_page = 50

    save_on_top = True

    fieldsets = (
        (
            "Customer",
            {
                "fields": (
                    "name",
                    "company_name",
                    "phone",
                    "email",
                ),
            },
        ),
        (
            "Enquiry",
            {
                "fields": (
                    "message",
                    "source",
                    "status",
                    "assigned_to",
                    "notes",
                ),
            },
        ),
        (
            "Marketing Attribution",
            {
                "fields": (
                    "utm_source",
                    "utm_medium",
                    "utm_campaign",
                    "referrer",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),
        (
            "Technical",
            {
                "fields": (
                    "ip_address",
                    "user_agent",
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),
    )


from django.contrib import admin
from .models import Quotation


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "enquiry",
        "status",
        "currency",
        "grand_total",
        "issue_date",
        "valid_until",
    )
    list_filter = ("status", "currency", "issue_date")
    search_fields = (
        "reference",
        "customer_name",
        "customer_email",
    )
    ordering = ("-created_at",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "company_name",
        "email",
        "phone",
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
        "company_name",
        "email",
        "phone",
        "subject",
        "message",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "created_at",
    )

    date_hierarchy = "created_at"

    list_per_page = 50