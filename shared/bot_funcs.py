from bot import bot
from classesStructure.classStructures import botMessage
from keyboards.inline_keyboards.pickup_kb import build_first_kb


async def callBot(obj, chat_id, delivery_btns):
    if not botMessage.deliveryBtns:
        await bot.send_message(chat_id=chat_id, text="Order has been closed")
    else:
        await bot.send_message(chat_id=chat_id, text=obj, reply_markup=build_first_kb(delivery_btns))


