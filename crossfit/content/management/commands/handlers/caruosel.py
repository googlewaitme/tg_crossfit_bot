from ..loader import dp
from aiogram import types
from ..keyboards.inline import generic
from ..utils.filters import starts_with
from ..utils.helpers import get_chapter_model, get_publication_model
from content.models import Product


@dp.callback_query_handler(starts_with('EMPTY_CALLBACK'))
async def set_readed(callback_query: types.CallbackQuery):
    """
        Нужен пустой колбек, который будет просто отмечать
        что он получен.
        Нужен для того, чтобы можно было добавлять информационные
        кнопки в inline клавиатуру или делать заглушки, для еще
        не сделанной функциональности.
    """
    await dp.bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(starts_with('categories_list'))
async def send_chapter_list(callback_query: types.CallbackQuery):
    name_of_chapter = callback_query.data.split('_')[2]
    query = get_chapter_model(name_of_chapter).objects.filter(is_view=True)
    list_button_names = [
        (el.name, f'element_{name_of_chapter}_{el.pk}_{0}') for el in query
    ]
    list_button_names.append(('Меню', 'menu'))
    markup = generic.list_inline_buttons(list_button_names)
    text = 'Список категорий'
    await callback_query.message.edit_text(
        text=text, reply_markup=markup)


@dp.callback_query_handler(starts_with('element'))
async def send_carousel_element_product(callback_query: types.CallbackQuery):
    # element_{chapter_name}_{category_id}_{element_id}
    data = callback_query.data.split('_')
    publication = get_publication_model(data[1])
    category_id, element_id = data[2], int(data[3])
    query = publication.objects.filter(category=category_id)
    if len(list(query)) > 0:
        product = list(query)[element_id]
        text = make_post(product)
        markup = make_keyboard(data)
    else:
        text = 'Пока что не одной публикации'  # TODO
        markup = generic.inline_button(
            'Назад', f'categories_list_{data[1]}')
    await callback_query.message.edit_text(
        text=text, reply_markup=markup)


def make_keyboard(data):
    category_id, element_id = data[2], int(data[3])
    back_button_callback = f'categories_list_{data[1]}'
    query = Product.objects.filter(category=category_id)
    count_objects = len(list(query))
    callback_prefix = '_'.join(data[:3])
    markup = generic.inline_carousel(
        element_id, count_objects, callback_prefix, back_button_callback)
    return markup


def make_post(element):
    text = f'<b>{element.name}</b>\n\n{element.text}'
    return text
