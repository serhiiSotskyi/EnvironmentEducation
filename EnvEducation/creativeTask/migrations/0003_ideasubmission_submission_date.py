# Generated by Django 4.2.6 on 2023-12-31 11:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("creativeTask", "0002_rename_category_ideasubmission_name_of_the_idea"),
    ]

    operations = [
        migrations.AddField(
            model_name="ideasubmission",
            name="submission_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
