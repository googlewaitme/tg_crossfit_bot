# Generated by Django 3.2.5 on 2021-07-14 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictribution', '0004_auto_20210714_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictribution',
            name='send_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 21, 40, 25, 401686), verbose_name='Время отправки'),
        ),
    ]
