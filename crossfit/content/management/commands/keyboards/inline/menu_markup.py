from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton('Питание', callback_data='categories_list_product'),
        InlineKeyboardButton('Упражения', callback_data='categories_list_exercise')
    )
    markup.row(
        InlineKeyboardButton('Чат', callback_data='MESSAGE_CHAT'),
        InlineKeyboardButton('Интересное', callback_data='MESSAGE_INTERESTING')
    )
    markup.row(
        InlineKeyboardButton('Поддержка проекта', callback_data='MESSAGE_SUPPORT'),
        InlineKeyboardButton('О нас', callback_data='MESSAGE_ABOUT_US')
    )
    return markup
