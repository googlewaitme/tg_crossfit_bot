from django.db import models
from datetime import datetime


class Dictribution(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст публицаии')
    send_date_time = models.DateTimeField(
        default=datetime.now(), verbose_name='Время отправки')
    is_sended = models.BooleanField(default=False, verbose_name='Было отправлено')
    description = models.TextField(
        default='Описание', verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True)
    content_url = models.URLField(
        null=True, blank=True, verbose_name='Ссылка на фото или видео')

    button_name = models.CharField(
        default='Нет кнопки', max_length=100, verbose_name='Имя кнопки')
    button_url = models.URLField(
        null=True, blank=True, verbose_name='Ссылка кнопки действия')

    def __str__(self):
        state = '🟢' if self.is_sended else '⚪'
        return state + self.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
