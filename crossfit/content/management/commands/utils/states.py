from aiogram.dispatcher.filters.state import State, StatesGroup


class SearchPlaceState(StatesGroup):
    SEARCHING = State()
