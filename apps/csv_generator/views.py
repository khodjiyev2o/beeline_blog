# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .forms import *
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.utils.decorators import method_decorator
#
#
# @method_decorator(login_required, name='dispatch')
# class DataSchemaListView(ListView):
#     template_name = 'csv_generator/templates/csv_generator/schemas.html'
#     model = DataSchema
#     queryset = DataSchema.objects.all()
#
#
# @method_decorator(login_required, name='dispatch')
# class DataSchemaDetailView(DetailView):
#     model = DataSchema
#     template_name = 'csv_generator/templates/csv_generator/detail_schema.html'
#
#     def get_queryset(self):
#         queryset = super(DataSchemaDetailView, self).get_queryset()
#         pk = self.kwargs.get(self.pk_url_kwarg, None)
#         return queryset.filter(id=pk).prefetch_related('column_set','generated_data')
#
#     def post(self, request, *args, **kwargs):
#         schema = self.get_object()
#         form = GeneratedDataForm(request.POST)
#         rows = request.POST.get('rows')
#         if not rows:
#             messages.error(request, 'Please enter the number of rows',extra_tags='danger')
#             return self.get(request, *args, **kwargs)
#         if form.is_valid():
#             messages.success(request, 'Data is being generated, please refresh the page !')
#             generated_data = form.save(commit=False)
#             generated_data.data_schema = schema
#             generated_data.save()
#             return redirect(self.request.path)
#         return render(request, self.template_name, {'form': form, 'schema': schema})

#
# @method_decorator(login_required, name='dispatch')
# class SchemaDeleteView(DeleteView):
#     model = DataSchema
#     template_name = "csv_generator/templates/csv_generator/delete_schema.html"
#     success_url = reverse_lazy("schemas")

