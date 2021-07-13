from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def list_inline_buttons(list_buttons):
    markup = InlineKeyboardMarkup()
    for name, callback_data in list_buttons:
        button = InlineKeyboardButton(name, callback_data=callback_data)
        markup.add(button)
    return markup
