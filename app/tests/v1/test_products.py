import unittest
import json
from ... import create_app


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {
            "Product Name": "Infinix",
            "Category": "Electronics",
            "Stock Balance": 10,
            "Minimum Inventory": 1,
            "Price": 20000,
            "id": 1
            }

    def test_create_products(self):
        res = self.client.post(
            '/api/v1/products',
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['Message'], "Product created")

    def test_invalid_product_name(self):
        products_data = {
            "Product Name": "",
            "Category": "Electronics",
            "Stock Balance": 10,
            "Minimum Inventory": 1,
            "Price": 20000
            }
        res = self.client.post(
            '/api/v1/products',
            data=json.dumps(products_data),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertTrue(response_data['Message'], "Enter a valid product name")

    def test_invalid_product_category(self):
        products_data = {
            "Product Name": "LG prada",
            "Category": "",
            "Stock Balance": 10,
            "Minimum Inventory": 1,
            "Price": 20000
            }
        res = self.client.post(
            '/api/v1/products',
            data=json.dumps(products_data),
            headers={"content-type": "application/json"}
        )
        response_data = json.loads(res.data.decode('utf-8'))

        self.assertTrue(response_data['Message'], "Enter a valid category")

    def test_get_all_products(self):

        res = self.client.get(
            '/api/v1/products',
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)

    def test_specific_product(self):

        res = self.client.get(
            '/api/v1/products/1',
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 404)

    def test_delete_product(self):
            res = self.client.delete(
                '/api/v1/products/3',
                headers={"content-type": "application/json"}
            )
            self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
