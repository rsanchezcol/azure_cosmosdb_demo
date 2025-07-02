const { CosmosClient } = require("@azure/cosmos");

// Cosmos DB Configuration
const COSMOS_URI = "<YOUR_COSMOS_DB_URI>";
const COSMOS_KEY = "<YOUR_COSMOS_DB_KEY>";
const DATABASE_NAME = "MyDatabase";
const CONTAINER_NAME = "MyContainer";

// Initialize Cosmos Client
const client = new CosmosClient({ endpoint: COSMOS_URI, key: COSMOS_KEY });

// Function to Fetch Data from Cosmos DB
async function fetchData() {
  try {
    const database = client.database(DATABASE_NAME);
    const container = database.container(CONTAINER_NAME);

    console.log(`Fetching data from container: ${CONTAINER_NAME}...`);

    // Query Data
    const query = "SELECT * FROM c WHERE c.id = '1'"; // Change query as needed
    const { resources: items } = await container.items.query(query).fetchAll();

    // Display Results
    if (items.length === 0) {
      console.log("No documents found.");
    } else {
      items.forEach(item => {
        console.log(`ID: ${item.id}, Name: ${item.name}, Category: ${item.category}, Quantity: ${item.quantity}`);
      });
    }
  } catch (error) {
    console.error("Failed to fetch data:", error.message);
  }
}

// Execute Data Fetch
fetchData();
