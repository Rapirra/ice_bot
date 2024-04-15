from gql import Client, gql
from gql.transport.websockets import WebsocketsTransport

from bot import chat_id, bot
from classesStructure.classStructures import botMessage

client = None


async def initializeGraphql(userToken):
    print('userToken', userToken)
    if userToken:
        transport = WebsocketsTransport(
            url='wss://api.iceberg-crm.kz/graphql',
            init_payload={
                'Authorization': userToken},
            keep_alive_timeout=600,
            ping_interval=60,
            pong_timeout=10,

        )

        if not transport:
            return
        await listen_for_orders(transport)
    else:
        print("User token is empty. Cannot initialize GraphqlClient.")


async def listen_for_orders(transport):
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        subscription = gql(
            """
           subscription  {
  displayOrderToBot {
    id
    name
    date
    parent
    price
    costPrice
    paid
  }
}
        """
        )
        async for result in session.subscribe(subscription):
            print(result)
            bot.send_message(chat_id, botMessage.objectMessage)




# 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMjhlYTE1YzAtYzllZi00Y2JiLWE5OGEtMTZjYTIyZmY5MzViIiwicHJlZml4IjoidGVzdCIsImlkIjoxLCJpYXQiOjE3MTI1NjIzMjZ9.sxHdOVAZwHrxVsYw34JR4NG0JzaKuyvUoOaqbIT5yLo'
