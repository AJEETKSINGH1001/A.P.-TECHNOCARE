from django.db import models


class AnalyticsEvent(models.Model):

    event_name = models.CharField(
        max_length=100,
    )

    event_category = models.CharField(
        max_length=100,
        blank=True,
    )

    page_path = models.CharField(
        max_length=1000,
        blank=True,
    )

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="analytics_events",
    )

    category = models.ForeignKey(
        "catalog.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="analytics_events",
    )

    referrer = models.URLField(blank=True)

    metadata = models.JSONField(
        default=dict,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=["event_name", "-created_at"],
                name="analytics_event_time_idx",
            ),
            models.Index(
                fields=["page_path"],
                name="analytics_page_idx",
            ),
        ]

    def __str__(self):
        return self.event_name