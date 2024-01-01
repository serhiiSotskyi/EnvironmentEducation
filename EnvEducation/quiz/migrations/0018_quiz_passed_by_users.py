# Generated by Django 4.2.6 on 2023-12-30 14:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("quiz", "0017_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="passed_by_users",
            field=models.ManyToManyField(
                blank=True, related_name="passed_quizzes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]