# Generated by Django 3.2.8 on 2021-10-09 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='category',
        ),
        migrations.RemoveField(
            model_name='market',
            name='text',
        ),
    ]
