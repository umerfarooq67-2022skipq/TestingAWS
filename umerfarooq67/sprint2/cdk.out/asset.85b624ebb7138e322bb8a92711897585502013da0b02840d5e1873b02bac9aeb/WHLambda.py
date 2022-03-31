import urllib3
from datetime import datetime

from aws_cdk import(
  aws_cloudwatch as cw,
  core
)

import boto3


WEB_URLS = ['www.skipq.org']#, 'www.google.com','www.facebook.com']
def lambdaHandlerWebHealth(event, context):
    '''
    Input: 
        Event and Context
    Steps:
        1. Check Availibility of the web server.
        2. Check the response time of the web server
        3. Doing above process for multiple urls.
    Output:
        Map of JSON Object with Availibility Status and Response Time.
    '''
    http = urllib3.PoolManager(num_pools=10)
    
    
    metric_data = []
    for url in WEB_URLS:
        
        url_result = {}    
        
        # Storing availibility status
        url_result["Name"] = 'Availibility'
        url_result['Value'] = checkAvailibility(url, http)
        
        # Storing latency in seconds.
        url_result["Name"] = "Latency"
        url_result['Value'] = checkResponseTime(url, http)
        
        metric_data.append(url_result)
    
    
    metric = {
        'MetricName': 'UF_WEB_STATS',
        'Dimensions': [
            {
                'Name': 'Web Url',
                'Value': 'Custom_URL',
            },
            
            {
                'Name': 'Metric',
                'Value': 'Custom_Value',
            },
        ],
        'Unit': 'None',
        'Value': metric_data
    }
    
    cloudwatch = boto3.client('cloudwatch','us-east-1')
    cloudwatch.put_metric_data(
        Namespace='uf_url',
        MetricData=metric
        )
    
    return cloudwatch
    
    
    



def checkAvailibility(url, http):
    '''
        Method: 
            Check the availibility of the web server.
        Ouptut:
            Return a response based on status of web server. 1 for live and 0 for unreachable.
    '''
    response = http.request("GET",url)
    if response.status == 200:
        return 200
    
    return 101


def checkResponseTime(url, http):
    '''
        Method: Compute the latency of the web server.
        Latency = Response Time (End) - Request Time (Start). Note. Convert it to seconds.
        Output:
            Return latency in seconds.
    '''
    startTime = datetime.now()
    response = http.request("GET",url)
    endTime = datetime.now()
    delta = endTime - startTime
    latency_in_sec = round(delta.microseconds * 0.000001,6)
    return latency_in_sec
    
