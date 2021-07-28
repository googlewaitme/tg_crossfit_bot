from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from django.core.paginator import Page


def list_inline_buttons(list_buttons):
    markup = InlineKeyboardMarkup()
    for name, callback_data in list_buttons:
        button = InlineKeyboardButton(name, callback_data=callback_data)
        markup.add(button)
    return markup


def inline_carousel(object_id, count_objects,
                    callback_prefix='', callback_back_button=''):
    """
    Будет генерировать клавиатуру для карусели


    На вход получает id нового объекта,
    массив всех объектов.

    Возвращает клавиатуру, с кнопками
    <- | номер_страницы | ->
            назад
    """
    markup = InlineKeyboardMarkup()
    if object_id > 0:
        callback_prev = f'{callback_prefix}_{object_id - 1}'
        button_prev = InlineKeyboardButton('<-', callback_data=callback_prev)
        markup.insert(button_prev)
    button_page = InlineKeyboardButton(str(object_id + 1), callback_data='EMPTY_CALLBACK')
    markup.insert(button_page)
    if object_id + 1 < count_objects:
        callback_next = f'{callback_prefix}_{object_id + 1}'
        button_next = InlineKeyboardButton('->', callback_data=callback_next)
        markup.insert(button_next)
    back_button = InlineKeyboardButton('Назад', callback_data=callback_back_button)
    markup.add(back_button)
    return markup


def get_empty_markup(**kwargs):
    return InlineKeyboardMarkup(**kwargs)


def inline_button(text, callback_data, markup=None):
    if not markup:
        markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text, callback_data=callback_data)
    markup.add(button)
    return markup


def inline_carousel_by_paginator(
        markup: InlineKeyboardMarkup, page: Page,
        callback_prefix: str, callback_back_button: str):
    buttons = []
    if page.has_previous():
        callback_prev = callback_prefix + str(page.previous_page_number())
        button_prev = InlineKeyboardButton('<-', callback_data=callback_prev)
        buttons.append(button_prev)
    button_page = InlineKeyboardButton(str(page.number), callback_data='EMPTY_CALLBACK')
    buttons.append(button_page)
    if page.has_next():
        callback_next = callback_prefix + str(page.next_page_number())
        button_next = InlineKeyboardButton('->', callback_data=callback_next)
        buttons.append(button_next)
    markup.row(*buttons)
    back_button = InlineKeyboardButton('Назад', callback_data=callback_back_button)
    markup.add(back_button)
    return markup
