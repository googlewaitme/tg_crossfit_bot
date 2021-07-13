from aiogram import types
from ..loader import dp


@dp.callback_query_handler(lambda c: True)
async def send_echo(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(f'Колбек без хендлера'
                                           f'Колбек:'
                                           f'{callback_query.data}')


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")
