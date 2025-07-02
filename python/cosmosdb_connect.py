import os
from azure.cosmos import CosmosClient, PartitionKey

COSMOS_URI = "<YOUR_COSMOS_DB_URI>"
COSMOS_KEY = "<YOUR_COSMOS_DB_KEY>"
DATABASE_NAME = "MyDatabase"
CONTAINER_NAME = "MyContainer"

# Initialize Cosmos DB Client
client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)

# Connect to the database and container
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

# Query: Fetch all documents
query = "SELECT * FROM c"

# Execute Query
print("Fetching data from Cosmos DB...")
for item in container.query_items(query, enable_cross_partition_query=True):
    print(f"ID: {item['id']}, Name: {item['name']}, Category: {item['category']}, Quantity: {item['quantity']}")
