from aiogram import types
from ..loader import dp
from ..utils.helpers import get_message_one_button
from aiogram.dispatcher.filters import Command
from content.models import TelegramUser
from ..keyboards.inline import menu_markup


@dp.message_handler(Command('start'))
async def send_menu(message: types.Message):
    user, created = TelegramUser.objects.get_or_create(
        telegram_id=message.from_user.id)
    text = get_message_one_button('START_MESSAGE')
    await message.answer(text,
                         reply_markup=menu_markup.get())
