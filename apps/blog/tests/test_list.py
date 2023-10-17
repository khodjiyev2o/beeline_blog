
from django.test import TestCase
from django.urls import reverse
from apps.blog.models import Blog
from django.contrib.auth.models import User


class TestBlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some test blogs for the list view
        author = User.objects.create(username='khodjiyev2o', email='admin@gmail.com', password='123456')
        number_of_blogs = 5
        for blog_num in range(number_of_blogs):
            Blog.objects.create(title=f'Test Blog {blog_num}', content=f'Test Content {blog_num}', author=author)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_blog.html')

    def test_queryset_returns_all_blogs(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['blogs']), 5)

    def test_queryset_returns_correct_blogs(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['blogs'][0].title, 'Test Blog 4')
        self.assertEqual(response.context['blogs'][1].title, 'Test Blog 3')
