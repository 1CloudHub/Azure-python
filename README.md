#### Retrieving System metrics from Azure using Monitoring API

The below content will guide you through the various processes that need to be performed to retreive system metrics about a Virtual Machine running in Azure cloud.

This blog will be useful for developers who are facing the below pain points.

- Metrics can be obtained for only one VM at a time at the console level and the task gets tedious when there are large number of Virtual machines.

- The obtained data needs to be customized as per the requirements, but such customizations cannot be performed at console level.

- There is no monitoring tool to rely on, for the custom report generation.


**Table of Contents**
 * [Pre-requisites](#pre-requisites)
      - [Python -v 3.7](#python -v 3.7)
	  - [Pip -v 19.0](#pip -v 19.0)
	  - [Azure package for python -v 4.0](#azure-package-python -v 4.0)
	  
 * [Authentication](#authentication)
 	
 	- [Authenticate the API call](#authenticate-the-api-call)
	
 * [Context Setting](#context-setting)
  	- [List the virtual machines](#list-the-virtual-machines)
	
 * [Metrics Retrieval](#metrics-retrieval)
  	- [Fetch system metrics](#fetch-sysytem-metrics)
	
 * [Output handling](#output-handling)
  	- [Writing the output to a file](#writing-the-output-to-a-file)
	
 * [Reference Links](#reference-links)

## Pre-requisites
- #### Python -v 3.7

 Check if python is already installed.
 	
 `$ python3 --version `
 	
 If not installed, download and setup python from the below official website.
   https://www.python.org/downloads/
	
- #### Pip -v 19.0
Check if pip is already installed.
	
 `$pip3 --version `
 	
	If not installed, execute the below command.
	
	 `$ sudo apt install python3-pip`
	 
- #### Azure package for python -v 4.0
	Install Azure package for python using the below command.
	
	`$ sudo pip install azure`
	
## Authentication
- ##### Authenticate the API call - creds.py
	 Firstly, kindly clone/download the scripts and fill in the data for the below variables with the data specific to your requirement in the creds.py script. 
	 - CLIENT = An Application ID, sometimes referred to as a Client ID. This is a GUID that uniquely identifies the app's registration in your Active Directory tenant.
	 
	 - KEY = A secret associated with the application ID (like a password)
	 
	 - TENANT_ID = A Tenant is representative of an organization within Azure Active Directory. The GUID representing that is a tenant ID.
	 
	The credential object obtained can be passed as arguments for the APIs that we are going to use in the program.
	
## Context Setting
- ##### List the virtual machines  - getInstanceData.py
	For this step, we will first obtain the list of subscriptions available under the given Tenant ID as it is required to fetch the list of resource groups and the corresponding virtual machines. 
	
	From that, we will be able to pull out the resource ID (a combination of subscription ID, resource group name and the virtual machine name) for each VM which would be required by the monitoring API to retrieve system metrics.
	
```javascript
        for rg in resource_client.resource_groups.list():
            for vm in compute_client.virtual_machines.list(resource_group_name=rg.name):
                subID_resourceID_list .append({'subscriptionID': sub, 'resourceID': vm.id})

```
The ‘vm’ object does contain attributes other than ‘id’ such as ‘name’ which gives the name of the virtual machine and ‘location’ which gives the location of the virtual machine. 
	
These can be used to customize the report further.
	
## Metrics Retrieval
- ##### Fetch system metrics  - getMetricsData.py
	We will use the Azure monitoring API to fetch the given system metrics over a specific time frame with a predefined granularity. 
	
	For this case, we will try to fetch just the CPU utilization, Network in and Network out. Data for other metrics can also be retrieved using this method provided the name of the metric is already known.
	
```javascript
            metrics_data = monitor_client.metrics.list(
                subID_resourceID['resourceID'],
                timespan="{}/{}".format(startTime, endTime),
                interval='PT1H',
                metricnames=metric,
                aggregation='Minimum, Maximum, Average'
            )
```
	
## Output handling
- ##### Writing the output to a file  - main.py
	The data obtained from the Azure monitoring API will be written onto a CSV file but can be customized as per the requirement. 
	
## Reference Links
The Azure API documentation referenced below has all the necessary details to fetch various system metrics and can also be used to work on other Azure services.

https://docs.microsoft.com/en-us/azure/python/python-sdk-azure-overview?view=azure-python
