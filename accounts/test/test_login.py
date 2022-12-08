from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginTest(TestCase):
    def setUp(self):
        self.username = "testuser123"
        self.email ="testuser123@gmail.com"
        self.password ="testpassword##123"

        User.objects.create_user(
            username =self.username,
            email=self.email,
            password=self.password
        )

    def test_login_page_exists(self):
        response =self.client.get(reverse('login_page'))

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,'accounts/login.html')

    def test_login_page_has_login_form(self):
        response =self.client.get(reverse('login_page'))

        form = response.context.get('form')

        self.assertIsInstance(form,AuthenticationForm)
    
    def test_login_page_logs_in_user(self):
        user_data ={
            'username':self.username,
            'password':self.password
        }

        response = self.client.post(reverse('login_page'),user_data)

        self.assertRedirects(response,reverse('homepage'))