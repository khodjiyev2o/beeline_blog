from django.urls import path
from apps.blog.views import BlogListView, BlogDetailView, CreateBlogView, EditBlogView, BlogDeleteView


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', CreateBlogView.as_view(), name='create_blog'),
    path('edit/<int:pk>/', EditBlogView.as_view(), name='edit_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
