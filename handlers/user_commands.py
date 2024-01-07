from config_reader import settings
from keyboards.inline_keyboards import admin_kb
from utils.strings import registration_msg, welcome_msg
from keyboards.reply_keyboards import main_kb, get_phone_kb
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from data.database_connection import conn, cur
from datetime import date
from utils.helpers import make_id_list
from utils.states import PhoneState
from utils.paths import fratelli_logo, registration_photo

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    id_list = make_id_list()
    if user_id in id_list:
        await message.answer_photo(fratelli_logo, welcome_msg, reply_markup=main_kb)
    else:
        await message.answer_photo(registration_photo, registration_msg, reply_markup=get_phone_kb)
        await state.set_state(PhoneState.registration)


@router.message(PhoneState.registration)
async def registration(message: Message, state: FSMContext):
    user_id = message.from_user.id
    phone_number = message.contact.phone_number
    full_name = message.from_user.full_name

    cur.execute('INSERT INTO users (user_id, phone_number, registration_date, full_name) VALUES (?,?,?,?)',
                (user_id, phone_number, date.today(), full_name))
    conn.commit()

    await state.clear()
    await message.answer_photo(fratelli_logo, welcome_msg, reply_markup=main_kb)


@router.message(F.text == "/admin")
async def admin(message: Message):
    if str(message.from_user.id) == settings.admin_id:
        await message.reply("Добро пожаловать в админ панель", reply_markup=admin_kb)
    else:
        print(message.from_user.id)
        print(settings.admin_id)
        await message.reply("Вы не являетесь администратором")


@router.callback_query(lambda c: c.data == 'delete_my_user_id')
async def delete_my_user_id(callback_query: CallbackQuery):
    cur.execute(f"DELETE FROM users WHERE user_id = {settings.admin_id}")
    conn.commit()
    await callback_query.message.answer("Удаление id прошло успешно!")
    await callback_query.message.delete()


@router.callback_query(lambda c: c.data == 'clear_reviews')
async def reservation_visitors(callback_query: CallbackQuery):
    cur.execute("DELETE FROM reviews WHERE id >= 11")
    conn.commit()
    await callback_query.message.answer("Удаление отзывов прошло успешно!")
    await callback_query.message.delete()


@router.callback_query(lambda c: c.data == 'hide_admin')
async def reservation_visitors(callback_query: CallbackQuery):
    await callback_query.message.delete()
