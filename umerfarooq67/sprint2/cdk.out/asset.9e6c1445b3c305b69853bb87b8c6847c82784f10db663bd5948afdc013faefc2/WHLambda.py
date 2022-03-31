import urllib3
from datetime import datetime
import CloudWatchPutMetric


WEB_URLS = ['www.skipq.org']#, 'www.google.com','www.facebook.com']
URL_NAMESPACE = "UF67NAMESPACE"
URL_METRIC_NAME_AVAILABILITY = 'availability'
URL_METRIC_NAME_LATENCY = 'latency'
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
    http = urllib3.PoolManager(num_pools=10)
    
    
    cw = CloudWatchPutMetric()
    
    finalResult = []
    
    for url in WEB_URLS:
        url_result = {}
        
        dimension = {
            'Name' : 'url',
            'Value': url
        }  
        
        # Storing availibility status
        availability = checkAvailibility(url, http)
        url_result['availability'] = availability
        cw.putMetricData(URL_NAMESPACE, URL_METRIC_NAME_AVAILABILITY, dimension, availability)
        
        # Storing latency in seconds.
        latency = checkResponseTime(url, http)
        cw.putMetricData(URL_NAMESPACE, URL_METRIC_NAME_LATENCY, dimension, latency)
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
    
