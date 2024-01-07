import datetime
from aiogram import Router, F
from emoji import emojize as emj
from keyboards.reply_keyboards import main_kb
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery, ShippingQuery, ShippingOption
from keyboards.inline_keyboards import (delivery_kb, snacks_kb, risotto_kb, soups_kb, salads_kb, pizza_kb, paste_kb,
                                        hot_dishes_kb, desserts_kb, tea_kb, coffee_kb)
from utils.helpers import get_dish_info, make_cart, send_electronic_check
from config_reader import settings
from utils.paths import payment_pic
from utils.strings import min_delivery_price_msg, payment_title, payment_description_msg, wrong_address_msg, \
    successful_payment_msg
from data.database_connection import conn, cur

router = Router()

global total_price
global cart_list
global make_delivery_msg_id


@router.message(F.text == emj(":delivery_truck:") + "Сделать заказ на дом")
async def send_delivery_kb(message: Message):
    global make_delivery_msg_id
    make_delivery_msg_id = message.message_id
    await message.reply(text=make_cart([], 300), reply_markup=delivery_kb)
    global total_price
    total_price = 300
    global cart_list
    cart_list = []


@router.callback_query(lambda c: c.data == "snacks")
async def get_snacks(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=snacks_kb)


@router.callback_query(lambda c: c.data == "risotto")
async def get_risotto(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=risotto_kb)


@router.callback_query(lambda c: c.data == "soups")
async def get_soups(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=soups_kb)


@router.callback_query(lambda c: c.data == "salads")
async def get_salads(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=salads_kb)


@router.callback_query(lambda c: c.data == "pizza")
async def get_pizza(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=pizza_kb)


@router.callback_query(lambda c: c.data == "paste")
async def get_paste(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=paste_kb)


@router.callback_query(lambda c: c.data == "hot_dishes")
async def get_hot_dishes(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=hot_dishes_kb)


@router.callback_query(lambda c: c.data == "desserts")
async def get_desserts(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=desserts_kb)


@router.callback_query(lambda c: c.data == "tea")
async def get_tea(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=tea_kb)


@router.callback_query(lambda c: c.data == "coffee")
async def get_coffee(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=coffee_kb)


@router.callback_query(lambda c: c.data == "back_to_delivery_menu")
async def get_back_to_delivery_menu(callback_query: CallbackQuery):
    from bot import bot
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=delivery_kb)


@router.callback_query(lambda c: c.data.endswith("р."))
async def update_menu(callback_query: CallbackQuery):
    from bot import bot
    global total_price
    global cart_list
    dish_name = get_dish_info(callback_query)
    cart_list.append(dish_name)
    total_price += int(callback_query.data[:callback_query.data.index('р')])

    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=delivery_kb)


@router.callback_query(lambda c: c.data == "clear_cart")
async def clear_cart(callback_query: CallbackQuery):
    global cart_list
    if not cart_list:
        pass
    else:
        from bot import bot
        global total_price
        total_price = 0
        cart_list = []

        await bot.answer_callback_query(callback_query.id)
        await callback_query.message.edit_text(text=make_cart(cart_list, total_price), reply_markup=delivery_kb)


@router.callback_query(lambda c: c.data == "cancel_delivery")
async def cancel_delivery(callback_query: CallbackQuery):
    await callback_query.message.delete()


@router.callback_query(lambda c: c.data == "make_delivery")
async def make_delivery(callback_query: CallbackQuery):
    from bot import bot
    global total_price
    global cart_list

    await bot.answer_callback_query(callback_query.id)

    if total_price < 1500:
        await callback_query.message.reply(text=min_delivery_price_msg)
    else:
        await bot.send_invoice(
            chat_id=callback_query.message.chat.id,
            title=payment_title,
            description=payment_description_msg,
            payload="payload",
            provider_token=settings.payment_token,
            currency="RUB",
            prices=[
                LabeledPrice(
                    label="Заказ",
                    amount=(total_price-300)*100
                )
            ],
            max_tip_amount=total_price*20,
            suggested_tip_amounts=[total_price*5, total_price*10, total_price*15, total_price*20],
            start_parameter="True",
            provider_data=None,
            photo_url=payment_pic,
            photo_size=100,
            photo_width=800,
            photo_height=400,
            need_name=True,
            need_phone_number=True,
            need_email=True,
            need_shipping_address=True,
            is_flexible=True,
            disable_notification=False,
            protect_content=False,
            reply_to_message_id=callback_query.message.message_id,
            allow_sending_without_reply=True
        )


MSK_SHIPPING = ShippingOption(
    id="moscow",
    title="Доставка курьером в пределах Москвы",
    prices=[
        LabeledPrice(
            label="Доставка курьером",
            amount=300*100
        )
    ]
)


@router.shipping_query(lambda query: True)
async def shipping_check(shipping_query: ShippingQuery):
    from bot import bot
    shipping_options = []
    if (shipping_query.shipping_address.country_code != "RU") or (shipping_query.shipping_address.city != "Москва"):
        return await bot.answer_shipping_query(shipping_query.id, ok=False, error_message=wrong_address_msg)
    else:
        shipping_options.append(MSK_SHIPPING)

    await bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options)


@router.pre_checkout_query(lambda query: True)
async def get_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    from bot import bot
    global cart_list
    global total_price

    shipping_address = (f"{pre_checkout_query.order_info.shipping_address.city} "
                        f"{pre_checkout_query.order_info.shipping_address.street_line1}")

    cur.execute('INSERT INTO deliveries (delivery_id, user_id, order_date, order_time, shipping_address, client_name, '
                'phone_number, receiver_email, total_price) VALUES (?,?,?,?,?,?,?,?,?)',
                (pre_checkout_query.id, pre_checkout_query.from_user.id, datetime.date.today().strftime('%Y-%m-%d'),
                 datetime.datetime.now().time().strftime('%H:%M'), shipping_address, pre_checkout_query.order_info.name,
                 pre_checkout_query.order_info.phone_number, pre_checkout_query.order_info.email,
                 pre_checkout_query.total_amount/100))
    conn.commit()

    send_electronic_check(delivery_id=pre_checkout_query.id,
                          date=datetime.date.today().strftime('%d.%m.%Y'),
                          time=datetime.datetime.now().time().strftime('%H:%M'),
                          shipping_address=shipping_address,
                          name=pre_checkout_query.order_info.name,
                          phone_number=pre_checkout_query.order_info.phone_number,
                          receiver_email=pre_checkout_query.order_info.email,
                          cart=make_cart(cart_list, total_price))

    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@router.message(F.successful_payment)
async def successful_payment(message: Message):
    await message.reply(successful_payment_msg, reply_markup=main_kb)
