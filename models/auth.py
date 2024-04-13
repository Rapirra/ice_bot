from python_graphql_client import GraphqlClient
from classesStructure.classStructures import RegisterMessages

client = GraphqlClient(
    endpoint='http://localhost/graphql',
    headers={
        'Authorization': RegisterMessages.userToken}
)

# 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMjhlYTE1YzAtYzllZi00Y2JiLWE5OGEtMTZjYTIyZmY5MzViIiwicHJlZml4IjoidGVzdCIsImlkIjoxLCJpYXQiOjE3MTI1NjIzMjZ9.sxHdOVAZwHrxVsYw34JR4NG0JzaKuyvUoOaqbIT5yLo'


