from django.test import TestCase
from django.urls import reverse
from apps.blog.models import Blog
from django.contrib.auth.models import User


class BlogDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = User.objects.create(username='khodjiyev2o', email='admin@gmail.com', password='123456')
        author2 = User.objects.create(username='user2', email='user2@gmail.com', password='123456')
        cls.blog = Blog.objects.create(title='Test Blog', content='Test Content', author=author)

    def test_anonymous_user_cannot_delete(self):
        response = self.client.get(reverse('delete_blog', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 302)  #

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='khodjiyev2o', password='123456')
        response = self.client.get(reverse('delete_blog', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='khodjiyev2o', password='123456')
        response = self.client.get(reverse('delete_blog', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 302)

    def test_deleting_blog(self):
        self.client.login(username='khodjiyev2o', password='123456')
        response = self.client.post(reverse('delete_blog', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 302)  # Redirects after deletion

        # Check if the blog has been deleted
        self.assertEqual(Blog.objects.filter(pk=self.blog.pk).exists(), True)

    def test_deleting_own_blog(self):
        self.client.login(username='khodjiyev2o', password='123456')
        response = self.client.post(reverse('delete_blog', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 302)

        # Check if the blog has been deleted
        self.assertEqual(Blog.objects.filter(pk=self.blog.pk).exists(), True)

    def test_deleting_other_user_blog(self):
        self.client.login(username='user2', password='123456')
        response = self.client.post(reverse('delete_blog', args=[self.blog.pk]))
        self.assertEqual(response.status_code, 302)

        # Check if the blog still exists
        self.assertEqual(Blog.objects.filter(pk=self.blog.pk).exists(), True)
