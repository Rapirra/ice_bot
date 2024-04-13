import asyncio

from aiogram.fsm.context import FSMContext

from bot import dispatcher as dp, bot, chat_id
from handlers import router, SubscriptionStates


async def processing_auto_message(state: FSMContext):
    data = await state.get_data()
    subscription_data = data.get('subscription_data', 'No data')
    await bot.send_message(chat_id, f"hi banshee: {subscription_data}")


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    while SubscriptionStates.sendingResponse:
        await processing_auto_message()
        await asyncio.sleep(5)


asyncio.run(main())
