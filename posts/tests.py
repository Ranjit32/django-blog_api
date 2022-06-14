from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a user
        testUser1 = User.objects.create_user(
            username="ranjit", password="ranjit")
        testUser1.save()

        # create a blog post
        testPost = Post.objects.create(
            author=testUser1, title="django", body="about django")
        testPost.save()

    def testBlogContent(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "ranjit")
        self.assertEqual(title, "django")
        self.assertEqual(body, "about django")
