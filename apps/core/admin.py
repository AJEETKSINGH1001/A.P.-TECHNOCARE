from django.contrib import admin

from .models import CompanyProfile, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "site_name",
                    "site_tagline",
                    "footer_text",
                )
            },
        ),
        (
            "Contact",
            {
                "fields": (
                    "primary_phone",
                    "secondary_phone",
                    "email",
                    "whatsapp_number",
                )
            },
        ),
        (
            "Address",
            {
                "fields": (
                    "address_line_1",
                    "address_line_2",
                    "city",
                    "state",
                    "postal_code",
                    "country",
                    "google_maps_url",
                    "business_hours",
                )
            },
        ),
        (
            "Social",
            {
                "fields": (
                    "facebook_url",
                    "instagram_url",
                    "linkedin_url",
                    "youtube_url",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Company Identity",
            {
                "fields": (
                    "display_name",
                    "legal_name",
                    "logo",
                    "tagline",
                )
            },
        ),
        (
            "About",
            {
                "fields": (
                    "short_description",
                    "about",
                )
            },
        ),
        (
            "Business Information",
            {
                "fields": (
                    "business_type",
                    "year_established",
                    "employee_count",
                    "legal_status",
                    "gstin",
                    "iec",
                    "annual_turnover",
                    "service_area",
                    "export_markets",
                )
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "is_published",
                )
            },
        ),
    )