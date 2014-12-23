from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import ScrapeSite, ScrapeLog


class ScrapeModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "scrape_test_user",
            "scrape@domain.com",
            "testpassword",
        )

        self.site = ScrapeSite.objects.create(title="My Test Site")
        self.log1 = ScrapeSite.objects.log(self.site, "S", "Successfully logged", 0, 0)

        self.prefix = 'scrape_'

    def test_site(self):
        site = ScrapeSite.objects.get(title=self.site.title)
        self.assertNotEqual(site.slug, None)

    def test_log(self):
        log = ScrapeLog.objects.get(id=1)


class ScrapeViewTest(TestCase):
    def setUp(self):
        ScrapeModelTest.setUp(self)

    def test_admin(self):
        url = reverse(self.prefix + 'admin')
        response = self.client.get(url)

    def test_log(self):
        url = reverse(self.prefix + 'logs')
        response = self.client.get(url)


class ScrapeFormTest(TestCase):
    pass