from gql import Client, gql
from classesStructure.classStructures import botMessage
from models.queries.queries import subQuery
from shared.bot_funcs import callBot


async def listen_for_orders(transport, chat_id):
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        subscription = gql(
            subQuery
        )
        async for result in session.subscribe(subscription):
            order_info = result['displayOrderToBot']['order']
            order_id = order_info['id']
            order_name = order_info['name']
            client_name = order_info['client']['name']
            client_phone = order_info['client']['numbers'][0]['phone'] if order_info['client']['numbers'] else 'N/A'
            client_address = order_info['client']['addresses'][0]['address'] if order_info['client'][
                'addresses'] else 'N/A'
            status_name = order_info['status']['more']['delivery'] if order_info['status']['more'] else 'N/A'
            text_msg = f"Order ID: {order_id}\nOrder Name: {order_name}\nClient: {client_name}{client_phone}\nClient Address:{client_address}\nStatus: {status_name}"
            if botMessage is not None:
                found_item = botMessage.getObjMessageById(order_id)
                if found_item is None:
                    botMessage.addObjMessage(result['displayOrderToBot']['order'])
                found_btns = botMessage.get_delivery_btns(order_id)
                implement_btn = result['displayOrderToBot']['deliveryBtns']
                if found_btns is None:
                    botMessage.add_delivery_btns(implement_btn, order_id)
                else:
                    set_of_sets = {frozenset(d.items()) for d in found_btns}
                    set_of_dict = {frozenset(v.items()) for v in implement_btn}
                    if set_of_dict != set_of_sets:
                        botMessage.add_delivery_btns(implement_btn, order_id)
                if found_item is None or found_btns is not None:
                    await callBot(text_msg, chat_id, botMessage.deliveryBtns[order_id], order_id)
