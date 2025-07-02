# Azure Cosmos DB Demo

This repository contains example scripts and step-by-step guides for working with Azure Cosmos DB using **Python** and **Node.js**. It demonstrates how to:

1. Create an Azure Cosmos DB instance.
2. Upload and query data using Python.
3. Upload and query data using Node.js.
4. Test scripts locally using Visual Studio Code.

---

## **Table of Contents**
- [Prerequisites](#prerequisites)
- [Create Azure Cosmos DB Instance](#create-azure-cosmos-db-instance)
- [Python Script to Fetch Cosmos DB Data](#python-script-to-fetch-cosmos-db-data)
- [Python Script to Upload Cosmos DB Data](#python-script-to-upload-cosmos-db-data)
- [Node.js Script to Query Cosmos DB Data](#nodejs-script-to-query-cosmos-db-data)
- [Run and Test Scripts in Visual Studio Code](#run-and-test-scripts-in-visual-studio-code)
- [Contributing](#contributing)
- [License](#license)

---

## **Prerequisites**

Before using the repository, ensure you have the following tools installed:

### **Tools Required**
1. **Azure CLI**:
   - Install the Azure CLI from [Azure CLI Installation Guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
   - Login into Azure using:
     ```bash
     az login
     ```

2. **Node.js**:
   - Install Node.js from [Node.js Official Website](https://nodejs.org/).
   - Verify installation:
     ```bash
     node -v
     npm -v
     ```

3. **Python**:
   - Install Python from [Python Official Website](https://www.python.org/).
   - Install required Python libraries:
     ```bash
     pip install azure-cosmos
     ```

4. **Visual Studio Code**:
   - Install Visual Studio Code from [Visual Studio Code Website](https://code.visualstudio.com/).

---

## **Create Azure Cosmos DB Instance**

Follow these steps to create and configure an Azure Cosmos DB instance:

### **Step 1: Create Cosmos DB Account**
Use Azure CLI commands to create a Cosmos DB account:

```bash
# Variables
RESOURCE_GROUP="myResourceGroup"
COSMOS_ACCOUNT="myCosmosDBAccount"
LOCATION="eastus"
DATABASE_NAME="MyDatabase"
CONTAINER_NAME="MyContainer"
PARTITION_KEY_PATH="/category"

# Create Resource Group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create Azure Cosmos DB Account (SQL API)
az cosmosdb create \
  --name $COSMOS_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --kind GlobalDocumentDB \
  --default-consistency-level Eventual \
  --locations regionName=$LOCATION isZoneRedundant=False

# Create Database
az cosmosdb sql database create \
  --account-name $COSMOS_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --name $DATABASE_NAME

# Create Container with Partition Key
az cosmosdb sql container create \
  --account-name $COSMOS_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --database-name $DATABASE_NAME \
  --name $CONTAINER_NAME \
  --partition-key-path $PARTITION_KEY_PATH
