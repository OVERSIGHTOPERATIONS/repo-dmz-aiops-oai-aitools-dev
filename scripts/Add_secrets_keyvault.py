# Author: Copilot
# Date: 2025-01-28
# Summary: This script adds secrets to the Key Vault.
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# URL of your Azure Key Vault
vault_url = "https://<YourVaultName>.vault.azure.net/"

# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()

# Create a SecretClient to interact with the Key Vault
client = SecretClient(vault_url=vault_url, credential=credential)

# Name and value of the secret for the cognitive service endpoint
secret_name_endpoint = "cog-service-endpoint"
secret_value_endpoint = "<your_endpoint>"

# Set the secret in the Key Vault
client.set_secret(secret_name_endpoint, secret_value_endpoint)

# Name and value of the secret for the cognitive service key
secret_name_key = "cog-service-key"
secret_value_key = "<your_key>"

# Set the secret in the Key Vault
client.set_secret(secret_name_key, secret_value_key)
