from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)

    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
    )

    sort_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=320, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "name"]
        indexes = [
            models.Index(
                fields=["is_active", "sort_order"],
                name="cat_active_order_idx",
            ),
            models.Index(
                fields=["parent", "is_active"],
                name="cat_parent_active_idx",
            ),
        ]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)

    logo = models.ImageField(
        upload_to="brands/",
        blank=True,
    )

    website = models.URLField(blank=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):

    class Availability(models.TextChoices):
        IN_STOCK = "in_stock", "In Stock"
        AVAILABLE = "available", "Available"
        MADE_TO_ORDER = "made_to_order", "Made to Order"
        ON_REQUEST = "on_request", "On Request"
        OUT_OF_STOCK = "out_of_stock", "Out of Stock"

    class PriceVisibility(models.TextChoices):
        SHOW = "show", "Show Price"
        HIDE = "hide", "Hide Price"
        QUOTE = "quote", "Get Quote"

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True)

    sku = models.CharField(
        max_length=100,
        blank=True,
        db_index=True,
    )

    model_number = models.CharField(
        max_length=150,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="products",
        null=True,
        blank=True,
    )

    applications = models.ManyToManyField(
        Application,
        blank=True,
        related_name="products",
    )

    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
    )

    price_visibility = models.CharField(
        max_length=20,
        choices=PriceVisibility.choices,
        default=PriceVisibility.QUOTE,
    )

    currency = models.CharField(
        max_length=10,
        default="INR",
    )

    minimum_order_quantity = models.DecimalField(
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

    packaging_details = models.CharField(
        max_length=255,
        blank=True,
    )

    availability = models.CharField(
        max_length=30,
        choices=Availability.choices,
        default=Availability.ON_REQUEST,
    )

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    sort_order = models.PositiveIntegerField(default=0)

    meta_title = models.CharField(
        max_length=255,
        blank=True,
    )

    meta_description = models.CharField(
        max_length=320,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "name"]
        indexes = [
            models.Index(
                fields=["is_active", "is_featured", "sort_order"],
                name="prd_active_featured_idx",
            ),
            models.Index(
                fields=["category", "is_active"],
                name="prd_category_active_idx",
            ),
            models.Index(
                fields=["brand", "is_active"],
                name="prd_brand_active_idx",
            ),
            models.Index(
                fields=["name"],
                name="prd_name_idx",
            ),
        ]

    def __str__(self):
        return self.name


class ProductSpecificationDefinition(models.Model):
    """
    Defines specification labels such as:
    Diameter, Process, AWS Grade, Packaging Size, etc.
    """

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, unique=True)

    unit = models.CharField(
        max_length=50,
        blank=True,
    )

    sort_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="specifications",
    )

    definition = models.ForeignKey(
        ProductSpecificationDefinition,
        on_delete=models.PROTECT,
        related_name="values",
    )

    value = models.CharField(max_length=500)

    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "definition__name"]
        constraints = [
            models.UniqueConstraint(
                fields=["product", "definition"],
                name="unique_product_specification",
            ),
        ]
        indexes = [
            models.Index(
                fields=["product", "sort_order"],
                name="prd_spec_product_order_idx",
            ),
        ]

    def __str__(self):
        return f"{self.product.name} - {self.definition.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="products/%Y/%m/",
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
    )

    title = models.CharField(
        max_length=255,
        blank=True,
    )

    sort_order = models.PositiveIntegerField(default=0)

    is_primary = models.BooleanField(default=False)

    width = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    height = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "id"]
        indexes = [
            models.Index(
                fields=["product", "is_primary", "sort_order"],
                name="prd_img_primary_idx",
            ),
        ]

    def __str__(self):
        return f"{self.product.name} image"


class ProductDocument(models.Model):

    class DocumentType(models.TextChoices):
        DATASHEET = "datasheet", "Datasheet"
        CATALOG = "catalog", "Catalog"
        MANUAL = "manual", "Manual"
        CERTIFICATE = "certificate", "Certificate"
        OTHER = "other", "Other"

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    title = models.CharField(max_length=255)

    file = models.FileField(
        upload_to="product-documents/%Y/%m/",
    )

    document_type = models.CharField(
        max_length=30,
        choices=DocumentType.choices,
        default=DocumentType.OTHER,
    )

    sort_order = models.PositiveIntegerField(default=0)

    is_public = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "title"]

    def __str__(self):
        return self.title