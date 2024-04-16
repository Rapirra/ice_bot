import asyncio

from bot import dispatcher as dp, bot
from handlers import router


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


asyncio.run(main())
