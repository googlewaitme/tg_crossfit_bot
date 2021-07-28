from content.models import PopularQuestion
from ..loader import dp
from aiogram import types
from ..utils.filters import starts_with
from ..keyboards.inline import generic
from ..utils.helpers import get_message_one_button


@dp.callback_query_handler(starts_with('FAQ_element'))
async def send_faq_carousel(callback_query: types.CallbackQuery):
    # data FAQ_element_{element_id}
    data = callback_query.data.split('_')
    list_elements = list(PopularQuestion.objects.all())
    count_elements = len(list_elements)
    if count_elements == 0:
        text = get_message_one_button('FAQ нет ни одного вопроса')
        markup = generic.inline_button('Назад', 'menu')
    else:
        element_id = int(data[2])
        text = make_post(element_id, list_elements)
        markup = make_markup(data, count_elements)
    await callback_query.message.edit_text(
        text=text, reply_markup=markup)


def make_markup(data, count_elements):
    element_id = int(data[2])
    callback_prefix = 'FAQ_element'
    callback_back_button = 'menu'
    markup = generic.inline_carousel(
        element_id, count_elements, callback_prefix, callback_back_button
    )
    return markup


def make_post(element_id, list_objects):
    question = list_objects[element_id]
    text = f'<b>{question.name}</b>\n\n{question.text}'
    return text
