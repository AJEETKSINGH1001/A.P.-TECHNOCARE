from django.test import TestCase
from django.urls import reverse

from apps.catalog.models import (
    Category,
    Product,
)


class ProductCatalogViewTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Welding Electrodes",
            slug="welding-electrodes",
            is_active=True,
        )

        self.product = Product.objects.create(
            name="Test Welding Electrode",
            slug="test-welding-electrode",
            category=self.category,
            is_active=True,
        )

    def test_product_list_page_loads(self):
        response = self.client.get(
            reverse("products")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Test Welding Electrode",
        )

    def test_product_detail_page_loads(self):
        response = self.client.get(
            reverse(
                "product_detail",
                kwargs={
                    "slug": self.product.slug,
                },
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Test Welding Electrode",
        )

    def test_category_page_loads(self):
        response = self.client.get(
            reverse(
                "category_products",
                kwargs={
                    "slug": self.category.slug,
                },
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Test Welding Electrode",
        )

    def test_search_finds_product(self):
        response = self.client.get(
            reverse("search"),
            {
                "q": "Welding",
            },
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "Test Welding Electrode",
        )