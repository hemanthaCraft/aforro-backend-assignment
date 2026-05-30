from rest_framework.test import APITestCase

class ProductSearchTests(APITestCase):

    def test_product_search(self):
        response = self.client.get(
            "/api/search/products/"
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_category_filter(self):
        response = self.client.get(
            "/api/search/products/?category=Electronics"
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_store_filter(self):
        response = self.client.get(
            "/api/search/products/?store=1"
        )

        self.assertEqual(
            response.status_code,
            200
        )