from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        'Питание', callback_data='categories_list_product'))
    markup.add(InlineKeyboardButton(
        'Упражения', callback_data='categories_list_exercise'))
    return markup
