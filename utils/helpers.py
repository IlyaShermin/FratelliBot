from aiogram.types import CallbackQuery
from data.database_connection import cur
import datetime
import re
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv


def review_text_shaper(current_position: int, reviews: list):
    review_text = f"Отзыв №: [{current_position+1}/{len(reviews)}]\n" + reviews[current_position][2]
    return review_text


def get_dish_info(callback_query: CallbackQuery):
    pattern = fr"text='([^']+\s{callback_query.data})'"
    match = re.search(pattern, str(callback_query.message.reply_markup.inline_keyboard))
    result = match.group(1)
    return result


def make_cart(cart_list: list, total_price: int):
    cart = "Корзина:\nДоставка курьером: 300р.\n"
    for i in cart_list:
        cart += i + "\n"
    cart += f"\nОбщая стоимость: {total_price} р."
    return cart


def get_dates():
    dates = []
    now = datetime.datetime.now()
    if now.hour >= 21 and now.minute >= 30:
        today = datetime.date.today() + datetime.timedelta(days=1)
    else:
        today = datetime.date.today()
    for i in range(14):
        date = today + datetime.timedelta(days=i)
        date_list = [date.day, date.month, date.year]
        dates.append(date_list)
    return dates


def make_id_list():
    user_id_column = list(cur.execute("SELECT user_id FROM users"))
    id_list = []
    for i in user_id_column:
        id_list.append(i[0])
    return id_list


def send_electronic_check(delivery_id: str,
                          date: str,
                          time: str,
                          shipping_address: str,
                          name: str,
                          phone_number: str,
                          receiver_email: str,
                          cart: str):
    load_dotenv()
    sender = os.environ.get('EMAIl_ADDRESS')
    password = os.environ.get('GMAIL_APP_PASSWORD')
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)

    check_text = (f"Электронный чек № {delivery_id}\n"
                  f"Дата и время оформления заказа: {date} {time}\n"
                  f"Адресс получателя: {shipping_address}\n"
                  f"Имя: {name}\n"
                  f"Телефон: {phone_number}\n"
                  f"Почта: {receiver_email}\n"
                  f"{cart}\n\n"
                  f"Ссылка на нашего бота: https://t.me/fratelli_restaraunt_bot\n"
                  f"Телефон для обратной связи: 79255135188")

    msg = MIMEText(check_text)
    msg["Subject"] = f"Электронный чек № {delivery_id}"
    server.sendmail(sender, receiver_email, msg.as_string())


def check_phone_number(message):
    pattern = r'(([\+]?[7|8][\s\-(]?[9][0-9]{2}[\s\-\)]?)?([\d]{3})[\s\-]?([\d]{2})[\s\-]?([\d]{2}))'
    return bool(re.fullmatch(pattern, message))


def check_time_format(message):
    pattern = r'^(1[2-9]|2[01]):[0-5][0-9]$'
    if re.fullmatch(pattern, message):
        hour = int(message[:2])
        minute = int(message[3:])
        if hour == 21 and minute > 30:
            return False
        elif hour > 21:
            return False
        elif hour < 12:
            return False
        else:
            return True
    else:
        return False


def check_user_id(user_id):
    cur.execute("SELECT * FROM reservations WHERE user_id = ?", (user_id,))
    rows = cur.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False


def reservation_info_msg_shaper(name: str, phone_number: str, date: str, time: str, visitors: int):
    return (f"Имя: {name}\n"
            f"Номер телефона: {phone_number}\n"
            f"Дата: {date}\n"
            f"Время: {time}\n"
            f"Количество гостей: {visitors}")
