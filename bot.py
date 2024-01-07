from aiogram import Bot, Dispatcher
import asyncio
from handlers import reservation, user_commands, reviews, delivery, information, menu
from config_reader import settings

bot = Bot(settings.bot_token, parse_mode="HTML")
dp = Dispatcher()


async def main():
    dp.include_routers(
        user_commands.router,
        reservation.router,
        reviews.router,
        delivery.router,
        information.router,
        menu.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
