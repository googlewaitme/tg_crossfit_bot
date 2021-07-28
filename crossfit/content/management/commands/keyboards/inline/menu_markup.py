from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton('Выбрать спортзал 🏆', callback_data='gym_list_city')
    )
    markup.row(
        InlineKeyboardButton('Питание 🍽', callback_data='categories_list_product'),
        InlineKeyboardButton('Упражнения 🏋🏻', callback_data='categories_list_exercise')
    )
    markup.row(
        InlineKeyboardButton('Чат 💬', callback_data='MESSAGE_CHAT'),
        InlineKeyboardButton('Интересное 🧐', callback_data='MESSAGE_INTERESTING')
    )
    markup.row(
        InlineKeyboardButton('Поддержка проекта 💰', callback_data='MESSAGE_SUPPORT'),
        InlineKeyboardButton('О нас 🕵🏻‍♂️', callback_data='MESSAGE_ABOUT_US')
    )
    markup.row(
        InlineKeyboardButton('Частые вопросы 📝', callback_data='FAQ_element_0')
    )
    return markup
