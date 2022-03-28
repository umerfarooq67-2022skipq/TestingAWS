import urllib3
from datetime import datetime

WEB_URL = 'www.skipq.org'
def lambdaHandlerWebHealth(event, context):
    '''
    Input: 
        Event and Context
    Steps:
        1. Check Availibility of the web server.
        2. Check the response time of the web server
    Output:
        JSON Object with Availibility Status and Response Time.
    '''
    

    result = {}
    
    # Storing availibility status
    result['availibility'] = checkAvailibility()
    
    # Storing latency in seconds.
    result['latency'] = checkResponseTime()
    
    return result
    
    
    

def sendRequest():
    '''
        Method:
            Sending GET request to a web server.
        Output:
            Returning the status of the web server.
    '''
    http = urllib3.PoolManager()
    response =  http.request("GET",WEB_URL)
    return response
    


def checkAvailibility():
    '''
        Method: 
            Check the availibility of the web server.
        Ouptut:
            Return a response based on status of web server. 1 for live and 0 for unreachable.
    '''
    response = sendRequest()
    if response.status == 200:
        return 2.0
    
    return 1.0


def checkResponseTime():
    '''
        Method: Compute the latency of the web server.
        Latency = Response Time (End) - Request Time (Start). Note. Convert it to seconds.
        Output:
            Return latency in seconds.
    '''
    startTime = datetime.now()
    response = sendRequest()
    endTime = datetime.now()
    delta = endTime - startTime
    latency_in_sec = round(delta.microsecond * 0.000001,6)
    return latency_in_sec
    
