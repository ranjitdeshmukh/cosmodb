from azure.cosmos import CosmosClient, PartitionKey, exceptions
from decouple import config

# API_USERNAME = config('USER')
# API_KEY = config('KEY')
url = config('ACCOUNT_URI')
key = config('ACCOUNT_KEY')
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'
database = client.get_database_client(database_name)
container_name = 'products'

try:
    container = database.create_container(
        id=container_name, partition_key=PartitionKey(path="/productName"))
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(container_name)
except exceptions.CosmosHttpResponseError:
    raise
