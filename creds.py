from azure.common.credentials import ServicePrincipalCredentials

# Tenant ID for your Azure Subscription
TENANT_ID = 'Your tenant ID goes here'

# Your Service Principal App ID
CLIENT = 'Your App ID goes here'

# Your Service Principal Password
KEY = 'Your password goes here'


credentials = ServicePrincipalCredentials(
    client_id=CLIENT,
    secret=KEY,
    tenant=TENANT_ID
)
