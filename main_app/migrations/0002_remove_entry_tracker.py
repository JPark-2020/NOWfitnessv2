# Generated by Django 3.2.5 on 2021-07-10 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='tracker',
        ),
    ]
