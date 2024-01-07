from aiogram import Router, F
from emoji import emojize as emj
from keyboards.reply_keyboards import main_kb
from aiogram.types import Message
from utils.strings import menu_text

router = Router()


@router.message(F.text == emj(":clipboard:") + "Посмотреть меню")
async def send_menu(message: Message):
    await message.reply(menu_text, reply_markup=main_kb)
