from django.db import models


class TelegramUser(models.Model):
    telegram_id = models.CharField(editable=False, max_length=12)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.telegram_id

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class AbstractCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя категории')
    description = models.TextField(verbose_name='Описание')
    is_view = models.BooleanField(default=False, verbose_name='Отображение')
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        state = '🟢' if self.is_view else '⚪'
        return state + ' ' + self.name + ' | ' + self.description[:100]

    class Meta:
        abstract = True


class ProductCategory(AbstractCategory):
    class Meta:
        verbose_name = 'Категория рецептов'
        verbose_name_plural = 'Категории рецептов'


class ExerciseCategory(AbstractCategory):
    class Meta:
        verbose_name = 'Категория упражнений'
        verbose_name_plural = 'Категории упражнений'


class Publication(models.Model):
    text = models.TextField(verbose_name='Текст публикации')
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    name = models.CharField(
        max_length=200, verbose_name='Заголовок')

    def __str__(self):
        return self.name + ' ' + self.category.name

    class Meta:
        abstract = True


class PopularQuestion(Publication):
    class Meta:
        verbose_name = 'Популярный вопрос'
        verbose_name_plural = 'Частые вопросы'

    def __str__(self):
        return self.name


class Product(Publication):
    category = models.ForeignKey(
        ProductCategory, on_delete=models.PROTECT,
        verbose_name='Категория', related_name='products')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'рецепты'


class Exercise(Publication):
    category = models.ForeignKey(
        ExerciseCategory, on_delete=models.PROTECT,
        verbose_name='Категория', related_name='exercises')

    class Meta:
        verbose_name = 'Упражения'
        verbose_name_plural = 'Упражения'


class ButtonOneText(models.Model):
    name = models.CharField(
        max_length=200, unique=True, verbose_name='Уникальное название')
    text = models.TextField(
        verbose_name='Отправляемый текст')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шаблон сообщения'
        verbose_name_plural = 'Шаблоны сообщений'
