import uuid

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


def generate_quotation_reference():
    """
    Generate a unique quotation reference.

    Example:
    QTN-20261003-A1B2C3D4
    """
    date_part = timezone.localdate().strftime("%Y%m%d")
    random_part = uuid.uuid4().hex[:8].upper()
    return f"QTN-{date_part}-{random_part}"


class Enquiry(models.Model):

    class Status(models.TextChoices):
        NEW = "new", "New"
        CONTACTED = "contacted", "Contacted"
        QUALIFIED = "qualified", "Qualified"
        QUOTED = "quoted", "Quoted"
        WON = "won", "Won"
        LOST = "lost", "Lost"
        SPAM = "spam", "Spam"
        CLOSED = "closed", "Closed"

    class Source(models.TextChoices):
        WEBSITE = "website", "Website"
        PRODUCT_PAGE = "product_page", "Product Page"
        HOMEPAGE = "homepage", "Homepage"
        CONTACT_PAGE = "contact_page", "Contact Page"
        WHATSAPP = "whatsapp", "WhatsApp"
        PHONE = "phone", "Phone"
        OTHER = "other", "Other"

    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)

    source = models.CharField(
        max_length=30,
        choices=Source.choices,
        default=Source.WEBSITE,
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.NEW,
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_enquiries",
    )

    notes = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    referrer = models.URLField(blank=True)
    utm_source = models.CharField(max_length=150, blank=True)
    utm_medium = models.CharField(max_length=150, blank=True)
    utm_campaign = models.CharField(max_length=150, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=["status", "-created_at"],
                name="enq_status_created_idx",
            ),
            models.Index(fields=["phone"], name="enq_phone_idx"),
            models.Index(fields=["email"], name="enq_email_idx"),
        ]

    def __str__(self):
        return f"{self.name} - {self.status}"


class EnquiryItem(models.Model):
    enquiry = models.ForeignKey(
        Enquiry,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.PROTECT,
        related_name="enquiry_items",
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
    )

    unit = models.CharField(max_length=50, blank=True)
    customer_note = models.TextField(blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.enquiry} - {self.product.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=["is_read", "-created_at"],
                name="contact_read_created_idx",
            ),
        ]

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Quotation(models.Model):

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SENT = "sent", "Sent"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"
        EXPIRED = "expired", "Expired"
        CANCELLED = "cancelled", "Cancelled"

    class SupplyType(models.TextChoices):
        INTRA_STATE = "intra_state", "Intra-state"
        INTER_STATE = "inter_state", "Inter-state"

    reference = models.CharField(
        max_length=40,
        unique=True,
        default=generate_quotation_reference,
        editable=False,
    )

    enquiry = models.ForeignKey(
        Enquiry,
        on_delete=models.PROTECT,
        related_name="quotations",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    currency = models.CharField(max_length=10, default="INR")

    # Customer details snapshot
    customer_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=255, blank=True)
    customer_email = models.EmailField(blank=True)
    customer_phone = models.CharField(max_length=50)
    billing_address = models.TextField(blank=True)
    shipping_address = models.TextField(blank=True)
    customer_gstin = models.CharField(max_length=15, blank=True)

    # GST information
    supply_type = models.CharField(
        max_length=20,
        choices=SupplyType.choices,
        default=SupplyType.INTRA_STATE,
    )
    place_of_supply = models.CharField(max_length=100, blank=True)

    # Financial calculations
    subtotal = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    discount_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    taxable_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    cgst_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    sgst_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    igst_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    grand_total = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )

    # Quotation validity and communication
    issue_date = models.DateField(default=timezone.localdate)
    valid_until = models.DateField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    terms = models.TextField(blank=True)
    internal_notes = models.TextField(blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_quotations",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=["status", "-created_at"],
                name="quote_status_created_idx",
            ),
            models.Index(
                fields=["enquiry", "-created_at"],
                name="quote_enquiry_created_idx",
            ),
        ]

    def __str__(self):
        return self.reference


class QuotationItem(models.Model):
    quotation = models.ForeignKey(
        Quotation,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.PROTECT,
        related_name="quotation_items",
    )

    # Product snapshots
    description = models.CharField(max_length=500)
    sku = models.CharField(max_length=100, blank=True)

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        validators=[MinValueValidator(0.001)],
    )

    unit = models.CharField(max_length=50, blank=True)

    # Negotiated pricing
    unit_price = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    # Configurable GST rate
    gst_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
    )

    # Calculated amounts
    taxable_value = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    cgst_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    sgst_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    igst_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    line_total = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.quotation.reference} - {self.description}"
