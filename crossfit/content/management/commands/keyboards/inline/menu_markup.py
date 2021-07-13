from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


def get():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        'Питание', callback_data='product'))
    markup.add(InlineKeyboardButton(
        'Упражения', callback_data='exersice'))
    return markup
