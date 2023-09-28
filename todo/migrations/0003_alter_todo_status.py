# Generated by Django 4.2.5 on 2023-09-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_alter_todo_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="status",
            field=models.CharField(
                choices=[
                    ("backlog", "Backlog"),
                    ("to do", "To do"),
                    ("doing", "Doing"),
                    ("done", "Done"),
                ],
                default="backlog",
                max_length=10,
            ),
        ),
    ]
