from aiogram import types
from ..keyboards.inline import generic
from ..loader import dp
from ..utils.helpers import get_message_one_button
from ..utils.filters import starts_with


@dp.callback_query_handler(starts_with('MESSAGE'))
async def send_editable_message(callback_query: types.CallbackQuery):
    back = generic.inline_button('Назад', 'menu')
    text = get_message_one_button(callback_query.data)
    await callback_query.message.edit_text(
        text=text, reply_markup=back)
