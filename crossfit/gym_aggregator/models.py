from django.db import models
from django.core.exceptions import ValidationError


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя города')
    is_hidden = models.BooleanField(
        default=False, verbose_name='Отображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Location(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Обозначение локации')
    city = models.ForeignKey(
        City, verbose_name='Город', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


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


class GymProfile(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    address = models.CharField(max_length=300, verbose_name='Адресс')
    general_comment = models.TextField(verbose_name='Общий комментарий')
    locations = models.ManyToManyField(
        Location,
        verbose_name='Локации'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спортзал'
        verbose_name_plural = 'Спортзалы'


class Raiting(models.Model):
    raiting = models.OneToOneField(
        GymProfile,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    location = grade_field('Местоположение')
    square = grade_field('Площадь зала')
    equipment = grade_field('Оснащённость зала')
    suitability = grade_field('Пригодность оборудования')
    certification = grade_field('Сертифицированные тренера')
    interior = grade_field('Свежесть интерьера')
    purity = grade_field('Чистота')
    convenience = grade_field('Сопутствующие блага')
    service = grade_field('Сервис')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
