from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class StaticPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True)

    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)

    featured_image = models.ImageField(
        upload_to="pages/",
        blank=True,
    )

    is_published = models.BooleanField(default=True)

    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=320, blank=True)

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    customer_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=255, blank=True)

    designation = models.CharField(
        max_length=150,
        blank=True,
    )

    message = models.TextField()

    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )

    image = models.ImageField(
        upload_to="testimonials/",
        blank=True,
    )

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return self.customer_name


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    sort_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "question"]

    def __str__(self):
        return self.question