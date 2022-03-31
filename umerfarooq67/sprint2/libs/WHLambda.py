import urllib3
import json
from datetime import datetime
from cloudWatch import CloudWatchPutMetric
import boto3


def lambdaHandlerWebHealth(event, context):
    
    '''
        Input: 
            Event and Context
        Steps:
            1. Check Availibility of the web server.
            2. Check the response time of the web server
            3. Doing above process for multiple urls.
        Output:
            Map of JSON Object with availability Status and Response Time.
    '''

    s3 = boto3.client('s3')
    bucket = "ufbucketsprinttwo"
    key_ = 'constants.json'
    s3_response = s3.get_object(Bucket=bucket, Key = key_)
    s3_content = s3_response['Body']
    jsonObject = json.loads(s3_content.read())
    
    WEB_URLS = jsonObject["WEB_URLS"]
    URL_NAMESPACE = jsonObject["URL_NAMESPACE"]
    URL_METRIC_AVAILABILITY = jsonObject["URL_METRIC_AVAILABILITY"]
    URL_METRIC_LATENCY = jsonObject["URL_METRIC_LATENCY"]


        
    
    http = urllib3.PoolManager(num_pools=10)
    
    
    cw = CloudWatchPutMetric()
    
    finalResult = []
    
    for url in WEB_URLS:
        url_result = {}
        
        dimensions = [
            {
                'Name' : 'url',
                'Value': url
            }  
        ]
        
        # Storing availibility status
        availability = checkAvailibility(url, http)
        url_result['availability'] = availability
        cw.putMetricData(URL_NAMESPACE, URL_METRIC_AVAILABILITY, dimensions, availability)
        
        # Storing latency in seconds.
        latency = checkResponseTime(url, http)
        cw.putMetricData(URL_NAMESPACE, URL_METRIC_LATENCY, dimensions, latency)
        url_result['latency'] = latency
        
        
        finalResult.append(url_result)
        
        
    return finalResult
        
        
        

def checkAvailibility(url, http):
    '''
        Method: 
            Check the availibility of the web server.
        Ouptut:
            Return a response based on status of web server. 1 for live and 0 for unreachable.
    '''
    response = http.request("GET",url)
    if response.status == 200:
        return 1.0
    
    return 0.0


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
    

