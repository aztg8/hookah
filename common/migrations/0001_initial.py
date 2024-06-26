# Generated by Django 5.0.6 on 2024-06-10 06:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='only_medias/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'svg', 'jpeg', 'mp4', 'avi', 'mkv', 'mov', 'pdf', 'doc', 'docx', 'gif'])], verbose_name='Файл')),
                ('file_type', models.CharField(choices=[('image', 'Изображение'), ('video', 'Видео'), ('document', 'Документ'), ('gif', 'Гиф')], max_length=10, verbose_name='Тип файла')),
            ],
            options={
                'verbose_name': 'Медиа файл',
                'verbose_name_plural': 'Медиа файлы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('stars', models.IntegerField(default=0)),
                ('text', models.TextField(verbose_name='Текст')),
                ('author_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='common.user', verbose_name='author_id')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
