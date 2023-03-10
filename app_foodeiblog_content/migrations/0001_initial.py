# Generated by Django 4.1.5 on 2023-03-02 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('text', models.TextField(verbose_name='Содержание')),
                ('image', models.ImageField(upload_to='articles/articles/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('author_birth_day', models.DateField(auto_now_add=True, verbose_name='Дата рождения')),
                ('author_email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('author_phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('author_photo', models.ImageField(upload_to='articles/photo/', verbose_name='Фото')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
