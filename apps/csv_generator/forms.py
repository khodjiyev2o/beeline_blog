# from django import forms
# from .models import *
# from .services.data_types import *
#
#
# class DataSchemaForm(forms.ModelForm):
#     class Meta:
#         model = DataSchema
#         fields = ('name', 'column_separator', 'string_character')
#
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'Name'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             for field_name, field in self.fields.items():
#                 field.widget.attrs['class'] = 'form-control'
#
#
# class SchemaColumnForm(forms.ModelForm):
#
#     class Meta:
#         model = Column
#         fields = ('column_name', 'data_type', 'order')
#
#     def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             for field_name, field in self.fields.items():
#                 field.widget.attrs['class'] = 'form-control'
#
#
# class GeneratedDataForm(forms.ModelForm):
#     class Meta:
#         model = GeneratedData
#         fields = ('rows',)