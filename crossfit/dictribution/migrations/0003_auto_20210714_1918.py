# Generated by Django 3.2.5 on 2021-07-14 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictribution', '0002_auto_20210714_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictribution',
            name='button_name',
            field=models.CharField(default='test_text', max_length=100, verbose_name='Имя кнопки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dictribution',
            name='send_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 19, 18, 33, 521488), verbose_name='Время отправки'),
        ),
    ]
