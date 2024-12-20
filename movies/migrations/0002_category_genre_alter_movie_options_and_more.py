# Generated by Django 5.1.3 on 2024-11-17 12:26

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категорія')),
                ('description', models.TextField(default='No description available', verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('description', models.TextField(default='No description available', verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанри',
            },
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Фільм', 'verbose_name_plural': 'Фільми'},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Актори'),
        ),
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.PositiveIntegerField(default=0, help_text='вказувати суму в доларах', verbose_name='Бюджет'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.CharField(default='Unknown', max_length=30, verbose_name='Країна'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default='No description available', verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.TextField(default='Unknown', verbose_name='Режисер'),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='movies/', verbose_name='Постер'),
        ),
        migrations.AddField(
            model_name='movie',
            name='url',
            field=models.SlugField(default='', max_length=130, unique=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='world_premiere',
            field=models.DateField(default=datetime.date.today, verbose_name='Премʼєра у світі'),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(default=2024, verbose_name='Дата виходу'),
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.genre', verbose_name='жанри'),
        ),
    ]
