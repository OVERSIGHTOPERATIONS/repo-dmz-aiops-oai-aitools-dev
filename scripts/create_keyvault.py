# Author: Copilot
# Date: 2025-01-28
# Summary
# This script creates a new Key Vault in Azure.
# Pre-requisites: Before running this script, ensure that you have the Azure CLI installed on your local machine. 
# Install the python SDK package: pip install azure-keyvault-secrets azure-identity
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient

# Set your variables
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
resource_group_name = "<ResourceGroup>"
vault_name = "<YourVaultName>"
location = "<Location>"

# Authenticate with Azure
credential = DefaultAzureCredential()
kv_client = KeyVaultManagementClient(credential, subscription_id)

# Create the Key Vault
async_key_vault_creation = kv_client.vaults.begin_create_or_update(
    resource_group_name,
    vault_name,
    {
        "location": location,
        "properties": {
            "sku": {"family": "A", "name": "standard"},
            "tenant_id": os.environ["AZURE_TENANT_ID"],
            "access_policies": []
        }
    }
)

key_vault = async_key_vault_creation.result()
print(f"Key Vault {key_vault.name} created successfully.")
