# Generated by Django 4.1.3 on 2022-11-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=50)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="product_item/images/%Y/%m/%d/"
                    ),
                ),
            ],
        ),
    ]