# Generated by Django 5.1.1 on 2024-10-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "simuladosingles",
            "0002_alter_question_assertiva1_alter_question_assertiva2_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="FillInBlank",
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
                ("pergunta", models.CharField(max_length=5000)),
                ("resposta", models.CharField(max_length=5000)),
            ],
        ),
    ]