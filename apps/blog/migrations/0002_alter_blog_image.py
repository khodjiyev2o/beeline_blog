# Generated by Django 4.2.6 on 2023-10-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="blog/images/%Y/%m/",
                verbose_name="Image",
            ),
        ),
    ]
