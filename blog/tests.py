from django.test import TestCase
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        Post.objects.Create(
            title = 'myTitle',
            body = 'just a Test'
        )
    def test_string_representation(self):
        post = Post(title='My entity title')
        self.assertEqual(str(post),post.title)
    def test_post_list_view(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response, 'blog/blog.html')
    def test_post_detail_view(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response, 'blog/post.html')