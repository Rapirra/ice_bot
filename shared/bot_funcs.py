from bot import bot
from keyboards.inline_keyboards.pickup_kb import build_first_kb
from aiogram.exceptions import TelegramBadRequest


async def callBot(obj, chat_id, delivery_btns, order_id, bot_msg_class):
    print(obj, 'obj')
    print('bot_msg_class', bot_msg_class)
    if bot_msg_class is not None:
        if len(delivery_btns) == 0:
            message = await bot.send_message(chat_id=chat_id, text="Order has been closed")
            bot_msg_class.add_order_related_message(message.message_id, order_id)
        else:
            message = await bot.send_message(chat_id=chat_id, text=obj,
                                             reply_markup=build_first_kb(delivery_btns, order_id))
            bot_msg_class.add_order_related_message(message.message_id, order_id)


async def construct_msg(result):
    order_info = result['displayOrderToBot']['order']
    order_id = order_info['id']
    order_name = order_info['name']
    client_name = order_info['client']['name']
    client_phone = order_info['client']['numbers'][0]['phone'] if order_info['client'][
        'numbers'] else 'N/A'
    client_address = order_info['client']['addresses'][0]['address'] if order_info['client'][
        'addresses'] else 'N/A'
    status_name = order_info['status']['more']['delivery'] if order_info['status'][
        'more'] else 'N/A'
    text_msg = f"Order ID: {order_id}\nOrder Name: {order_name}\nClient: {client_name}{client_phone}\nClient Address:{client_address}\nStatus: {status_name}"
    return text_msg


async def delete_msgs(order_msgs, chat_id,  order_id):
    for order_msg_id in order_msgs:
        # print('bot_msg_class', bot_msg_class)
        print('order_msg_id', order_msg_id)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=order_msg_id)
            # await bot_msg_class.delete_msg_from_dict(order_id, order_msg_id)
            # print('bot_msg_class', bot_msg_class.order_related_messages)
        except TelegramBadRequest:
            print(f"Message with ID {order_msg_id} not found. It may have been deleted already or doesn't exist.")

        # if bot_msg_class is not None:
             # else:
        #     print('here delete_msgs')