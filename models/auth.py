import json

from gql import Client, gql
from gql.transport.websockets import WebsocketsTransport

from bot import bot
from classesStructure.classStructures import botMessage

client = None


async def initializeGraphql(userToken, chatId):
    if userToken:
        transport = WebsocketsTransport(
            # url='wss://api.iceberg-crm.kz/graphql',
            url='ws://localhost/graphql',
            init_payload={
                'Authorization': userToken
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


async def listen_for_orders(transport, chatId):
    async with Client(
            transport=transport,
            fetch_schema_from_transport=True,
    ) as session:
        subscription = gql(
            """
           subscription Subscription {
  displayOrderToBot {
    id
    name
    date
    client {
      id
      name
    }
    status {
      id
      name
    }
  }
}
        """
        )
        async for result in session.subscribe(subscription):
            await bot.send_message(chat_id='1092777329', text='hi banshee')
            text_msg = json.dumps(result['displayOrderToBot'])
            if botMessage is not None:
                setattr(botMessage, 'objectMessage', text_msg)
                await callBot(text_msg, chatId)


async def callBot(obj, chatId):
    await bot.send_message(chat_id=chatId, text=obj)

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMjhlYTE1YzAtYzllZi00Y2JiLWE5OGEtMTZjYTIyZmY5MzViIiwicHJlZml4IjoidGVzdCIsImlkIjoxLCJpYXQiOjE3MTI1NjIzMjZ9.sxHdOVAZwHrxVsYw34JR4NG0JzaKuyvUoOaqbIT5yLo
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGRjNzJiZTktYmQ5OS00NzUxLTgxODAtOGZmM2YxYWJlYTJkIiwicHJlZml4IjoidGVzdCIsImlkIjozLCJpYXQiOjE3MTAxNTU3OTN9.kzdbjajZqpjnB2SmIN-5shxWcyLrdnWm8KjE6g0XV9I
