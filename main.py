import asyncio

from aiogram.fsm.context import FSMContext
from classesStructure.classStructures import processing_auto_message
from bot import dispatcher as dp, bot, chat_id
from handlers import router, SubscriptionStates
from classesStructure.classStructures import botMessage, RegisterMessage
from models.auth import client



async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    while chat_id:
        await processing_auto_message(chat_id, bot, botMessage)
        await asyncio.sleep(5)


asyncio.run(main())
