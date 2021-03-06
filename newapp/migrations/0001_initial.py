# Generated by Django 3.2.8 on 2021-10-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('text', models.CharField(default='No Text', max_length=1000, verbose_name='Текст Поста')),
                ('category', models.CharField(max_length=40, verbose_name='категория')),
                ('image', models.ImageField(upload_to='upload/products', verbose_name='Изображение')),
            ],
        ),
    ]
