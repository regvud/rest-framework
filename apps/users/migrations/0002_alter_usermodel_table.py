# Generated by Django 4.2.6 on 2023-11-01 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='usermodel',
            table='auth_users',
        ),
    ]
