# Generated by Django 3.2.5 on 2021-07-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210706_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(blank=True, null=True, to='main_app.Exercise'),
        ),
    ]