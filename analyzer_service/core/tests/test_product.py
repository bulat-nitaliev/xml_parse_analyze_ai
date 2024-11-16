from rest_framework.test import APITestCase
from rest_framework import status
from core.factories import ProductFactory, UserFactory
from core.models import Product

class ProductTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = '/api/product/'
        print(self)

    def test_product_list(self):
        ProductFactory.create_batch(20)
        response = self.client.get(path=self.url, format="json")
        count = Product.objects.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 20)
        self.assertEqual(len(response.data), count)

    def test_unauthorized_list_product(self):
        ProductFactory.create_batch(20)
        self.client.logout()
        response = self.client.get(path=self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
 

    def test_product_list_response_structure(self):
        product = ProductFactory()
        response = self.client.get(path=self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)

        data_product = {
            "name": product.name,
            "date_product": product.date_product,
            "quantity": product.quantity,
            "price": product.price,
            "category": product.category
        }

    
        self.assertDictEqual(response.data[0], data_product)




