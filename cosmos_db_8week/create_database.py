from azure.cosmos import CosmosClient, exceptions
from decouple import config

url = config('ACCOUNT_URI')
key = config('ACCOUNT_KEY')
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'
try:
    database = client.create_database(database_name)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)
