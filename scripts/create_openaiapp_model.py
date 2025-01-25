import subprocess

# Author: Copilot
# Created on: January 25, 2025

# Summary
# This Python script uses the subprocess module to run an Azure CLI command that creates a deployment for a Cognitive Services account.
# The command specifies the resource group, account name, deployment name, model name, model version, model format, SKU name, and SKU capacity.
# The script captures the output and error messages from the command and prints them to the console.

# Define variables
resource_group = 'OAIResourceGroup'
account_name = 'MyOpenAIResource'
deployment_name = 'MyModel'
model_name = 'gpt-35-turbo'
model_version = '0125'
model_format = 'OpenAI'
sku_name = 'Standard'
sku_capacity = 1

# Define the Azure CLI command
command = [
    'az', 'cognitiveservices', 'account', 'deployment', 'create',
    '-g', resource_group,
    '-n', account_name,
    '--deployment-name', deployment_name,
    '--model-name', model_name,
    '--model-version', model_version,
    '--model-format', model_format,
    '--sku-name', sku_name,
    '--sku-capacity', str(sku_capacity)
]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print(result.stdout)
print(result.stderr)
