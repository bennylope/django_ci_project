from django.test import TestCase

from blog.models import BlogPost


class TestBlogQuerySet(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.draft = BlogPost.objects.create(
            status="draft", title="Hi", body="Hello World!"
        )
        cls.published = BlogPost.objects.create(
            status="published", title="First Post", body="This is my first post!"
        )

    def test_drafts(self):
        self.assertEqual(BlogPost.objects.drafts().get(), self.draft)

    def test_published(self):
        self.assertEqual(BlogPost.objects.published().get(), self.published)
