# Generated by Django 5.1.3 on 2024-11-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='', verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(default='', verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(default='', max_length=30, verbose_name='Країна'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(default='', verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.TextField(default='', verbose_name='Режисер'),
        ),
    ]
