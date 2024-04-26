from gql import Client, gql
from models.queries.queries import subQuery
from shared.bot_funcs import callBot, delete_msgs, construct_msg


async def listen_for_orders(transport, chat_id, bot_msg_class):
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        subscription = gql(
            subQuery
        )
        async for result in session.subscribe(subscription):
            delivery_id = result['displayOrderToBot']['order']['delivery']['delivery']['id']
            prev_pickup = result['displayOrderToBot']['order']['previousPickup']
            if bot_msg_class is not None:
                user_me_id = bot_msg_class.user_me['id']
                if user_me_id == delivery_id:
                    order_info = result['displayOrderToBot']['order']
                    order_id = order_info['id']
                    text_msg = await construct_msg(result)
                    found_item = bot_msg_class.getObjMessageById(order_id)
                    if found_item is None:
                        bot_msg_class.addObjMessage(result['displayOrderToBot']['order'])
                    found_btns = bot_msg_class.get_delivery_btns(order_id)
                    implement_btn = result['displayOrderToBot']['deliveryBtns']
                    if found_btns is None:
                        bot_msg_class.add_delivery_btns(implement_btn, order_id)
                    else:
                        set_of_sets = {frozenset(d.items()) for d in found_btns}
                        set_of_dict = {frozenset(v.items()) for v in implement_btn}
                        if set_of_dict != set_of_sets:
                            bot_msg_class.add_delivery_btns(implement_btn, order_id)
                    if found_item is None or found_btns is not None:
                        await callBot(text_msg, chat_id, bot_msg_class.deliveryBtns[order_id], order_id)
                else:
                    order_msgs = bot_msg_class.order_related_messages.get(order_id)
                    await delete_msgs(order_msgs, chat_id)
                    bot_msg_class.delete_msg_from_dict(order_id)


