from python_graphql_client import GraphqlClient
from handlers.pickup_handler import botMessage

client = None


def initializeGraphql(userToken):
    print('userToken', userToken)
    global client
    if userToken:
        client = GraphqlClient(
            endpoint='http://localhost/graphql',
            headers={'Authorization': userToken}
        )
    else:
        print("User token is empty. Cannot initialize GraphqlClient.")

# 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMjhlYTE1YzAtYzllZi00Y2JiLWE5OGEtMTZjYTIyZmY5MzViIiwicHJlZml4IjoidGVzdCIsImlkIjoxLCJpYXQiOjE3MTI1NjIzMjZ9.sxHdOVAZwHrxVsYw34JR4NG0JzaKuyvUoOaqbIT5yLo'
