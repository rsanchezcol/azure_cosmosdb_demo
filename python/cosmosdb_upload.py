import os
from azure.cosmos import CosmosClient, PartitionKey

# Cosmos DB Configuration - Update these values
COSMOS_URI = "<YOUR_COSMOS_DB_URI>"
COSMOS_KEY = "<YOUR_COSMOS_DB_KEY>"
DATABASE_NAME = "MyDatabase"
CONTAINER_NAME = "MyContainer"

# Sample Data to Upload - Replace with Your Data
data_to_upload = [
    {
        "id": "4",
        "category": "drinks",
        "name": "Water",
        "quantity": 100
    },
    {
        "id": "5",
        "category": "fruits",
        "name": "Orange",
        "quantity": 40
    },
    {
        "id": "6",
        "category": "vegetables",
        "name": "Potato",
        "quantity": 200
    }
]

# Initialize Cosmos DB Client
def cosmosdb_client(uri, key):
    return CosmosClient(uri, credential=key)

# Upload Data to Cosmos DB
def upload_data_to_cosmosdb(client, database_name, container_name, data):
    try:
        # Connect to Database and Container
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        for item in data:
            try:
                # Insert one item at a time
                container.upsert_item(item)
                print(f"Successfully uploaded item with id: {item['id']}")
            except Exception as e:
                print(f"Error uploading item {item['id']}: {e}")

    except Exception as e:
        print(f"Failed to upload data to Cosmos DB: {e}")

# Main Function
if __name__ == "__main__":
    # Create Client
    client = cosmosdb_client(COSMOS_URI, COSMOS_KEY)

    # Upload Data
    upload_data_to_cosmosdb(client, DATABASE_NAME, CONTAINER_NAME, data_to_upload)
