from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UserTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            name="Example User",
            user_id=1,
            plaid_info="12245",
            coinbase_info="98765",
        )

    def test_user_content(self):
        self.assertEqual(self.user.name, "Example User")
        self.assertEqual(self.user.user_id, 1)
        self.assertEqual(self.user.plaid_info, "12245")
        self.assertEqual(self.user.coinbase_info, "98765")

    def test_user_list(self):
        response = self.client.get(reverse("api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.user.name)