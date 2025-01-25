import subprocess

# Author: Copilot
# Created on: January 25, 2025

# Summary
# This Python script uses the subprocess module to run an Azure CLI command that creates a Cognitive Services account.
# The command specifies the account name, resource group, location, kind, SKU, and subscription ID.
# The script captures the output and error messages from the command and prints them to the console.

# Define variables
account_name = 'account_name'
resource_group = 'resource_group_name'
location = 'location'
kind = 'OpenAI'
sku = 's0'
subscription_id = 'subscription_id'

# Define the Azure CLI command to restore the resource
command = [
    'az', 'cognitiveservices', 'account', 'create',
    '-n', account_name,
    '-g', resource_group,
    '-l', location,
    '--kind', kind,
    '--sku', sku,
    '--subscription', subscription_id
]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print(result.stdout)
print(result.stderr)
