# Generated by Django 3.2.8 on 2021-10-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20211009_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='market',
            name='price',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='цена'),
        ),
    ]
