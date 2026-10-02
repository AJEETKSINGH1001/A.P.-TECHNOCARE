from apps.catalog.models import Category
from apps.core.models import CompanyProfile, SiteSettings


def site_context(request):
    site_settings = (
        SiteSettings.objects
        .filter(is_active=True)
        .first()
    )

    company_profile = (
        CompanyProfile.objects
        .filter(is_published=True)
        .first()
    )

    navigation_categories = (
        Category.objects
        .filter(
            parent__isnull=True,
            is_active=True,
        )
        .order_by(
            "sort_order",
            "name",
        )[:8]
    )

    return {
        "site_settings": site_settings,
        "company_profile": company_profile,
        "navigation_categories": navigation_categories,
    }