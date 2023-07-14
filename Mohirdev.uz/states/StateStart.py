from aiogram.dispatcher.filters.state import StatesGroup, State


class StateStart(StatesGroup):
    Kurs = State()
    Kasb = State()