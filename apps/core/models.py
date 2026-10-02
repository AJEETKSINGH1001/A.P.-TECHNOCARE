from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteSettings(TimeStampedModel):
    """
    Global website configuration.
    Keep exactly one record in normal operation.
    """

    site_name = models.CharField(max_length=200)
    site_tagline = models.CharField(max_length=300, blank=True)

    primary_phone = models.CharField(max_length=50, blank=True)
    secondary_phone = models.CharField(max_length=50, blank=True)

    email = models.EmailField(blank=True)
    whatsapp_number = models.CharField(max_length=50, blank=True)

    address_line_1 = models.CharField(max_length=255, blank=True)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, default="India")

    google_maps_url = models.URLField(blank=True)
    business_hours = models.TextField(blank=True)

    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    footer_text = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.site_name


class CompanyProfile(TimeStampedModel):
    """
    Public company/business profile.
    All business-specific facts remain editable from admin.
    """

    display_name = models.CharField(max_length=200)
    legal_name = models.CharField(max_length=255, blank=True)

    logo = models.ImageField(
        upload_to="company/",
        blank=True,
    )

    tagline = models.CharField(max_length=300, blank=True)

    short_description = models.TextField(blank=True)
    about = models.TextField(blank=True)

    business_type = models.CharField(max_length=150, blank=True)
    year_established = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(2200),
        ],
    )

    employee_count = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    legal_status = models.CharField(max_length=150, blank=True)
    gstin = models.CharField(max_length=50, blank=True)
    iec = models.CharField(max_length=50, blank=True)

    annual_turnover = models.CharField(max_length=150, blank=True)

    service_area = models.CharField(max_length=255, blank=True)
    export_markets = models.TextField(blank=True)

    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Company Profile"
        verbose_name_plural = "Company Profile"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.display_name