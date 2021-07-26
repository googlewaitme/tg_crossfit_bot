from django.db import models
from django.core.exceptions import ValidationError


def validate_grade(value):
    if 0 <= value <= 10:
        return value
    raise ValidationError('Оценка должна быть от 0 до 10')


def grade_field(verbose_name, default=0):
    field = models.IntegerField(
        verbose_name=verbose_name,
        validators=[validate_grade],
        default=default
    )
    return field


class Raiting(models.Model):
    location = grade_field('Местоположение')
    square = grade_field('Площадь зала')
    equipment = grade_field('Оснащённость зала')
    suitability = grade_field('Пригодность оборудования')
    certification = grade_field('Сертифицированные тренера')
    interior = grade_field('Свежесть интерьера')
    purity = grade_field('Чистота')
    convenience = grade_field('Сопутствующие блага')
    service = grade_field('Сервис')


class GymProfile(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    address = models.CharField(max_length=300, verbose_name='Адресс')
    general_comment = models.TextField(verbose_name='Общий комментарий')
    raiting = models.OneToOneField(
        Raiting,
        on_delete=models.CASCADE,
        primary_key=True,
    )
