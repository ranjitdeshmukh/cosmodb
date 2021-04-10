from azure.cosmos import CosmosClient
from decouple import config

url = config('ACCOUNT_URI')
key = config('ACCOUNT_KEY')
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'
database = client.get_database_client(database_name)
container_name = 'products'
container = database.get_container_client(container_name)

for i in range(1, 10):
    container.upsert_item({
        'id': 'item{0}'.format(i),
        'productName': 'Widget',
        'productModel': 'Model {0}'.format(i)
    }
    )
