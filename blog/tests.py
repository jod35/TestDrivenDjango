from django.test import TestCase
from .models import Entry
from http import HTTPStatus
from django.contrib.auth import get_user_model
# Create your tests here.

User = get_user_model()

class EntryModelTest(TestCase):

    def setUp(self):
        User.objects.create(
            username="testuser",
            password ="testuser123"
        )
    

    def test_string_representation_is_correct(self):
        entry = Entry(title="Sample Title",
        body="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        
        self.assertEqual(str(entry),entry.title)


    def test_verbose_name_plural_returns_correct(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural),"Entries")

   
    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,'blog/index.html')


    def test_blog_entries_show_up_on_homepage(self):
        user = User.objects.get(id=1)
        Entry.objects.create(
            title= "Learn Django",
            body="This is a self paced Django tutorial",
            author= user
        )

        response =  self.client.get('/')

        self.assertContains(response,'Learn Django')
        

    def test_entry_detail_page_returns_ok(self):
        user = User.objects.get(id=1)
        Entry.objects.create(
            title="Learn Django",
            body="dpqwjdpodwq dwqdjqwopdjpoqw dqwopdjqwopjdoqpwjd dqwdqwdqwdqw dqwdqwdqw",
            author=user
        )

        response =self.client.get('/1')

        self.assertEqual(response.status_code,HTTPStatus.OK)

