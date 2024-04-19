from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport

from classesStructure.classStructures import botMessage
from models.queries.queries import meQuery
from models.resolvers.orders_resolver import listen_for_orders

client = None


async def initialize_auth(user_token):
    if user_token:
        try:
            transport = AIOHTTPTransport(
                url='ws://localhost/graphql',
                headers={'Authorization': user_token}
            )
            async with Client(
                    transport=transport,
                    fetch_schema_from_transport=True,
            ) as session:
                query = gql(meQuery)

                result = await session.execute(query)
                response = result['me']
                botMessage.add_user_me(response)
            if not transport:
                return "Initialization failed"
            return "Initialization successful, Hello " + botMessage.user_me['name']
        except Exception as e:
            return "Initialization failed"
    else:
        return "User token is empty"


async def initialize_graphql(user_token, chat_id):
    if user_token:
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
        except Exception as e:
            return "Initialization failed"
    else:
        return "User token is empty"

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMjhlYTE1YzAtYzllZi00Y2JiLWE5OGEtMTZjYTIyZmY5MzViIiwicHJlZml4IjoidGVzdCIsImlkIjoxLCJpYXQiOjE3MTI1NjIzMjZ9.sxHdOVAZwHrxVsYw34JR4NG0JzaKuyvUoOaqbIT5yLo
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGRjNzJiZTktYmQ5OS00NzUxLTgxODAtOGZmM2YxYWJlYTJkIiwicHJlZml4IjoidGVzdCIsImlkIjozLCJpYXQiOjE3MTAxNTU3OTN9.kzdbjajZqpjnB2SmIN-5shxWcyLrdnWm8KjE6g0XV9I
