from django.test import TestCase
from .models import Post
from http import HTTPStatus

# Create your tests here.


class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):

        post = Post.objects.create(title="Test Post", body="Test Body")

        self.assertEqual(str(post), post.title)


class HomepageTest(TestCase):
    def setUp(self) -> None:
        self.post1 = Post.objects.create(
            title="sample post 1",
            body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,",
        )

        self.post2 = Post.objects.create(
            title="sample post 2",
            body="Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,",
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")
        
        self.assertContains(response,self.post1.title)
        self.assertContains(response,self.post2.title)


class DetailPageTest(TestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create(
        title="Learn Javascript in this 23 hour course",
        body="this is a beginner course on JS"
    )

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,'posts/detail.html')

    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response,self.post.title)
        self.assertContains(response,self.post.body)
        self.assertContains(response,self.post.created_at)


