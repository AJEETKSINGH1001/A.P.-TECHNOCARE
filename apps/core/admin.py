from django.contrib import admin

from .models import CompanyProfile, SiteSettings


admin.site.site_header = "Business Website Administration"
admin.site.site_title = "Business Website Admin"
admin.site.index_title = "Website Management"
admin.site.index_template = "admin/index.html"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "site_name",
        "email",
        "primary_phone",
        "is_active",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "site_name",
                    "site_tagline",
                    "footer_text",
                ),
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
                ),
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
                ),
            },
        ),
        (
            "Social Media",
            {
                "fields": (
                    "facebook_url",
                    "instagram_url",
                    "linkedin_url",
                    "youtube_url",
                ),
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_active",
                ),
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):

    list_display = (
        "display_name",
        "business_type",
        "year_established",
        "is_published",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    search_fields = (
        "display_name",
        "legal_name",
        "business_type",
        "gstin",
        "iec",
    )

    fieldsets = (
        (
            "Company Identity",
            {
                "fields": (
                    "display_name",
                    "legal_name",
                    "logo",
                    "tagline",
                ),
            },
        ),
        (
            "About",
            {
                "fields": (
                    "short_description",
                    "about",
                ),
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
                ),
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "is_published",
                ),
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),
    )

    def has_add_permission(self, request):
        return not CompanyProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False