from azure.cosmos import CosmosClient

# Cosmos DB Configuration (Update these values)
COSMOS_URI = "<YOUR_COSMOS_DB_URI>"
COSMOS_KEY = "<YOUR_COSMOS_DB_KEY>"
DATABASE_NAME = "MyDatabase"
CONTAINER_NAME = "MyContainer"

# Initialize Cosmos DB Client
def initialize_client(uri, key):
    return CosmosClient(uri, credential=key)

# Search Data in Cosmos DB
def search_data_in_cosmosdb(client, database_name, container_name, search_query):
    try:
        # Connect to Database and Container
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        print(f"Searching data in {container_name}...")

        # Execute Query
        results = container.query_items(
            query=search_query,
            enable_cross_partition_query=True  # Enable if container uses partition keys
        )

        # Print Query Results
        for item in results:
            print(f"Found: {item}")
    except Exception as e:
        print(f"Error occurred while searching: {e}")

# Main Function
if __name__ == "__main__":
    # Initialize Connection
    client = initialize_client(COSMOS_URI, COSMOS_KEY)

    # Define Search Query (SQL-style query; replace WHERE clause based on your needs)
    search_query = "SELECT * FROM c WHERE c.quantity > 30"

    # Search Data
    search_data_in_cosmosdb(client, DATABASE_NAME, CONTAINER_NAME, search_query)
