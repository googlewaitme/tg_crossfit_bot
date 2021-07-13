from content.models import *


def get_message_one_button(button_name):
    '''
    В боте очень много кнопок, который отправляют текст
    с какой-то нагрузкой и актуальностью. Поэтому нужно
    иметь возможность обновлять их, без изменения в коде.
    '''
    defaults = {'description': 'Создана новый кнопка!!!',
                'text': f'Текста для {button_name} нет, просьба заполнить!'}
    button, created = ButtonOneText.objects.get_or_create(
        name=button_name, defaults=defaults)
    return button.text


def get_chapter_model(chapter_name):
    if chapter_name == 'exercise':
        return ExerciseCategory
    if chapter_name == 'product':
        return ProductCategory


def get_publication_model(chapter_name):
    if chapter_name == 'exercise':
        return Exercise
    if chapter_name == 'product':
        return Product
