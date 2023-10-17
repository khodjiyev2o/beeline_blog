from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm


class RegisterView(View):
    form_class = CustomUserCreationForm
    template_name = 'registration.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})
