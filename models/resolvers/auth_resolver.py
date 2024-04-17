from gql.transport.websockets import WebsocketsTransport

from models.resolvers.orders_resolver import listen_for_orders

client = None



async def initializeGraphql(user_token, chatId):
    if user_token:
        transport = WebsocketsTransport(
            # url='wss://api.iceberg-crm.kz/graphql',
            url='ws://localhost/graphql',
            init_payload={
                'Authorization': user_token
            },
            keep_alive_timeout=600,
            ping_interval=60,
            pong_timeout=10,

        )

        if not transport:
            return
        await listen_for_orders(transport, chatId)
    else:
        print("User token is empty. Cannot initialize GraphqlClient.")







# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMjhlYTE1YzAtYzllZi00Y2JiLWE5OGEtMTZjYTIyZmY5MzViIiwicHJlZml4IjoidGVzdCIsImlkIjoxLCJpYXQiOjE3MTI1NjIzMjZ9.sxHdOVAZwHrxVsYw34JR4NG0JzaKuyvUoOaqbIT5yLo
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGRjNzJiZTktYmQ5OS00NzUxLTgxODAtOGZmM2YxYWJlYTJkIiwicHJlZml4IjoidGVzdCIsImlkIjozLCJpYXQiOjE3MTAxNTU3OTN9.kzdbjajZqpjnB2SmIN-5shxWcyLrdnWm8KjE6g0XV9I
