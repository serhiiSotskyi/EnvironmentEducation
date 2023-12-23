# Generated by Django 4.2.6 on 2023-12-23 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0009_rename_answer_answer_answer_text_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answer",
            old_name="answer_text",
            new_name="answer",
        ),
        migrations.RenameField(
            model_name="question",
            old_name="question_text",
            new_name="question",
        ),
        migrations.AlterField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="question_answer",
                to="quiz.question",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questins",
                to="quiz.quiz",
            ),
        ),
    ]
