from django.contrib import admin
from django.db.models import Count
from django.forms.models import BaseInlineFormSet
from django.utils.html import format_html

from .models import (
    Application,
    Brand,
    Category,
    Product,
    ProductDocument,
    ProductImage,
    ProductSpecification,
    ProductSpecificationDefinition,
)


# =============================================================================
# Category
# =============================================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
        "product_count",
        "is_active",
        "is_featured",
        "sort_order",
    )

    list_filter = (
        "is_active",
        "is_featured",
        "parent",
    )

    search_fields = (
        "name",
        "slug",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    list_editable = (
        "is_active",
        "is_featured",
        "sort_order",
    )

    ordering = (
        "sort_order",
        "name",
    )

    list_per_page = 50

    @admin.display(
        description="Products",
        ordering="product_count",
    )
    def product_count(self, obj):
        return obj.product_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        return queryset.annotate(
            product_count=Count(
                "products",
                distinct=True,
            )
        )


# =============================================================================
# Brand
# =============================================================================

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "product_count",
        "is_active",
        "is_featured",
    )

    list_filter = (
        "is_active",
        "is_featured",
    )

    search_fields = (
        "name",
        "slug",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    list_editable = (
        "is_active",
        "is_featured",
    )

    list_per_page = 50

    @admin.display(
        description="Products",
        ordering="product_count",
    )
    def product_count(self, obj):
        return obj.product_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count(
                "products",
                distinct=True,
            )
        )


# =============================================================================
# Application
# =============================================================================

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    list_editable = (
        "is_active",
    )


# =============================================================================
# Product image formset
# =============================================================================

class ProductImageInlineFormSet(BaseInlineFormSet):

    def clean(self):
        super().clean()

        primary_count = 0

        for form in self.forms:
            if not hasattr(form, "cleaned_data"):
                continue

            if not form.cleaned_data:
                continue

            if form.cleaned_data.get("DELETE"):
                continue

            if form.cleaned_data.get("is_primary"):
                primary_count += 1

        if primary_count > 1:
            from django.core.exceptions import ValidationError

            raise ValidationError(
                "A product can have only one primary image."
            )


# =============================================================================
# Product image
# =============================================================================

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    formset = ProductImageInlineFormSet

    extra = 1

    fields = (
        "image",
        "preview",
        "alt_text",
        "title",
        "sort_order",
        "is_primary",
    )

    readonly_fields = (
        "preview",
    )

    ordering = (
        "sort_order",
        "id",
    )

    @admin.display(description="Preview")
    def preview(self, obj):
        if not obj.image:
            return "No image"

        return format_html(
            '<img src="{}" width="100" height="100" '
            'style="object-fit: contain; border: 1px solid #ddd;" />',
            obj.image.url,
        )


# =============================================================================
# Product specification
# =============================================================================

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification

    extra = 1

    fields = (
        "definition",
        "value",
        "sort_order",
    )

    autocomplete_fields = (
        "definition",
    )


# =============================================================================
# Product document
# =============================================================================

class ProductDocumentInline(admin.TabularInline):
    model = ProductDocument

    extra = 0

    fields = (
        "title",
        "document_type",
        "file",
        "sort_order",
        "is_public",
    )


# =============================================================================
# Product
# =============================================================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "brand",
        "price_display",
        "availability",
        "is_featured",
        "is_active",
        "image_count",
    )

    list_filter = (
        "category",
        "brand",
        "availability",
        "price_visibility",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "name",
        "sku",
        "model_number",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    autocomplete_fields = (
        "category",
        "brand",
        "applications",
    )

    filter_horizontal = (
        "applications",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        ProductImageInline,
        ProductSpecificationInline,
        ProductDocumentInline,
    ]

    list_per_page = 50

    save_on_top = True

    actions = [
        "publish_products",
        "unpublish_products",
        "feature_products",
        "unfeature_products",
    ]

    fieldsets = (
        (
            "Product Identity",
            {
                "fields": (
                    "name",
                    "slug",
                    "sku",
                    "model_number",
                ),
            },
        ),
        (
            "Classification",
            {
                "fields": (
                    "category",
                    "brand",
                    "applications",
                ),
            },
        ),
        (
            "Description",
            {
                "fields": (
                    "short_description",
                    "description",
                ),
            },
        ),
        (
            "Pricing",
            {
                "fields": (
                    "price",
                    "price_visibility",
                    "currency",
                    "minimum_order_quantity",
                    "unit",
                    "packaging_details",
                ),
            },
        ),
        (
            "Availability",
            {
                "fields": (
                    "availability",
                ),
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "is_featured",
                    "is_active",
                    "sort_order",
                ),
            },
        ),
        (
            "SEO",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
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

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related(
                "category",
                "brand",
            )
            .annotate(
                image_count_value=Count(
                    "images",
                    distinct=True,
                )
            )
        )

    @admin.display(description="Price")
    def price_display(self, obj):
        if obj.price is None:
            return "On Request"

        return f"{obj.currency} {obj.price:,.2f}"

    @admin.display(
        description="Images",
        ordering="image_count_value",
    )
    def image_count(self, obj):
        return obj.image_count_value

    @admin.action(description="Publish selected products")
    def publish_products(self, request, queryset):
        updated = queryset.update(
            is_active=True,
        )

        self.message_user(
            request,
            f"{updated} product(s) published.",
        )

    @admin.action(description="Unpublish selected products")
    def unpublish_products(self, request, queryset):
        updated = queryset.update(
            is_active=False,
        )

        self.message_user(
            request,
            f"{updated} product(s) unpublished.",
        )

    @admin.action(description="Mark selected products as featured")
    def feature_products(self, request, queryset):
        updated = queryset.update(
            is_featured=True,
        )

        self.message_user(
            request,
            f"{updated} product(s) marked as featured.",
        )

    @admin.action(description="Remove selected products from featured")
    def unfeature_products(self, request, queryset):
        updated = queryset.update(
            is_featured=False,
        )

        self.message_user(
            request,
            f"{updated} product(s) removed from featured.",
        )


# =============================================================================
# Specification definitions
# =============================================================================

@admin.register(ProductSpecificationDefinition)
class ProductSpecificationDefinitionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "unit",
        "sort_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    list_editable = (
        "sort_order",
        "is_active",
    )