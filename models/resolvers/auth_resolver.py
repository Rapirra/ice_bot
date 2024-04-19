from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError
from gql.transport.websockets import WebsocketsTransport

from bot import bot
from classesStructure.classStructures import botMessage
from models.queries.queries import meQuery
from models.resolvers.orders_resolver import listen_for_orders

client = None


async def establish_http_connection(user_token):
    try:
        transport = AIOHTTPTransport(
            url='ws://localhost/graphql',
            headers={'Authorization': user_token}
        )
        return await initialize_auth(transport)
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


async def initialize_auth(transport):
    try:
        async with Client(
                transport=transport,
                fetch_schema_from_transport=True,
        ) as session:
            query = gql(meQuery)
            result = await session.execute(query)
            response = result['me']
            botMessage.add_user_me({})
            botMessage.add_user_me(response)
        return "Initialization successful, Hello " + botMessage.user_me['name']
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


async def initialize_graphql(user_token, chat_id):
    try:
        transport = WebsocketsTransport(
            url='ws://localhost/graphql',
            init_payload={
                'Authorization': user_token
            },
            keep_alive_timeout=600,
            ping_interval=60,
            pong_timeout=10,
        )
        if not transport:
            return None
        await listen_for_orders(transport, chat_id)
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
