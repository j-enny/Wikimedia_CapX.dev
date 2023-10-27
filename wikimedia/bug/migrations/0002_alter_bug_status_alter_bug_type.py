# Generated by Django 4.2.6 on 2023-10-27 04:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bug", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bug",
            name="Status",
            field=models.CharField(
                choices=[
                    ("to do", "To Do"),
                    ("in progress", "In Progress"),
                    ("done", "Done"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="bug",
            name="Type",
            field=models.CharField(
                choices=[
                    ("error", "Error"),
                    ("new", "New Feature"),
                    ("update", "Update Needed"),
                ],
                max_length=15,
            ),
        ),
    ]
