# Generated by Django 4.2.6 on 2023-12-24 13:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("quiz", "0016_remove_question_quiz_delete_answer_delete_question_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Quiz",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("quiz_name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("question", models.CharField(max_length=300)),
                ("marks", models.IntegerField(default=1)),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question",
                        to="quiz.quiz",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("answer", models.CharField(max_length=100)),
                ("is_correct", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answer",
                        to="quiz.question",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]