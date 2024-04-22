from bot import bot
from keyboards.inline_keyboards.pickup_kb import build_first_kb


async def callBot(obj, chat_id, delivery_btns, order_id):
    print('obj', obj)
    print('delivery_btns', delivery_btns)
    if len(delivery_btns) == 0:
        await bot.send_message(chat_id=chat_id, text="Order has been closed")
    else:
        await bot.send_message(chat_id=chat_id, text=obj, reply_markup=build_first_kb(delivery_btns, order_id))


