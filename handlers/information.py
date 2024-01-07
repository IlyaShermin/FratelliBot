from aiogram import Router, F
from emoji import emojize as emj
from keyboards.reply_keyboards import main_kb
from aiogram.types import Message
from utils.paths import full_name_logo
from utils.strings import information_msg

router = Router()


@router.message(F.text == emj(":information:") + "Информация")
async def send_information(message: Message):
    await message.reply_photo(full_name_logo, information_msg, reply_markup=main_kb)
