from keyboards.reply_keyboards import reviews_kb, main_kb, cancel_kb
from keyboards.inline_keyboards import watch_reviews_kb
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from utils.states import ReviewForm
from data.database_connection import conn, cur
from emoji import emojize as emj
from bot import bot
from utils.helpers import review_text_shaper
from utils.strings import choose_action_from_menu_msg, make_review_msg, wrong_review_msg, thanks_for_review_msg, \
    review_absence_msg, back_to_main_menu_msg, cancel_msg

router = Router()

global current_position
global reviews


@router.message(F.text == emj(":hundred_points:") + "Отзывы")
async def get_review_menu(message: Message):
    await message.reply(choose_action_from_menu_msg, reply_markup=reviews_kb)


@router.message(F.text == emj(":hundred_points:") + "Оставить отзыв")
async def make_review(message: Message, state: FSMContext):
    await state.set_state(ReviewForm.text)
    await message.reply(make_review_msg, reply_markup=cancel_kb)


@router.message(ReviewForm.text)
async def leave_review_text(message: Message, state: FSMContext):
    review_text = message.text
    if review_text == cancel_msg:
        await message.reply(choose_action_from_menu_msg, reply_markup=reviews_kb)
        await state.clear()
        return
    elif len(review_text) > 500 or len(review_text) < 100:
        await message.reply(wrong_review_msg)
        return

    cur.execute('INSERT INTO reviews (user_id, review_text) VALUES (?,?)', (message.from_user.id, review_text,))
    conn.commit()
    await message.reply(thanks_for_review_msg, reply_markup=reviews_kb)
    await state.clear()


@router.message(F.text == emj(":eyes:") + "Посмотреть отзывы")
async def watch_reviews(message: Message):
    global current_position
    global reviews
    current_position = 0
    reviews = list(cur.execute("SELECT * FROM reviews"))

    if not reviews:
        await message.reply(review_absence_msg, reply_markup=reviews_kb)

    await message.reply(review_text_shaper(current_position, reviews), reply_markup=watch_reviews_kb)


@router.callback_query(lambda c: c.data == 'previous_review')
async def process_prev(callback_query: CallbackQuery):
    global current_position
    global reviews
    if current_position + 1 > 1:
        current_position -= 1
    else:
        current_position = len(reviews) - 1
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(review_text_shaper(current_position, reviews), reply_markup=watch_reviews_kb)


@router.callback_query(lambda c: c.data == 'next_review')
async def process_next(callback_query: CallbackQuery):
    global current_position
    global reviews
    if current_position + 1 < len(reviews):
        current_position += 1
    else:
        current_position = 0
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(review_text_shaper(current_position, reviews), reply_markup=watch_reviews_kb)


@router.callback_query(lambda c: c.data == 'hide_reviews')
async def hide_reviews_message(callback_query: CallbackQuery):
    await callback_query.message.delete()


@router.message(F.text == emj(":left_arrow:") + "В главное меню")
async def reviews_to_main_manu(message: Message):
    await message.reply(back_to_main_menu_msg, reply_markup=main_kb)
