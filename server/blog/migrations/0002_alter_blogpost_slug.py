# Generated by Django 4.1.2 on 2022-10-29 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
