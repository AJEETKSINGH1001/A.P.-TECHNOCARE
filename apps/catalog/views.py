from django.core.paginator import Paginator
from django.db.models import Q, Prefetch
from django.shortcuts import get_object_or_404, render

from .models import (
    Application,
    Brand,
    Category,
    Product,
    ProductImage,
    ProductSpecification,
)


PRODUCT_LIST_PAGE_SIZE = 12


def product_queryset():
    specification_queryset = (
        ProductSpecification.objects
        .select_related("definition")
        .order_by(
            "sort_order",
            "definition__name",
        )
    )

    image_queryset = (
        ProductImage.objects
        .order_by(
            "-is_primary",
            "sort_order",
            "id",
        )
    )

    return (
        Product.objects
        .filter(is_active=True)
        .select_related(
            "category",
            "brand",
        )
        .prefetch_related(
            Prefetch(
                "images",
                queryset=image_queryset,
                to_attr="ordered_images",
            ),

            Prefetch(
                "specifications",
                queryset=specification_queryset,
                to_attr="ordered_specifications",
            ),

            "applications",
            "documents",
        )
    )


def apply_product_filters(request, queryset):
    query = request.GET.get("q", "").strip()

    category_slug = (
        request.GET.get("category", "").strip()
    )

    brand_slug = (
        request.GET.get("brand", "").strip()
    )

    application_slug = (
        request.GET.get("application", "").strip()
    )

    availability = (
        request.GET.get("availability", "").strip()
    )

    sort = (
        request.GET.get("sort", "featured").strip()
    )

    if query:
        queryset = queryset.filter(
            Q(name__icontains=query)
            | Q(sku__icontains=query)
            | Q(model_number__icontains=query)
            | Q(short_description__icontains=query)
            | Q(description__icontains=query)
            | Q(category__name__icontains=query)
            | Q(brand__name__icontains=query)
            | Q(
                specifications__value__icontains=query
            )
            | Q(
                specifications__definition__name__icontains=query
            )
        ).distinct()

    if category_slug:
        queryset = queryset.filter(
            category__slug=category_slug
        )

    if brand_slug:
        queryset = queryset.filter(
            brand__slug=brand_slug
        )

    if application_slug:
        queryset = queryset.filter(
            applications__slug=application_slug
        )

    if availability:
        queryset = queryset.filter(
            availability=availability
        )

    if sort == "name":
        queryset = queryset.order_by(
            "name",
        )

    elif sort == "price_low":
        queryset = queryset.order_by(
            "price",
            "name",
        )

    elif sort == "price_high":
        queryset = queryset.order_by(
            "-price",
            "name",
        )

    elif sort == "newest":
        queryset = queryset.order_by(
            "-created_at",
            "name",
        )

    else:
        queryset = queryset.order_by(
            "-is_featured",
            "sort_order",
            "name",
        )

    return queryset


def catalog_context(request):
    return {
        "categories": (
            Category.objects
            .filter(
                is_active=True,
                parent__isnull=True,
            )
            .order_by(
                "sort_order",
                "name",
            )
        ),

        "brands": (
            Brand.objects
            .filter(is_active=True)
            .order_by("name")
        ),

        "applications": (
            Application.objects
            .filter(is_active=True)
            .order_by("name")
        ),

        "availability_choices": (
            Product.Availability.choices
        ),

        "sort_options": [
            ("featured", "Featured"),
            ("name", "Name"),
            ("newest", "Newest"),
            ("price_low", "Price: Low to High"),
            ("price_high", "Price: High to Low"),
        ],
    }


def product_list(request):
    queryset = product_queryset()

    queryset = apply_product_filters(
        request,
        queryset,
    )

    paginator = Paginator(
        queryset,
        PRODUCT_LIST_PAGE_SIZE,
    )

    page_number = request.GET.get(
        "page",
        1,
    )

    page_obj = paginator.get_page(
        page_number,
    )

    context = {
        "page_obj": page_obj,
        "products": page_obj.object_list,
        "query": request.GET.get(
            "q",
            "",
        ).strip(),
        **catalog_context(request),
    }

    return render(
        request,
        "catalog/product_list.html",
        context,
    )


def category_products(request, slug):
    category = get_object_or_404(
        Category.objects.filter(is_active=True),
        slug=slug,
    )

    queryset = product_queryset().filter(
        category=category,
    )

    queryset = apply_product_filters(
        request,
        queryset,
    )

    paginator = Paginator(
        queryset,
        PRODUCT_LIST_PAGE_SIZE,
    )

    page_obj = paginator.get_page(
        request.GET.get("page", 1),
    )

    context = {
        "category": category,
        "page_obj": page_obj,
        "products": page_obj.object_list,
        "query": request.GET.get(
            "q",
            "",
        ).strip(),
        **catalog_context(request),
    }

    return render(
        request,
        "catalog/category_products.html",
        context,
    )


def product_search(request):
    return product_list(request)


def product_detail(request, slug):
    product = get_object_or_404(
        product_queryset(),
        slug=slug,
    )

    related_products = (
        product_queryset()
        .filter(
            category=product.category,
        )
        .exclude(
            pk=product.pk,
        )
        .order_by(
            "-is_featured",
            "sort_order",
            "name",
        )[:4]
    )

    context = {
        "product": product,
        "related_products": related_products,
    }

    return render(
        request,
        "catalog/product_detail.html",
        context,
    )