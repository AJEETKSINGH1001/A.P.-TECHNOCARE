from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class SEOMetadata(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )

    object_id = models.PositiveBigIntegerField(
        db_index=True,
    )

    content_object = GenericForeignKey(
        "content_type",
        "object_id",
    )

    meta_title = models.CharField(
        max_length=255,
        blank=True,
    )

    meta_description = models.CharField(
        max_length=320,
        blank=True,
    )

    canonical_url = models.URLField(
        blank=True,
    )

    og_title = models.CharField(
        max_length=255,
        blank=True,
    )

    og_description = models.CharField(
        max_length=320,
        blank=True,
    )

    og_image = models.ImageField(
        upload_to="seo/",
        blank=True,
    )

    robots_index = models.BooleanField(default=True)
    robots_follow = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["content_type", "object_id"],
                name="unique_seo_target",
            ),
        ]
        indexes = [
            models.Index(
                fields=["content_type", "object_id"],
                name="seo_content_object_idx",
            ),
        ]

    def __str__(self):
        return self.meta_title or "SEO metadata"


class Redirect(models.Model):

    class RedirectType(models.IntegerChoices):
        PERMANENT = 301, "301 Permanent"
        TEMPORARY = 302, "302 Temporary"

    old_path = models.CharField(
        max_length=500,
        unique=True,
    )

    new_path = models.CharField(
        max_length=500,
    )

    redirect_type = models.PositiveSmallIntegerField(
        choices=RedirectType.choices,
        default=RedirectType.PERMANENT,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.old_path} → {self.new_path}"