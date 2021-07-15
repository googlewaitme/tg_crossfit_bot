from ..loader import dp
from aiogram import types
from ..keyboards.inline import menu_markup
from aiogram.dispatcher.filters import Command
from content.models import TelegramUser
from ..utils.filters import starts_with
from ..utils.helpers import get_message_one_button


@dp.message_handler(Command('menu'))
async def send_menu(message: types.Message):
    user, created = TelegramUser.objects.get_or_create(
        telegram_id=message.from_user.id)
    text = get_message_one_button('MENU_MESSAGE')
    await message.answer(text,
                         reply_markup=menu_markup.get())


@dp.callback_query_handler(starts_with('menu'))
async def send_menu_by_callback(callback_query: types.CallbackQuery):
    user, created = TelegramUser.objects.get_or_create(
        telegram_id=callback_query.from_user.id)
    text = get_message_one_button('MENU_MESSAGE')
    await callback_query.message.edit_text(
        text, reply_markup=menu_markup.get())
