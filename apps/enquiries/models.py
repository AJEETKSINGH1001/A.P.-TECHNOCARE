from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


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
    company_name = models.CharField(
        max_length=255,
        blank=True,
    )

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

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    user_agent = models.TextField(blank=True)

    referrer = models.URLField(
        blank=True,
    )

    utm_source = models.CharField(
        max_length=150,
        blank=True,
    )

    utm_medium = models.CharField(
        max_length=150,
        blank=True,
    )

    utm_campaign = models.CharField(
        max_length=150,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=["status", "-created_at"],
                name="enq_status_created_idx",
            ),
            models.Index(
                fields=["phone"],
                name="enq_phone_idx",
            ),
            models.Index(
                fields=["email"],
                name="enq_email_idx",
            ),
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

    unit = models.CharField(
        max_length=50,
        blank=True,
    )

    customer_note = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.enquiry} - {self.product.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)

    company_name = models.CharField(
        max_length=255,
        blank=True,
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=50,
        blank=True,
    )

    subject = models.CharField(
        max_length=255,
        blank=True,
    )

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