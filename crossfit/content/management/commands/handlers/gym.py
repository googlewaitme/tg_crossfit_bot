from ..loader import dp
from aiogram import types
from ..utils.filters import starts_with
from ..keyboards.inline import generic
from gym_aggregator.models import City, GymProfile, Visit
from django.core.paginator import Paginator
from ..utils.helpers import get_message_one_button


@dp.callback_query_handler(starts_with('gym_list_city'))
async def send_list_cities(callback_query: types.CallbackQuery):
    # gym_list_city
    # TODO для количества городов больше 10
    buttons = list()
    for city in City.objects.filter(is_view=True):
        buttons.append((city.name, f'gym_city_{city.pk}_0'))
    buttons.append(('Назад', 'menu'))
    text = get_message_one_button('Список городов', 'Выберите город')
    markup = generic.list_inline_buttons(buttons)
    await callback_query.message.edit_text(
        text, reply_markup=markup)


@dp.callback_query_handler(starts_with('gym_city_'))
async def send_locations(callback_query: types.CallbackQuery):
    # gym_city_{city_index}_{page_id}
    # TODO для количества локаций больше 10 и больше 100
    # Сделать поиск по локациям
    city_index = int(callback_query.data.split('_')[2])
    page_id = int(callback_query.data.split('_')[3])
    city = City.objects.get(pk=city_index)
    locations = list(city.locations.all())[7 * page_id: 7 * (page_id + 1)]
    first_page = 1
    buttons = list()
    for location in locations:
        buttons.append(
            (location.name, f'gym_{city.pk}_{location.pk}_{page_id}_{first_page}'))
    buttons.append(('Назад', 'gym_list_city'))
    markup = generic.list_inline_buttons(buttons)
    text = get_message_one_button('Список локаций', 'Выберите локацию')
    await callback_query.message.edit_text(
        text, reply_markup=markup)


@dp.callback_query_handler(starts_with('gym_visit'))
async def set_walked(callback_query: types.CallbackQuery):
    # gym_visit_{gym_id}_{user_id}
    gym_id, user_id = callback_query.data.split('_')[2:]
    gym = GymProfile.objects.get(pk=gym_id)
    Visit.objects.get_or_create(gym=gym, user=user_id)
    markup = callback_query.message.reply_markup
    markup['inline_keyboard'][0][0]['text'] = '🏆 ВЫ СХОДИЛИ'
    await callback_query.message.edit_reply_markup(markup)


@dp.callback_query_handler(starts_with('gym'))
async def send_gyms(callback_query: types.CallbackQuery):
    # gym_{city_index}_{location_index}_{page_id}_{gym_index}
    text, markup = make_message(callback_query)
    await callback_query.message.edit_text(
        text, reply_markup=markup)


def make_message(callback_query: types.CallbackQuery):
    city_index = int(callback_query.data.split('_')[1])
    location_index = int(callback_query.data.split('_')[2])
    location_page = int(callback_query.data.split('_')[3])
    page_id = int(callback_query.data.split('_')[4])
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
        city_index=city_index, location_page=location_page,
        location_index=location_index, page=page)
    text = make_text(gym)
    return (text, markup)


def make_markup(gym_id, user_id, city_index, location_page, location_index, page):
    back_button_callback = f'gym_city_{city_index}_{location_page}'
    callback_prefix = f'gym_{city_index}_{location_index}_{location_page}_'
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
