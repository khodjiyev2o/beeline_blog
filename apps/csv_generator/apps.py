from django.apps import AppConfig


class CsvGeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.csv_generator'

    def ready(self):
        pass