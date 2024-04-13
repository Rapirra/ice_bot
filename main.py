import asyncio
from bot import dispatcher as dp, bot, chat_id
from handlers import router


async def processing_auto_message():
    await bot.send_message(chat_id, 'hi Banshee')


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    while True:
        await processing_auto_message()
        await asyncio.sleep(5)


asyncio.run(main())
