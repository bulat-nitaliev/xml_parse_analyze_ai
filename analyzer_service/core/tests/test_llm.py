from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.hashers import check_password
from core.factories import LlmFactory, UserFactory
from core.models import AnswerLLm
from django.utils.timezone import make_naive

class LlmTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = '/api/llm/'
        print(self)

    def test_llm_list(self):
        LlmFactory.create_batch(20)
        response = self.client.get(path=self.url, format="json")
        count = AnswerLLm.objects.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 20)
        self.assertEqual(len(response.data), count)

    def test_unauthorized_list_llm(self):
        LlmFactory.create_batch(20)
        self.client.logout()
        response = self.client.get(path=self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
 

    def test_llm_list_response_structure(self):
        llm = LlmFactory()
        response = self.client.get(path=self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)

        data_llm = {
            "prompt": llm.prompt,
            "answer": llm.answer,
            "dt_create": make_naive(llm.dt_create).strftime("%Y-%m-%dT%H:%M:%S")
        }

    
        self.assertDictEqual(response.data[0], data_llm)

