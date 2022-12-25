from django.test import TestCase
from django.urls import reverse
from http  import HTTPStatus
from accounts.models import Profile

class ProfileTest(TestCase):
    def setUp(self) -> None:
        self.url =reverse('current_user_profile')
        self.template_name ='accounts/currentuserprofile.html'


    def test_user_profile_page_exists(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,self.template_name)

    def test_user_profile_in_profile_page(self):
        response = self.client.get(self.url)

        user_profile=response.context.get('profile',None)

        self.assertIsInstance(user_profile,Profile)