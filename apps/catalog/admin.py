import logging
import os
import tempfile
from io import StringIO

from django.contrib import admin, messages
from django.core.exceptions import PermissionDenied
from django.core.management import call_command
from django.core.management.base import CommandError
from django.db.models import Count
from django.forms.models import BaseInlineFormSet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
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


logger = logging.getLogger(__name__)


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

    change_list_template = "admin/catalog/product/change_list.html"

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

    def get_urls(self):
        custom_urls = [
            path(
                "import-csv/",
                self.admin_site.admin_view(self.import_csv_view),
                name="catalog_product_import_csv",
            ),
        ]
        return custom_urls + super().get_urls()

    def import_csv_view(self, request):
        if not (
            self.has_add_permission(request)
            or self.has_change_permission(request)
        ):
            raise PermissionDenied

        if request.method == "POST":
            uploaded_file = request.FILES.get("csv_file")

            if not uploaded_file:
                messages.error(request, "Please choose a CSV file.")
            elif not uploaded_file.name.lower().endswith(".csv"):
                messages.error(request, "Only .csv files are accepted.")
            elif uploaded_file.size == 0:
                messages.error(request, "The selected CSV file is empty.")
            else:
                temp_path = None
                output = StringIO()

                try:
                    with tempfile.NamedTemporaryFile(
                        mode="wb",
                        suffix=".csv",
                        delete=False,
                    ) as temp_file:
                        temp_path = temp_file.name
                        for chunk in uploaded_file.chunks():
                            temp_file.write(chunk)

                    # Reuse the existing management command. Its positional
                    # argument is the path to the uploaded CSV file.
                    call_command(
                        "import_products",
                        temp_path,
                        stdout=output,
                    )

                    result = output.getvalue().strip()
                    messages.success(
                        request,
                        result or "Product CSV import completed successfully.",
                    )
                    return HttpResponseRedirect(
                        reverse("admin:catalog_product_changelist")
                    )

                except CommandError as exc:
                    messages.error(request, f"CSV import failed: {exc}")
                except Exception:
                    logger.exception("Unexpected error during product CSV import")
                    messages.error(
                        request,
                        "The CSV import failed because of an unexpected error. "
                        "Check the server log for details.",
                    )
                finally:
                    if temp_path and os.path.exists(temp_path):
                        os.remove(temp_path)

        context = {
            **self.admin_site.each_context(request),
            "opts": self.model._meta,
            "title": "Bulk Product CSV Upload",
        }
        return render(
            request,
            "admin/catalog/product/import_csv.html",
            context,
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
