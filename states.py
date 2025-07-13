from aiogram.fsm.state import StatesGroup, State


class MainMenuStates(StatesGroup):
    active = State()
    demobilized = State()