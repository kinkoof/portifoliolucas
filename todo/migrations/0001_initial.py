# Generated by Django 4.2.1 on 2023-09-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("titulo", models.CharField(max_length=255)),
                ("descriçao", models.TextField(verbose_name="descrição")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("fazendo", "Fazendo"),
                            ("feito", "Feito"),
                            ("fazer", "Fazer"),
                        ],
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]