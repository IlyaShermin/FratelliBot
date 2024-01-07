from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize as emj
from utils.strings import cancel_msg, return_msg, choose_action_from_menu_msg, provide_phone_number_msg

get_phone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=emj(":telephone_receiver:") + "Предоставить номер телефона", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder=provide_phone_number_msg
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=emj(":clipboard:") + "Посмотреть меню"),
            KeyboardButton(text=emj(":delivery_truck:") + "Сделать заказ на дом")
        ],
        [
            KeyboardButton(text=emj(":stopwatch:") + "Резервирование"),
            KeyboardButton(text=emj(":hundred_points:") + "Отзывы")
        ],
        [
            KeyboardButton(text=emj(":information:") + "Информация")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder=choose_action_from_menu_msg
)

reservation_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=emj(":scroll:") + "Правила бронирования"),
            KeyboardButton(text=emj(":hotel:") + "Планировка зала")

        ],
        [
            KeyboardButton(text=emj(":ten_o’clock:") + "Забронировать столик"),
            KeyboardButton(text=emj(":check_mark_button:") + "Посмотреть бронь"),
            KeyboardButton(text=emj(":wastebasket:") + "Снять бронь")
        ],
        [
            KeyboardButton(text=emj(":left_arrow:") + "В главное меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder=choose_action_from_menu_msg
)

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=cancel_msg)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

cancel_and_return_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=return_msg)

        ],
        [
            KeyboardButton(text=cancel_msg)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

reviews_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=emj(":hundred_points:") + "Оставить отзыв"),
            KeyboardButton(text=emj(":eyes:") + "Посмотреть отзывы")
        ],
        [
            KeyboardButton(text=emj(":left_arrow:") + "В главное меню")

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder=choose_action_from_menu_msg
)

delete_reservation_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=emj(":wastebasket:") + "Да, cнять бронь"),
            KeyboardButton(text=emj(":cross_mark:") + "Оставить бронь")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder=choose_action_from_menu_msg
)
