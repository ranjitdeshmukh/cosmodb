import json
from azure.cosmos import CosmosClient
from decouple import config

url = config('ACCOUNT_URI')
key = config('ACCOUNT_KEY')
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'
database = client.get_database_client(database_name)
container_name = 'products'
container = database.get_container_client(container_name)



discontinued_items = container.query_items(
    query='SELECT * FROM products p WHERE p.productModel = @model',
    parameters=[
        dict(name='@model', value='Model 7')
    ],
    enable_cross_partition_query=True
)
for item in discontinued_items:
    print(json.dumps(item, indent=True))