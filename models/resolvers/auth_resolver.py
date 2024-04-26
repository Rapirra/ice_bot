from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError
from gql.transport.websockets import WebsocketsTransport

from bot import url_graphql
from models.queries.queries import meQuery
from models.resolvers.orders_resolver import listen_for_orders

client = None


async def establish_http_connection(user_token, bot_msg_class):
    try:
        transport = AIOHTTPTransport(
            url=url_graphql,
            headers={'Authorization': user_token}
        )
        return await initialize_auth(transport, bot_msg_class)
    except TransportQueryError as e:
        if e.errors:
            for error in e.errors:
                if not isinstance(error['message'], str):
                    print("Error message is not a string:", error['message'])
                else:
                    print("GraphQL Error:", error['message'])
        else:
            print("Unknown GraphQL error occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


async def initialize_auth(transport, bot_msg_class):
    try:
        async with Client(
                transport=transport,
                fetch_schema_from_transport=True,
        ) as session:
            query = gql(meQuery)
            result = await session.execute(query)
            response = result['me']
            bot_msg_class.add_user_me(response)
        return "Initialization successful, Hello " + bot_msg_class.user_me['name']
    except TransportQueryError as e:
        if e.errors:
            for error in e.errors:
                if not isinstance(error['message'], str):
                    print("Error message is not a string:", error['message'])
                else:
                    print("GraphQL Error:", error['message'])
        else:
            print("Unknown GraphQL error occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


async def initialize_graphql(user_token, chat_id, bot_msg_class):
    try:
        transport = WebsocketsTransport(
            url=url_graphql,
            init_payload={
                'Authorization': user_token
            },
            keep_alive_timeout=600,
            ping_interval=60,
            pong_timeout=10,
        )
        if not transport:
            return None
        await listen_for_orders(transport, chat_id, bot_msg_class)
    except TransportQueryError as e:
        if e.errors:
            for error in e.errors:
                if not isinstance(error['message'], str):
                    print("Error message is not a string:", error['message'])
                else:
                    print("GraphQL Error:", error['message'])
        else:
            print("Unknown GraphQL error occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
