# Generated by Django 4.2.6 on 2023-12-23 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0008_quiz_remove_question_category_delete_category_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answer",
            old_name="answer",
            new_name="answer_text",
        ),
        migrations.RenameField(
            model_name="question",
            old_name="question",
            new_name="question_text",
        ),
        migrations.RemoveField(
            model_name="quiz",
            name="question",
        ),
        migrations.AddField(
            model_name="question",
            name="quiz",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="quiz.quiz",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="quiz.question",
            ),
        ),
    ]