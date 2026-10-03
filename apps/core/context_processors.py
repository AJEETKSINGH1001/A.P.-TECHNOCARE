
from django.db.models import Sum
from django.utils import timezone

from apps.catalog.models import (
    Application,
    Brand,
    Category,
    Product,
)

from apps.core.models import CompanyProfile, SiteSettings

from apps.enquiries.models import (
    ContactMessage,
    Enquiry,
    Quotation,
)


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


def admin_dashboard(request):
    """Provide business statistics for the Jazzmin admin dashboard."""

    if not request.path.startswith("/admin/"):
        return {}

    today = timezone.localdate()

    return {
        # Catalog
        "dashboard_products": Product.objects.count(),
        "dashboard_active_products": Product.objects.filter(
            is_active=True
        ).count(),
        "dashboard_categories": Category.objects.count(),
        "dashboard_active_categories": Category.objects.filter(
            is_active=True
        ).count(),
        "dashboard_brands": Brand.objects.count(),
        "dashboard_active_brands": Brand.objects.filter(
            is_active=True
        ).count(),
        "dashboard_applications": Application.objects.count(),
        "dashboard_featured_products": Product.objects.filter(
            is_active=True,
            is_featured=True,
        ).count(),
        "dashboard_out_of_stock": Product.objects.filter(
            availability=Product.Availability.OUT_OF_STOCK
        ).count(),

        # Enquiries
        "dashboard_enquiries": Enquiry.objects.count(),
        "dashboard_new_enquiries": Enquiry.objects.filter(
            status=Enquiry.Status.NEW
        ).count(),
        "dashboard_qualified_enquiries": Enquiry.objects.filter(
            status=Enquiry.Status.QUALIFIED
        ).count(),
        "dashboard_quoted_enquiries": Enquiry.objects.filter(
            status=Enquiry.Status.QUOTED
        ).count(),
        "dashboard_won_enquiries": Enquiry.objects.filter(
            status=Enquiry.Status.WON
        ).count(),

        # Contact messages
        "dashboard_contact_messages": ContactMessage.objects.count(),
        "dashboard_unread_messages": ContactMessage.objects.filter(
            is_read=False
        ).count(),

        # Quotations
        "dashboard_quotations": Quotation.objects.count(),
        "dashboard_draft_quotations": Quotation.objects.filter(
            status=Quotation.Status.DRAFT
        ).count(),
        "dashboard_sent_quotations": Quotation.objects.filter(
            status=Quotation.Status.SENT
        ).count(),
        "dashboard_accepted_quotations": Quotation.objects.filter(
            status=Quotation.Status.ACCEPTED
        ).count(),
        "dashboard_quotation_value": (
            Quotation.objects.filter(
                status=Quotation.Status.ACCEPTED
            ).aggregate(
                total=Sum("grand_total")
            )["total"] or 0
        ),

        # Recent enquiries
        "dashboard_recent_enquiries": Enquiry.objects.select_related(
            "assigned_to"
        ).order_by("-created_at")[:6],

        # Today's activity
        "dashboard_today_enquiries": Enquiry.objects.filter(
            created_at__date=today
        ).count(),
        "dashboard_today_messages": ContactMessage.objects.filter(
            created_at__date=today
        ).count(),
    }