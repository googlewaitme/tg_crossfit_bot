# Generated by Django 3.2.5 on 2021-07-11 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonOneText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=200, unique=True, verbose_name='Уникальное название')),
                ('text', models.TextField(verbose_name='Отправляемый текст')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Кнопка одного текста',
                'verbose_name_plural': 'Кнопки одного текста',
            },
        ),
        migrations.CreateModel(
            name='ExerciseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя категории')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория упражнений',
                'verbose_name_plural': 'Категории упражнений',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя категории')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория питания',
                'verbose_name_plural': 'Категории питаний',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст публикации')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='content.productcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Питание',
                'verbose_name_plural': 'Питания',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст публикации')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='content.exercisecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Упражения',
                'verbose_name_plural': 'Упражения',
            },
        ),
    ]
