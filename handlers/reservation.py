from utils.strings import cancel_msg, return_msg, choose_action_from_menu_msg, \
    too_long_name_msg, input_name_msg, already_have_reservation_msg, input_phone_number_msg, \
    wrong_phone_number_msg, input_time_msg, wrong_time_msg, choose_date_msg, choose_visitors_msg, \
    successful_reservation_msg, reservation_absence_msg, delete_reservation_msg, back_to_main_menu_msg, \
    reservation_rules, are_you_sure
from utils.helpers import check_phone_number, check_time_format, check_user_id, reservation_info_msg_shaper
from keyboards.reply_keyboards import reservation_kb, cancel_kb, cancel_and_return_kb, main_kb, delete_reservation_kb
from keyboards.inline_keyboards import dates_kb, visitors_kb
from utils.states import Reservation, DeleteReservation
from aiogram.types import Message, CallbackQuery
from data.database_connection import conn, cur
from utils.paths import reservation_layout
from aiogram.fsm.context import FSMContext
from emoji import emojize as emj
from aiogram import Router, F


router = Router()


@router.message(F.text == emj(":stopwatch:") + "Резервирование")
async def reservation_menu(message: Message):
    await message.answer(choose_action_from_menu_msg, reply_markup=reservation_kb)


@router.message(F.text == emj(":ten_o’clock:") + "Забронировать столик")
async def make_reservation(message: Message, state: FSMContext):
    if check_user_id(message.from_user.id):
        await message.reply(text=already_have_reservation_msg, reply_markup=reservation_kb)
    else:
        await state.set_state(Reservation.name)
        await message.reply(text=input_name_msg, reply_markup=cancel_kb)


@router.message(Reservation.name)
async def reservation_name(message: Message, state: FSMContext):
    if message.text == cancel_msg:
        await state.clear()
        await message.reply(choose_action_from_menu_msg, reply_markup=reservation_kb)
    elif len(message.text) > 20:
        await message.reply(too_long_name_msg, reply_markup=cancel_kb)
    else:
        await state.update_data(name=message.text)
        await state.set_state(Reservation.phone_number)
        await message.answer(text=input_phone_number_msg, reply_markup=cancel_and_return_kb)


@router.message(Reservation.phone_number)
async def reservation_phone_number(message: Message, state: FSMContext):
    if message.text == cancel_msg:
        await state.clear()
        await message.reply(choose_action_from_menu_msg, reply_markup=reservation_kb)
    elif message.text == return_msg:
        await message.reply(text=input_name_msg, reply_markup=cancel_kb)
        await state.set_state(Reservation.name)
    elif not check_phone_number(message.text):
        await message.reply(wrong_phone_number_msg, reply_markup=cancel_and_return_kb)
    else:
        await state.update_data(phone_number=message.text)
        await state.set_state(Reservation.time)
        await message.reply(text=input_time_msg, reply_markup=cancel_and_return_kb)


@router.message(Reservation.time)
async def reservation_time(message: Message, state: FSMContext):
    if message.text == cancel_msg:
        await state.clear()
        await message.reply(choose_action_from_menu_msg, reply_markup=reservation_kb)
    elif message.text == return_msg:
        await message.reply(text=input_phone_number_msg, reply_markup=cancel_and_return_kb)
        await state.set_state(Reservation.phone_number)
    elif not check_time_format(message.text):
        await message.reply(wrong_time_msg, reply_markup=cancel_and_return_kb)
    else:
        await state.update_data(time=message.text)
        await state.set_state(Reservation.date)
        await message.answer(text=choose_date_msg, reply_markup=dates_kb)


@router.callback_query(Reservation.date)
async def reservation_date(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.data == "cancel":
        await state.clear()
        await callback_query.message.delete()
        await callback_query.message.answer(choose_action_from_menu_msg, reply_markup=reservation_kb)
    elif callback_query.data == "return":
        await callback_query.message.delete()
        await callback_query.message.answer(text=input_time_msg, reply_markup=cancel_and_return_kb)
        await state.set_state(Reservation.time)
    else:
        await state.update_data(date=callback_query.data)
        await callback_query.message.edit_text(text=choose_visitors_msg, reply_markup=visitors_kb)
        await state.set_state(Reservation.visitors)


@router.callback_query(Reservation.visitors)
async def reservation_visitors(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.data == "cancel":
        await state.clear()
        await callback_query.message.delete()
        await callback_query.message.answer(choose_action_from_menu_msg, reply_markup=reservation_kb)
    elif callback_query.data == "return":
        await callback_query.message.edit_reply_markup(choose_date_msg, reply_markup=dates_kb)
        await state.set_state(Reservation.date)
    else:
        await state.update_data(visitors=callback_query.data)
        reservation_data = await state.get_data()
        cur.execute(
            'INSERT INTO reservations (user_id, name, phone_number, date, time, '
            'visitors) VALUES (?,?,?,?,?,?)',
            (callback_query.from_user.id, reservation_data["name"], reservation_data["phone_number"],
             reservation_data["date"], reservation_data["time"], reservation_data["visitors"]))
        conn.commit()
        await callback_query.message.delete()
        await state.clear()
        await callback_query.message.answer(successful_reservation_msg, reply_markup=reservation_kb)


@router.message(F.text == emj(":check_mark_button:") + "Посмотреть бронь")
async def watch_reservation(message: Message):
    if check_user_id(message.from_user.id):
        cur.execute("SELECT * FROM reservations WHERE user_id = ?", (message.from_user.id,))
        row = cur.fetchone()
        await message.reply(reservation_info_msg_shaper(row[2], row[3], row[4], row[5], row[6]),
                            reply_markup=reservation_kb)
    else:
        await message.reply(reservation_absence_msg, reply_markup=reservation_kb)


@router.message(F.text == emj(":wastebasket:") + "Снять бронь")
async def delete_reservation(message: Message,  state: FSMContext):
    if check_user_id(message.from_user.id):
        await message.reply(are_you_sure, reply_markup=delete_reservation_kb)
        await state.set_state(DeleteReservation.delete)
    else:
        await message.reply(reservation_absence_msg, reply_markup=reservation_kb)


@router.message(DeleteReservation.delete)
async def delete_reservation_sure(message: Message, state: FSMContext):
    if message.text == emj(":wastebasket:") + "Да, cнять бронь":
        await state.clear()
        cur.execute("DELETE FROM reservations WHERE user_id = ?", (message.from_user.id,))
        conn.commit()
        await message.reply(delete_reservation_msg, reply_markup=reservation_kb)
    else:
        await state.clear()
        await message.answer(choose_action_from_menu_msg, reply_markup=reservation_kb)


@router.message(F.text == emj(":scroll:") + "Правила бронирования")
async def get_reservation_rules(message: Message):
    await message.reply(reservation_rules, reply_markup=reservation_kb)


@router.message(F.text == emj(":hotel:") + "Планировка зала")
async def get_reservation_layout(message: Message):
    await message.reply_photo(reservation_layout, reply_markup=reservation_kb)


@router.message(F.text == emj(":left_arrow:") + "В главное меню")
async def reservation_to_main_manu(message: Message):
    await message.reply(back_to_main_menu_msg, reply_markup=main_kb)
