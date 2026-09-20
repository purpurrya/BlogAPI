from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post


class BlogTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="test",
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="Test Post",
            content="This is a test post.",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(str(self.post), "Test Post")
