# Generated by Django 4.2.6 on 2023-11-17 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='park',
        ),
    ]
