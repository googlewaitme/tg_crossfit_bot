from django.db import models
from django.core.exceptions import ValidationError


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя города')
    is_view = models.BooleanField(
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
        City, verbose_name='Город', on_delete=models.CASCADE, related_name='locations')

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
    conclusion = models.TextField(max_length=400, verbose_name='Заключение')

    def __str__(self):
        return self.name

    def get_raiting(self):
        fields = [getattr(self.raiting, el.name, None) for el in self.raiting._meta.get_fields()]
        int_fields = [field for field in fields if type(field) == int]
        return sum(int_fields)

    class Meta:
        verbose_name = 'Спортзал'
        verbose_name_plural = 'Спортзалы'


class Raiting(models.Model):
    raiting = models.OneToOneField(
        GymProfile,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='raiting'
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


class Visit(models.Model):
    gym = models.ForeignKey(GymProfile, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
