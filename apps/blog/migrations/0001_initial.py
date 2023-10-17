# Generated by Django 4.2.6 on 2023-10-17 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("content", models.TextField(max_length=255, verbose_name="Content")),
                (
                    "image",
                    models.ImageField(
                        upload_to="blog/images/%Y/%m/", verbose_name="Image"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blog",
                "verbose_name_plural": "Blogs",
                "ordering": ("-created_at",),
            },
        ),
    ]