from aiogram.fsm.state import StatesGroup, State


class ActiveState(StatesGroup):
    start = State()
    show_more = State()


class DemobilizedState(StatesGroup):
    start = State()
    show_more = State()


class VeteranState(StatesGroup):
    start = State()
    show_more = State()


class FamilyState(StatesGroup):
    start = State()
    show_more = State()


class CandidateState(StatesGroup):
    start = State()
    show_more = State()