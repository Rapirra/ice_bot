# import asyncio
# import logging
#
# from gql import Client, gql
# from gql.transport.websockets import WebsocketsTransport
#
# logging.basicConfig(level=logging.INFO)
#
#
# async def main():
#     transport = WebsocketsTransport(
#         url='wss://api.iceberg-crm.kz/graphql',
#         init_payload={
#             'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGRjNzJiZTktYmQ5OS00NzUxLTgxODAtOGZmM2YxYWJlYTJkIiwicHJlZml4IjoidGVzdCIsImlkIjozLCJpYXQiOjE3MTAxNTU3OTN9.kzdbjajZqpjnB2SmIN-5shxWcyLrdnWm8KjE6g0XV9I'},
#         keep_alive_timeout=60,
#         ping_interval=60,
#         pong_timeout=10,
#
#     )
#     async with Client(
#             transport=transport,
#             fetch_schema_from_transport=True,
#     ) as session:
#         subscription = gql(
#             """
#            subscription  {
#   displayOrderToBot {
#     id
#     name
#     date
#     parent
#     price
#     costPrice
#     paid
#   }
# }
#         """
#         )
#         async for result in session.subscribe(subscription):
#             print(result)
#
#
# asyncio.run(main())
