from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.helpers import get_dates
from emoji import emojize as emj
from utils.strings import cancel_msg, return_msg

watch_reviews_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=emj(":left_arrow:"), callback_data="previous_review"),
            InlineKeyboardButton(text=emj(":right_arrow:"), callback_data="next_review")
        ],
        [
            InlineKeyboardButton(text="Скрыть отзывы", callback_data="hide_reviews")
        ]
    ]
)

delivery_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=emj(":canned_food:") + "Закуски", callback_data="snacks")
        ],
        [
            InlineKeyboardButton(text=emj(":cheese_wedge:") + "Ризотто", callback_data="risotto")
        ],
        [
            InlineKeyboardButton(text=emj(":green_salad:") + "Салаты", callback_data="salads")
        ],
        [
            InlineKeyboardButton(text=emj(":pot_of_food:") + "Супы", callback_data="soups")
        ],
        [
            InlineKeyboardButton(text=emj(":pizza:") + "Пицца", callback_data="pizza")
        ],
        [
            InlineKeyboardButton(text=emj(":Italy:") + "Паста", callback_data="paste")
        ],
        [
            InlineKeyboardButton(text=emj(":fork_and_knife_with_plate:") + "Горчие блюда", callback_data="hot_dishes")
        ],
        [
            InlineKeyboardButton(text=emj(":shortcake:") + "Десерты", callback_data="desserts")
        ],
        [
            InlineKeyboardButton(text=emj(":teapot:") + "Чай", callback_data="tea")
        ],
        [
            InlineKeyboardButton(text=emj(":teacup_without_handle:") + "Коффе", callback_data="coffee")
        ],
        [
            InlineKeyboardButton(text=emj(":wastebasket:") + "Очистить корзину", callback_data="clear_cart")
        ],
        [
            InlineKeyboardButton(text=cancel_msg, callback_data="cancel_delivery")
        ],
        [
            InlineKeyboardButton(text=emj(":check_mark_button:") + "Готово", callback_data="make_delivery")
        ]
    ]
)

