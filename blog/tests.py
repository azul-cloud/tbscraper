from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Blog, Article


class BlogModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "blog_test_user",
            "blog@domain.com",
            "testpassword",
        )

        self.blog = Blog.objects.create(title="My Test Blog")
        self.article = Article.objects.create(
            title="My Test Article",
            blog=self.blog
        )

        self.prefix = 'blog_'

    def test_blog(self):
        blog = Blog.objects.get(title=self.blog.title)
        self.assertNotEqual(blog.slug, None)

    def test_article(self):
        article = Article.objects.get(title=self.article.title)
        self.assertNotEqual(article.slug, None)


class BlogViewTest(TestCase):
    def setUp(self):
        BlogModelTest.setUp(self)

    def test_blog(self):
        url = reverse(self.prefix + 'blog')
        response = self.client.get(url)

    def test_article(self):
        url = reverse(self.prefix + 'article')
        response = self.client.get(url)

    def test_topic(self):
        url = reverse(self.prefix + 'topic')
        response = self.client.get(url)

    def test_country(self):
        url = reverse(self.prefix + 'country')
        response = self.client.get(url)


class BlogFormTest(TestCase):
    pass