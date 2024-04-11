import asyncio

from aiogram import Bot, Dispatcher
from config.config import load_config, Config
from handlers import user_handler
from aiogram import Dispatcher


async def main():
    config: Config = load_config()
    dp = Dispatcher()

    bot = Bot(token=config.tg_bot)

    dp.include_router(user_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
