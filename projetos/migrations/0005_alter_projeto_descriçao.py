# Generated by Django 4.2.1 on 2023-07-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projetos", "0004_alter_projeto_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projeto",
            name="descriçao",
            field=models.TextField(verbose_name="descrição"),
        ),
    ]
