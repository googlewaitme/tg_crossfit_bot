from ..loader import dp
from aiogram import types
# from keyboards.inline import make_caruosel
from ..keyboards.inline import generic
from ..utils.filters import starts_with
from content.models import ProductCategory


@dp.callback_query_handler(starts_with('product'))
async def send_product_list(callback_query: types.CallbackQuery):
    query = ProductCategory.objects.all()
    list_button_names = [(el.name, f'product_{el.name}') for el in query]
    list_button_names.append(('Меню', 'menu'))
    markup = generic.list_inline_buttons(list_button_names)
    text = 'Список категорий'
    await callback_query.message.edit_text(
        text=text, reply_markup=markup)
