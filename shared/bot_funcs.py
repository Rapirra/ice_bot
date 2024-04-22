from bot import bot
from classesStructure.classStructures import botMessage
from keyboards.inline_keyboards.pickup_kb import build_first_kb


async def callBot(obj, chat_id, delivery_btns, order_id):
    if len(delivery_btns) == 0:
        message = await bot.send_message(chat_id=chat_id, text="Order has been closed")
        botMessage.add_order_related_message(message.message_id, order_id)
    else:
        message = await bot.send_message(chat_id=chat_id, text=obj, reply_markup=build_first_kb(delivery_btns, order_id))
        botMessage.add_order_related_message(message.message_id, order_id)


