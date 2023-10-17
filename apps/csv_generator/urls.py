
from django.urls import path
from .views import DataSchemaListView


urlpatterns = [
    path('', DataSchemaListView.as_view(), name='schemas'),
]
