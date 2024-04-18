from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from classesStructure.classStructures import botMessage
from models.queries.queries import btnMutation, commentMutation


async def save_btn_action(user_token, btn_event):
    print('user_token', user_token)
    transport = AIOHTTPTransport(
        url='ws://localhost/graphql',
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
        botMessage.add_delivery_btns(btns)
        # setattr(botMessage, 'deliveryBtns', result['deliveryButton'])


async def save_comment_action(user_token, btn_event):
    print('user_token', user_token)
    transport = AIOHTTPTransport(
        url='ws://localhost/graphql',
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
        botMessage.add_delivery_btns(None)
