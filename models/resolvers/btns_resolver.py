from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from models.queries.queries import btnMutation, commentMutation


async def save_btn_action(user_token, btn_event, bot_msg_class):
    transport = AIOHTTPTransport(
        url='ws://localhost/graphql',
        # url='wss://api.iceberg-crm.kz/graphql',
        headers={'Authorization': user_token}
    )
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        mutation = gql(btnMutation)
        params = {
            'order': btn_event['order'],
            'button': int(btn_event['button'])
        }
        result = await session.execute(mutation, variable_values=params)
        btns = result['deliveryButton']
        bot_msg_class.add_delivery_btns(btns, btn_event['order'])


async def save_comment_action(user_token, btn_event):
    transport = AIOHTTPTransport(
        url='ws://localhost/graphql',
        # url='wss://api.iceberg-crm.kz/graphql',
        headers={'Authorization': user_token}
    )
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        mutation = gql(commentMutation)
        params = {
            'object': btn_event['object'],
            'module': "ORDER",
            'comment': btn_event['comment']
        }

        await session.execute(mutation, variable_values=params)
