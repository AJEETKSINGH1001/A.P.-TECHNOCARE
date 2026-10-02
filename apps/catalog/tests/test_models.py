from django.test import TestCase
from django.db import IntegrityError

from apps.catalog.models import (
    Category,
    Product,
    ProductImage,
)


class ProductImageModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            slug="test-category",
        )

        self.product = Product.objects.create(
            name="Test Product",
            slug="test-product",
            category=self.category,
        )

    def test_product_can_be_created(self):
        self.assertEqual(
            self.product.name,
            "Test Product",
        )

    def test_only_one_primary_image_allowed(self):
        ProductImage.objects.create(
            product=self.product,
            image="products/test-1.jpg",
            is_primary=True,
        )

        with self.assertRaises(IntegrityError):
            ProductImage.objects.create(
                product=self.product,
                image="products/test-2.jpg",
                is_primary=True,
            )