from django.contrib import admin

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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
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
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    ordering = (
        "sort_order",
        "name",
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
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
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


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
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductDocumentInline(admin.TabularInline):
    model = ProductDocument
    extra = 0


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "brand",
        "price",
        "price_visibility",
        "availability",
        "is_featured",
        "is_active",
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
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

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

    ordering = (
        "sort_order",
        "name",
    )


@admin.register(ProductSpecificationDefinition)
class ProductSpecificationDefinitionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "unit",
        "is_active",
        "sort_order",
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