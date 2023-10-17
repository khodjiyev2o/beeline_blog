from django.test import TestCase
from django.urls import reverse
from apps.blog.models import Blog
from django.contrib.auth.models import User


class BlogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = User.objects.create(username='khodjiyev2o', email='admin@gmail.com', password='123456')
        cls.blog = Blog.objects.create(title='Test Blog', content='Test Content', author=author)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_blog.html')

    def test_queryset_returns_correct_blog(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['blog'].title, 'Test Blog')
        self.assertEqual(response.context['blog'].content, 'Test Content')

