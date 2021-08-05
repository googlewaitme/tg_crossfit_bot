from ..loader import dp
from aiogram import types
from ..utils.filters import starts_with
from ..keyboards.inline import generic
from gym_aggregator.models import City, GymProfile, Visit
from django.core.paginator import Paginator
from ..utils.helpers import get_message_one_button
from ..utils.states import SearchPlaceState
from aiogram.dispatcher import FSMContext
from fuzzywuzzy import process


@dp.callback_query_handler(starts_with('gym_list_city'))
async def send_list_cities(callback_query: types.CallbackQuery):
    # gym_list_city
    buttons = list()
    for city in City.objects.filter(is_view=True):
        buttons.append((city.name, f'gym_locations_city_{city.pk}'))
    buttons.append(('Назад', 'menu'))
    text = get_message_one_button('Список городов', 'Выберите город')
    markup = generic.list_inline_buttons(buttons)
    await callback_query.message.edit_text(
        text, reply_markup=markup)


@dp.callback_query_handler(starts_with('gym_locations_city'))
async def search_locations(callback_query: types.CallbackQuery, state: FSMContext):
    # gym_locations_city_{city.pk}
    city_id = callback_query.data.split('_')[3]
    await SearchPlaceState.SEARCHING.set()
    await callback_query.message.edit_text(
        text=get_message_one_button('Запишите название метро/локацию'),
        reply_markup=generic.inline_button('Меню', 'menu')
    )
    await state.update_data(
        message_id=callback_query.message.message_id,
        city_id=city_id
    )


@dp.message_handler(state=SearchPlaceState.SEARCHING)
async def searching(message: types.Message, state: FSMContext):
    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id
    )
    data = await state.get_data()
    message_id = data['message_id']
    city_id = data['city_id']
    city = City.objects.get(pk=city_id)
    locations = city.locations.all()
    query = process.extract(message.text, locations)
    first_page = 1
    buttons = [
        (location[0].name, f'gym_{city.pk}_{location[0].pk}_{first_page}') for location in query
    ]
    buttons.append(('Меню', 'menu'))
    await dp.bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message_id,
        text=f'<b>Список метро/районов по запросу:</b> {message.text}.'
             '\nОтправьте сообщение снова, чтобы поменять текст запроса!',
        reply_markup=generic.list_inline_buttons(buttons)
    )


@dp.callback_query_handler(starts_with('gym_visit'))
async def set_walked(callback_query: types.CallbackQuery):
    # gym_visit_{gym_id}_{user_id}
    gym_id, user_id = callback_query.data.split('_')[2:]
    gym = GymProfile.objects.get(pk=gym_id)
    Visit.objects.get_or_create(gym=gym, user=user_id)
    markup = callback_query.message.reply_markup
    markup['inline_keyboard'][0][0]['text'] = '🏆 ВЫ СХОДИЛИ'
    await callback_query.message.edit_reply_markup(markup)


@dp.callback_query_handler(starts_with('gym'), state='*')
async def send_gyms(callback_query: types.CallbackQuery, state: FSMContext):
    # gym_{city_index}_{location_index}_{gym_index}
    await state.reset_state()
    text, markup = make_message(callback_query)
    await callback_query.message.edit_text(
        text, reply_markup=markup)


def make_message(callback_query: types.CallbackQuery):
    city_index = int(callback_query.data.split('_')[1])
    location_index = int(callback_query.data.split('_')[2])
    page_id = int(callback_query.data.split('_')[3])
    city = City.objects.get(pk=city_index)
    location = city.locations.get(pk=location_index)
    query = GymProfile.objects.filter(locations__in=[location])
    gyms = list(query)
    gyms.sort(key=lambda x: -(x.get_raiting()))
    paginator = Paginator(gyms, per_page=1, allow_empty_first_page=True)
    page = paginator.page(page_id)
    gym = page.object_list[0]
    user_id = callback_query.message.from_user.id
    markup = make_markup(
        gym_id=gym.pk, user_id=user_id,
        city_index=city_index,
        location_index=location_index, page=page)
    text = make_text(gym)
    return (text, markup)


def make_markup(gym_id, user_id, city_index, location_index, page):
    back_button_callback = f'gym_locations_city_{city_index}'
    callback_prefix = f'gym_{city_index}_{location_index}_'
    if list(Visit.objects.filter(user=user_id, gym__pk=gym_id)):
        button_text = '🏆 ВЫ СХОДИЛИ'
    else:
        button_text = 'Сходил 🚶‍♂️'
    markup = generic.inline_button(button_text, f'gym_visit_{gym_id}_{user_id}')
    markup = generic.inline_carousel_by_paginator(
        markup, page, callback_prefix, back_button_callback)
    return markup


def make_text(gym):
    locations = ', '.join([location.name for location in gym.locations.all()])
    median = int(gym.get_raiting() / 9)
    points = '🔴' * min(3, median) + '🟡' * min(3, max(0, median - 3))
    points += '🟢' * min(4, max(median - 6, 0)) + '⚪' * (10 - median)
    text = f'<b>{gym.name}</b>\n' \
           f'{locations}\n\n' \
           f'{gym.general_comment}\n' \
           f'Оценка: {points}\n' \
           f'{gym.conclusion}\n' \
           f'{gym.address}'
    return text
