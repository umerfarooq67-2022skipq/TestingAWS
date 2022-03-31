import boto3

class CloudWatchPutMetric:
    
    def __init__(self):
        self.client = boto3.client('cloudwatch','us-east-1')
        
        
        
    def putMetricData(self,namespace, metric, dim, value):
        response = self.client.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metric,
                    'Dimensions': dim,
                    'Value': value,
                },
            ]
        )