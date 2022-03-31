import boto3

class CloudWatchPutMetric:
    
    def __init__(self):
        self.client = boto3.client('cloudwatch')
        
        
        
    def putMetricData(self,name_space, metric_name, dim, value):
        response = self.client.put_metric_data(
            Namespace=name_space,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': dim,
                    'Value': value,
                },
            ]
        )