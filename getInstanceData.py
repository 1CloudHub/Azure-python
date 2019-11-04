from creds import credentials

from azure.mgmt.resource import SubscriptionClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient


def get_sub_list():
    """
    This function returns a list of subscriptions available under the tenant ID
    provided in the credentials object.
    :return: list of strings
    """

    subscriptionClient = SubscriptionClient(credentials)

    sub_list = []
    for subscription in subscriptionClient.subscriptions.list():
        sub_list.append(subscription.subscription_id)

    return sub_list


def get_subID_resourceID_list():
    """
    This function retrieves resource groups and the corresponding virtual machines under every subscription
    returned from the 'get_sub_list' function and appends the output as a dictionary to a list.
    :return: list of dictionaries
    """

    sub_list = get_sub_list()
    subID_resourceID_list = []

    for sub in sub_list:
        resource_client = ResourceManagementClient(credentials=credentials, subscription_id=sub)
        compute_client = ComputeManagementClient(credentials=credentials, subscription_id=sub)

        for rg in resource_client.resource_groups.list():
            for vm in compute_client.virtual_machines.list(resource_group_name=rg.name):
                subID_resourceID_list.append({'subscriptionID': sub, 'resourceID': vm.id})

    return subID_resourceID_list
