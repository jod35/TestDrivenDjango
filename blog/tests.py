from django.test import TestCase
from .models import Entry
from http import HTTPStatus
# Create your tests here.

class EntryModelTest(TestCase):
    def test_string_representation(self):
        entry = Entry(title="Sample Title",
        body="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        
        self.assertEqual(str(entry),entry.title)


    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural),"Entries")


    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,'blog/index.html')