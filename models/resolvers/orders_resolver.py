from gql import Client, gql

from bot import bot
from classesStructure.classStructures import botMessage
from models.queries.queries import subQuery
from shared.bot_funcs import callBot


async def listen_for_orders(transport, chatId):
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        subscription = gql(
            subQuery
        )
        print()
        async for result in session.subscribe(subscription):
            await bot.send_message(chat_id='1092777329', text='hi banshee')

            order_info = result['displayOrderToBot']['order']
            order_id = order_info['id']
            order_name = order_info['name']
            client_name = order_info['client']['name']
            client_phone = order_info['client']['numbers'][0]['phone'] if order_info['client']['numbers'] else 'N/A'
            client_address = order_info['client']['addresses'][0]['address'] if order_info['client']['addresses'] else 'N/A'
            status_name = order_info['status']['more']['delivery'] if order_info['status']['more'] else 'N/A'

            text_msg = f"Order ID: {order_id}\nOrder Name: {order_name}\nClient: {client_name}{client_phone}\nClient Address:{client_address}\nStatus: {status_name}"
            print('result', result['displayOrderToBot']['deliveryBtns'])
            if botMessage is not None:
                setattr(botMessage, 'objectMessage', result['displayOrderToBot']['order'])
                setattr(botMessage, 'deliveryBtns', result['displayOrderToBot']['deliveryBtns'])

                await callBot(text_msg, chatId, botMessage.deliveryBtns)