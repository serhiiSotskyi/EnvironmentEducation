# Generated by Django 4.2.6 on 2023-12-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0014_remove_quiz_id_alter_quiz_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=200),
        ),
    ]