snacks_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Батат фри с трюфельно-сырным соусом 472р.", callback_data="472р.")
        ],
        [
            InlineKeyboardButton(text="Маринованные оливки 209р.", callback_data="209р.")
        ],
        [
            InlineKeyboardButton(text="Брускетта с цыпленком и соусом Руй 334р.", callback_data="334р.")
        ],
        [
            InlineKeyboardButton(text="Тартар из лосося с гуакамоле и лимоном 688р.", callback_data="688р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

risotto_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ризотто с белыми грибами 464р.", callback_data="464р.")
        ],
        [
            InlineKeyboardButton(text="Ризотто со страчателлой и тыквой 374р.", callback_data="374р.")
        ],
        [
            InlineKeyboardButton(text="Ризотто с креветками 462р.", callback_data="462р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

salads_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Овощной салат с оливками и луковым песто 187р.", callback_data="187р.")
        ],
        [
            InlineKeyboardButton(text="Салат Цезарь с креветками 462р.", callback_data="462р.")
        ],
        [
            InlineKeyboardButton(text="Салат с цыпленком и соусом руй 396р.", callback_data="396р.")
        ],
        [
            InlineKeyboardButton(text="Буррата с узбекскими томатами 656р.", callback_data="656р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

soups_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Грибной крем-суп 192р.", callback_data="192р.")
        ],
        [
            InlineKeyboardButton(text="Домашний куриный суп с лапшой 143р.", callback_data="143р.")
        ],
        [
            InlineKeyboardButton(text="Тыквенный кремсуп с лососем 464р.", callback_data="464р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

pizza_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Барбекю 476р.", callback_data="476р.")
        ],
        [
            InlineKeyboardButton(text="Карбонара 588р.", callback_data="588р.")
        ],
        [
            InlineKeyboardButton(text="Маргарита 432р.", callback_data="432р.")
        ],
        [
            InlineKeyboardButton(text="Пепперони 572р.", callback_data="572р.")
        ],
        [
            InlineKeyboardButton(text="7 сыров 689р.", callback_data="689р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

paste_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Равиоли с курицей, грибами 443р.", callback_data="443р.")
        ],
        [
            InlineKeyboardButton(text="Равиоли с говядиной и зеленым горошком 436р.", callback_data="436р.")
        ],
        [
            InlineKeyboardButton(text="Равиоли с креветками и кальмаром 484р.", callback_data="484р.")
        ],
        [
            InlineKeyboardButton(text="Фетучини томаты черри и моцарелла 472р.", callback_data="472р.")
        ],
        [
            InlineKeyboardButton(text="Фетучини с бураттой, песто и кедровым орехом 465р.", callback_data="465р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

hot_dishes_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Бифштекс с грибным соусом 582р.", callback_data="582р.")
        ],
        [
            InlineKeyboardButton(text="Бургер с соусом 1000 островов 629р.", callback_data="629р.")
        ],
        [
            InlineKeyboardButton(text="Стейк из лосося 964р.", callback_data="964р.")
        ],
        [
            InlineKeyboardButton(text="Жаркое из кальмара с томатами и беби картофелем 648р.", callback_data="648р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

desserts_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сорбет лимон 134р.", callback_data="134р.")
        ],
        [
            InlineKeyboardButton(text="Сорбет манго 145р.", callback_data="145р.")
        ],
        [
            InlineKeyboardButton(text="Фисташковое морожение 142р.", callback_data="142р.")
        ],
        [
            InlineKeyboardButton(text="Шоколадное мороженое 181р.", callback_data="181р.")
        ],
        [
            InlineKeyboardButton(text="Шоколадные макарунс 428р.", callback_data="428р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

coffee_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Эспрессо 152р.", callback_data="152р.")
        ],
        [
            InlineKeyboardButton(text="Двойной эспрессо 234р.", callback_data="234р.")
        ],
        [
            InlineKeyboardButton(text="Американо 193р.", callback_data="193р.")
        ],
        [
            InlineKeyboardButton(text="Капучино 242р.", callback_data="242р.")
        ],
        [
            InlineKeyboardButton(text="Латте 251р.", callback_data="251р.")
        ],
        [
            InlineKeyboardButton(text="Флет Уайт 284р.", callback_data="284р.")
        ],
        [
            InlineKeyboardButton(text="Классический Раф 328р.", callback_data="328р.")
        ],
        [
            InlineKeyboardButton(text="Лавандовый Раф 325р.", callback_data="325р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

tea_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Молочный улун 270р.", callback_data="270р.")
        ],
        [
            InlineKeyboardButton(text="Жасминовая жемчужина 275р.", callback_data="275р.")
        ],
        [
            InlineKeyboardButton(text="Гречишный чай 280р.", callback_data="280р.")
        ],
        [
            InlineKeyboardButton(text="Ассам Мокалбари 265р.", callback_data="265р.")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="back_to_delivery_menu")
        ]
    ]
)

dates = get_dates()

dates_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f"{dates[0][0]}.{dates[0][1]}", callback_data=f"{dates[0][2]}-{dates[0][1]}-{dates[0][0]}"),
            InlineKeyboardButton(text=f"{dates[1][0]}.{dates[1][1]}", callback_data=f"{dates[1][2]}-{dates[1][1]}-{dates[1][0]}"),
            InlineKeyboardButton(text=f"{dates[2][0]}.{dates[2][1]}", callback_data=f"{dates[2][2]}-{dates[2][1]}-{dates[2][0]}")
        ],
        [
            InlineKeyboardButton(text=f"{dates[3][0]}.{dates[3][1]}", callback_data=f"{dates[3][2]}-{dates[3][1]}-{dates[3][0]}"),
            InlineKeyboardButton(text=f"{dates[4][0]}.{dates[4][1]}", callback_data=f"{dates[4][2]}-{dates[4][1]}-{dates[4][0]}"),
            InlineKeyboardButton(text=f"{dates[5][0]}.{dates[5][1]}", callback_data=f"{dates[5][2]}-{dates[5][1]}-{dates[5][0]}")
        ],
        [
            InlineKeyboardButton(text=f"{dates[6][0]}.{dates[6][1]}", callback_data=f"{dates[6][2]}-{dates[6][1]}-{dates[6][0]}"),
            InlineKeyboardButton(text=f"{dates[7][0]}.{dates[7][1]}", callback_data=f"{dates[7][2]}-{dates[7][1]}-{dates[7][0]}"),
            InlineKeyboardButton(text=f"{dates[8][0]}.{dates[8][1]}", callback_data=f"{dates[8][2]}-{dates[8][1]}-{dates[8][0]}")
        ],
        [
            InlineKeyboardButton(text=f"{dates[9][0]}.{dates[9][1]}", callback_data=f"{dates[9][2]}-{dates[9][1]}-{dates[9][0]}"),
            InlineKeyboardButton(text=f"{dates[10][0]}.{dates[10][1]}", callback_data=f"{dates[10][2]}-{dates[10][1]}-{dates[10][0]}"),
            InlineKeyboardButton(text=f"{dates[11][0]}.{dates[11][1]}", callback_data=f"{dates[11][2]}-{dates[11][1]}-{dates[11][0]}")
        ],
        [
            InlineKeyboardButton(text=f"{dates[12][0]}.{dates[12][1]}", callback_data=f"{dates[12][2]}-{dates[12][1]}-{dates[12][0]}"),
            InlineKeyboardButton(text=f"{dates[13][0]}.{dates[13][1]}", callback_data=f"{dates[13][2]}-{dates[13][1]}-{dates[13][0]}")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="return"),
            InlineKeyboardButton(text=cancel_msg, callback_data="cancel")
        ]
    ]
)

visitors_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=emj(":keycap_1:"), callback_data="1"),
            InlineKeyboardButton(text=emj(":keycap_2:"), callback_data="2"),
            InlineKeyboardButton(text=emj(":keycap_3:"), callback_data="3")
        ],
        [
            InlineKeyboardButton(text=emj(":keycap_4:"), callback_data="4"),
            InlineKeyboardButton(text=emj(":keycap_5:"), callback_data="5"),
            InlineKeyboardButton(text=emj(":keycap_6:"), callback_data="6")
        ],
        [
            InlineKeyboardButton(text=return_msg, callback_data="return"),
            InlineKeyboardButton(text=cancel_msg, callback_data="cancel")
        ]
    ]
)

admin_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Удалить user_id", callback_data="delete_my_user_id"),
            InlineKeyboardButton(text="Очистить отзывы", callback_data="clear_reviews")

        ],
        [
            InlineKeyboardButton(text="Очистить брони", callback_data="clear_reservations"),
            InlineKeyboardButton(text="Очистить заказы", callback_data="clear_deliveries")
        ],
        [
            InlineKeyboardButton(text="Скрыть панель", callback_data="hide_admin")
        ]
    ]
)
