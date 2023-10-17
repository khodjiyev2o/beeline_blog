from apps.blog.models import Blog
from apps.blog.forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.views.generic import list, detail, DeleteView
from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class BlogListView(list.ListView):
    template_name = 'list_blog.html'
    queryset = Blog.objects.all()
    context_object_name = 'blogs'


class BlogDetailView(detail.DetailView):
    template_name = 'detail_blog.html'
    queryset = Blog.objects.all()
    context_object_name = 'blog'


@method_decorator(login_required, name='dispatch')
class CreateBlogView(View):
    template_name = 'create_blog.html'

    def get(self, request):
        form = BlogForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class BlogDeleteView(DeleteView):
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blog_list')

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


@method_decorator(login_required, name='dispatch')
class EditBlogView(View):
    template_name = 'edit_blog.html'

    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        if blog.author == request.user:
            form = BlogForm(instance=blog)
            return render(request, self.template_name, {'form': form, 'blog': blog})
        else:
            return redirect('blog_list')

    def post(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=blog.pk)
        return render(request, self.template_name, {'form': form, 'blog': blog})


__all__  = ['BlogListView', 'BlogDetailView', 'CreateBlogView', 'BlogDeleteView', 'EditBlogView']
