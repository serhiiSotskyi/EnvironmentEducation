# Generated by Django 4.2.6 on 2023-12-30 14:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0003_alter_article_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="readers",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]