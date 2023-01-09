from django.test import TestCase

from django.test import TestCase
from .models import Shop, Product


class ShopTestCase(TestCase):
    def setUp(self):
        Shop.objects.create(name="Test Shop", rating=7.0)
        Shop.objects.create(name="Another Test Shop", rating=4.0)

    def test_shop_names(self):
        test_shop = Shop.objects.get(name="Test Shop")
        another_test_shop = Shop.objects.get(name="Another Test Shop")
        self.assertEqual(test_shop.name, "Test Shop")
        self.assertEqual(another_test_shop.name, "Another Test Shop")

    def test_shop_ratings(self):
        test_shop = Shop.objects.get(name="Test Shop")
        another_test_shop = Shop.objects.get(name="Another Test Shop")
        self.assertEqual(test_shop.rating, 7.0)
        self.assertEqual(another_test_shop.rating, 4.0)

class ProductTestCase(TestCase):
    def setUp(self):
        shop = Shop.objects.create(name="Test Shop", rating=7.0)
        Product.objects.create(shop=shop, name="Test Product", price=10.99)
        Product.objects.create(shop=shop, name="Another Test Product", price=5.99)

    def test_product_names(self):
        test_product = Product.objects.get(name="Test Product")
        another_test_product = Product.objects.get(name="Another Test Product")
        self.assertEqual(test_product.name, "Test Product")
        self.assertEqual(another_test_product.name, "Another Test Product")

    def test_product_prices(self):
        test_product = Product.objects.get(name="Test Product")
        another_test_product = Product.objects.get(name="Another Test Product")
        self.assertEqual(test_product.price, 10.99)
        self.assertEqual(another_test_product.price, 5.99)
