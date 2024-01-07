from aiogram.fsm.state import StatesGroup, State


class ReviewForm(StatesGroup):
    text = State()


class PhoneState(StatesGroup):
    registration = State()


class Reservation(StatesGroup):
    name = State()
    phone_number = State()
    time = State()
    date = State()
    visitors = State()


class DeleteReservation(StatesGroup):
    delete = State()
