from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

class LoginTest(TestCase):
    def test_login_page_exists(self):
        response =self.client.get(reverse('login_page'))

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,'accounts/login.html')