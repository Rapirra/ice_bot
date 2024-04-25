from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError
from gql.transport.websockets import WebsocketsTransport

from models.queries.queries import meQuery
from models.resolvers.orders_resolver import listen_for_orders

client = None


async def establish_http_connection(user_token, bot_msg_class):
    try:
        transport = AIOHTTPTransport(
            url='ws://localhost/graphql',
            # url='wss://api.iceberg-crm.kz/graphql',
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
            print(bot_msg_class.user_me, "user_mer")
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
            url='ws://localhost/graphql',
            # url='wss://api.iceberg-crm.kz/graphql',
            init_payload={
                'Authorization': user_token
            },
            keep_alive_timeout=600,
            ping_interval=60,
            pong_timeout=10,
        )
        if not transport:
            return None
        print(transport, 'transport')
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

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMjhlYTE1YzAtYzllZi00Y2JiLWE5OGEtMTZjYTIyZmY5MzViIiwicHJlZml4IjoidGVzdCIsImlkIjoxLCJpYXQiOjE3MTI1NjIzMjZ9.sxHdOVAZwHrxVsYw34JR4NG0JzaKuyvUoOaqbIT5yLo
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGRjNzJiZTktYmQ5OS00NzUxLTgxODAtOGZmM2YxYWJlYTJkIiwicHJlZml4IjoidGVzdCIsImlkIjozLCJpYXQiOjE3MTAxNTU3OTN9.kzdbjajZqpjnB2SmIN-5shxWcyLrdnWm8KjE6g0XV9I
