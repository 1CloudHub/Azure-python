from creds import credentials
from getInstanceData import get_subID_resourceID_list
from azure.mgmt.monitor import MonitorManagementClient
import datetime


metrics = ['Percentage CPU', 'Network In Total', 'Network Out Total']


def get_final_list():
    """
    This function retrieves the aggregated metric values for every resourceID and appends it to a list.
    :return: list of dictionaries
    """

    final_list = []
    startTime = datetime.datetime.now() - datetime.timedelta(hours=24)
    endTime = datetime.datetime.now()

    subID_resourceID_list = get_subID_resourceID_list()

    for subID_resourceID in subID_resourceID_list:
        monitor_client = MonitorManagementClient(credentials=credentials,
                                                 subscription_id=subID_resourceID['subscriptionID'])
        for metric in metrics:
            metrics_data = monitor_client.metrics.list(
                subID_resourceID['resourceID'],
                timespan="{}/{}".format(startTime, endTime),
                interval='PT1H',
                metricnames=metric,
                aggregation='Minimum, Maximum, Average'
            )

            for iter2 in metrics_data.value:
                for ts in iter2.timeseries:
                    for data in ts.data:
                        time_stamp = str('{}'.format(data.time_stamp))
                        final_list.append({'subscription': subID_resourceID['subscriptionID'],
                                           'resource': subID_resourceID['resourceID'],
                                           'metricType': metric,
                                           'timestamp': time_stamp,
                                           'unit': iter2.unit.name,
                                           'minimum': data.minimum,
                                           'maximum': data.maximum,
                                           'average': data.average})

    return final_list
