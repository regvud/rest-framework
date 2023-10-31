# Generated by Django 4.2.6 on 2023-10-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ParkModel",
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
                ("park_name", models.CharField(max_length=120)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "PARKS",
                "ordering": ("id",),
            },
        ),
    ]
