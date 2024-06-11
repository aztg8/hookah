# Generated by Django 5.0.6 on 2024-06-10 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название страны')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='PrepMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Метод приготовления')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название тэга')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название продукта')),
                ('leaf', models.CharField(max_length=120, verbose_name='Из какого листа')),
                ('composition', models.CharField(max_length=120, verbose_name='Состав')),
                ('strength', models.CharField(choices=[('strong', 'крепкий')], max_length=120, verbose_name='Крепость')),
                ('taste', models.CharField(max_length=120, verbose_name='Вкус')),
                ('type', models.CharField(max_length=120, verbose_name='Тип')),
                ('description', models.TextField(verbose_name='Описание')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tobacco.country', verbose_name='Страна')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tobacco.manufacturer', verbose_name='Производитель')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Фото')),
                ('preparation', models.ManyToManyField(to='tobacco.prepmethod')),
                ('tag', models.ManyToManyField(to='tobacco.tag', verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]