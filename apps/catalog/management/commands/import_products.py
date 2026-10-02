import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.text import slugify

from apps.catalog.models import (
    Brand,
    Category,
    Product,
    ProductSpecification,
    ProductSpecificationDefinition,
)


TRUE_VALUES = {
    "1",
    "true",
    "yes",
    "y",
}


class Command(BaseCommand):

    help = "Import products from a CSV file."

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
        )

        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Validate the CSV without saving changes.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file = Path(options["csv_file"])
        dry_run = options["dry_run"]

        if not csv_file.exists():
            raise CommandError(
                f"CSV file does not exist: {csv_file}"
            )

        if csv_file.suffix.lower() != ".csv":
            raise CommandError(
                "Input file must be a .csv file."
            )

        created_count = 0
        updated_count = 0
        specification_count = 0

        with csv_file.open(
            "r",
            encoding="utf-8-sig",
            newline="",
        ) as file:

            reader = csv.DictReader(file)

            if not reader.fieldnames:
                raise CommandError(
                    "CSV file does not contain a header."
                )

            required_fields = {
                "name",
                "category",
            }

            missing_fields = (
                required_fields
                - set(reader.fieldnames)
            )

            if missing_fields:
                raise CommandError(
                    "Missing required columns: "
                    + ", ".join(sorted(missing_fields))
                )

            for row_number, row in enumerate(
                reader,
                start=2,
            ):
                name = (
                    row.get("name") or ""
                ).strip()

                if not name:
                    raise CommandError(
                        f"Row {row_number}: name is required."
                    )

                category_name = (
                    row.get("category") or ""
                ).strip()

                if not category_name:
                    raise CommandError(
                        f"Row {row_number}: category is required."
                    )

                category_slug = slugify(
                    category_name
                )

                category, _ = (
                    Category.objects.get_or_create(
                        slug=category_slug,
                        defaults={
                            "name": category_name,
                        },
                    )
                )

                brand = None

                brand_name = (
                    row.get("brand") or ""
                ).strip()

                if brand_name:
                    brand_slug = slugify(
                        brand_name
                    )

                    brand, _ = (
                        Brand.objects.get_or_create(
                            slug=brand_slug,
                            defaults={
                                "name": brand_name,
                            },
                        )
                    )

                sku = (
                    row.get("sku") or ""
                ).strip()

                model_number = (
                    row.get("model_number") or ""
                ).strip()

                slug_value = slugify(name)

                price = self.parse_decimal(
                    row.get("price"),
                    row_number,
                    "price",
                )

                minimum_order_quantity = (
                    self.parse_decimal(
                        row.get("minimum_order_quantity"),
                        row_number,
                        "minimum_order_quantity",
                    )
                )

                defaults = {
                    "name": name,
                    "slug": slug_value,
                    "model_number": model_number,
                    "category": category,
                    "brand": brand,
                    "short_description": (
                        row.get("short_description")
                        or ""
                    ).strip(),
                    "description": (
                        row.get("description")
                        or ""
                    ).strip(),
                    "price": price,
                    "price_visibility": (
                        row.get("price_visibility")
                        or "quote"
                    ).strip().lower(),
                    "currency": (
                        row.get("currency")
                        or "INR"
                    ).strip().upper(),
                    "minimum_order_quantity": (
                        minimum_order_quantity
                    ),
                    "unit": (
                        row.get("unit")
                        or ""
                    ).strip(),
                    "packaging_details": (
                        row.get("packaging_details")
                        or ""
                    ).strip(),
                    "availability": (
                        row.get("availability")
                        or "on_request"
                    ).strip().lower(),
                    "is_featured": self.parse_bool(
                        row.get("is_featured")
                    ),
                    "is_active": self.parse_bool(
                        row.get("is_active"),
                        default=True,
                    ),
                    "sort_order": self.parse_int(
                        row.get("sort_order"),
                        row_number,
                        "sort_order",
                        default=0,
                    ),
                    "meta_title": (
                        row.get("meta_title")
                        or ""
                    ).strip(),
                    "meta_description": (
                        row.get("meta_description")
                        or ""
                    ).strip(),
                }

                # -------------------------------------------------
                # FIXED PRODUCT LOOKUP LOGIC
                # -------------------------------------------------
                #
                # First try to find the product by SKU.
                # If it is not found, try the generated slug.
                #
                # This prevents:
                # UNIQUE constraint failed:
                # catalog_product.slug
                # -------------------------------------------------

                product = None

                if sku:
                    product = (
                        Product.objects
                        .filter(sku=sku)
                        .first()
                    )

                if product is None:
                    product = (
                        Product.objects
                        .filter(slug=slug_value)
                        .first()
                    )

                if dry_run:

                    if product:
                        updated_count += 1
                    else:
                        created_count += 1

                else:

                    if product:

                        # Update existing product.
                        for field, value in defaults.items():
                            setattr(
                                product,
                                field,
                                value,
                            )

                        # Only update SKU when CSV contains one.
                        if sku:
                            product.sku = sku

                        product.save()

                        created = False

                    else:

                        # Create a completely new product.
                        create_data = {
                            **defaults,
                        }

                        if sku:
                            create_data["sku"] = sku

                        product = Product.objects.create(
                            **create_data
                        )

                        created = True

                    if created:
                        created_count += 1
                    else:
                        updated_count += 1

                    specification_count += (
                        self.import_specifications(
                            product,
                            row,
                            dry_run=False,
                        )
                    )

        if dry_run:
            self.stdout.write(
                self.style.WARNING(
                    (
                        f"Dry run complete. "
                        f"Would create: {created_count}; "
                        f"would update: {updated_count}"
                    )
                )
            )
            return

        self.stdout.write(
            self.style.SUCCESS(
                (
                    f"Import complete. "
                    f"Created: {created_count}; "
                    f"Updated: {updated_count}; "
                    f"Specifications: {specification_count}"
                )
            )
        )

    @staticmethod
    def parse_decimal(
        value,
        row_number,
        field_name,
    ):
        value = (value or "").strip()

        if not value:
            return None

        try:
            return Decimal(value)

        except InvalidOperation as exc:
            raise CommandError(
                f"Row {row_number}: invalid "
                f"{field_name}: {value}"
            ) from exc

    @staticmethod
    def parse_int(
        value,
        row_number,
        field_name,
        default=0,
    ):
        value = (value or "").strip()

        if not value:
            return default

        try:
            return int(value)

        except ValueError as exc:
            raise CommandError(
                f"Row {row_number}: invalid "
                f"{field_name}: {value}"
            ) from exc

    @staticmethod
    def parse_bool(
        value,
        default=False,
    ):
        if value is None:
            return default

        return str(value).strip().lower() in TRUE_VALUES

    @staticmethod
    def import_specifications(
        product,
        row,
        dry_run=False,
    ):
        count = 0

        for column, value in row.items():

            if not column:
                continue

            if not column.startswith("spec:"):
                continue

            specification_name = (
                column.split(
                    ":",
                    1,
                )[1].strip()
            )

            specification_value = (
                value or ""
            ).strip()

            if (
                not specification_name
                or not specification_value
            ):
                continue

            definition, _ = (
                ProductSpecificationDefinition.objects.get_or_create(
                    slug=slugify(
                        specification_name
                    ),
                    defaults={
                        "name": specification_name,
                    },
                )
            )

            if not dry_run:
                ProductSpecification.objects.update_or_create(
                    product=product,
                    definition=definition,
                    defaults={
                        "value": specification_value,
                    },
                )

            count += 1

        return count