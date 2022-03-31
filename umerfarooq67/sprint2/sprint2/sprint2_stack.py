import os
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    RemovalPolicy,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_iam as iam,
    aws_cloudwatch as cw,
    aws_cloudwatch_actions as cw_actions,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_s3 as s3_,
    aws_s3_deployment as s3_deployment
    )
    
from constructs import Construct


class Sprint2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        
        self.CONSTS = {    
            "WEB_URLS" : [
                "www.skipq.org", 
                "www.google.com", 
                "www.namal.edu.pk"
            ],
            "URL_NAMESPACE" : "UF67NameSPACE",
            "URL_METRIC_AVAILABILITY" : "availability",
            "URL_METRIC_LATENCY" : "latency",
            "THRESHOLD_AVAILABILITY" : 1,
            "THRESHOLD_LATENCY" : 0.02
            
        }
    
    
    
        
        # Creating Lambda Role
        ROLE = self.createRole()
        
        # Creating Lambda in Stack
        WH_Lambda_Hanlder = self.createLambda("UF_WH_Lambda_Function",'./libs','WHLambda.lambdaHandlerWebHealth',ROLE)
        WH_Lambda_Hanlder.apply_removal_policy(RemovalPolicy.DESTROY)
        
        # Creating S3 bucketk.
        bucket = self.createS3Bucket("constants_file_bucket","DeployConstantsFile")
        bucket.grant_read_write(WH_Lambda_Hanlder)
        
        '''
            1. Creating Rule for our event.
            2. Event will trigger the target every 1 mins.
            3. Target is defined as our Web Health Lambda Function.
        '''
        lambda_schedule = events_.Schedule.rate(Duration.minutes(1))
        lambda_targets = targets_.LambdaFunction(handler = WH_Lambda_Hanlder)
        eventRule = events_.Rule(
            self, 
            'UF_WH_RULE',
            enabled = True,
            description = "This is event rule to trigger lambda function every 1 min.",
            schedule = lambda_schedule,
            targets = [lambda_targets]
        )
        
        topic_availability = sns.Topic(self, "Topic Availability")
        topic_latency = sns.Topic(self, "Topic Latency")
        for url in  self.CONSTS["WEB_URLS"]:
            
            web_name = url.split('.')[1]
            _dimensions = {'url' : url}
            topic_availability = sns.Topic(self, "{} Topic Availability".format(web_name))
            topic_latency = sns.Topic(self, "{} Topic Latency".format(web_name))
            
            '''
                1. Defining our metric for availability.
                2 Defining alarm for availability.
            '''
            availability_metric = cw.Metric(
                metric_name = self.CONSTS["URL_METRIC_AVAILABILITY"],
                namespace = self.CONSTS["URL_NAMESPACE"],
                dimensions_map = _dimensions,
                label = 'Availability Metric',
                period = Duration.minutes(1)
            )
                
                
            availability_alarm = cw.Alarm(
                self,
                id = "{}_alarm_availability".format(web_name),
                metric = availability_metric,
                evaluation_periods = 1,
                threshold = self.CONSTS["THRESHOLD_AVAILABILITY"],
                comparison_operator = cw.ComparisonOperator.LESS_THAN_THRESHOLD,
                datapoints_to_alarm = 1
            )
            
            topic_availability.add_subscription(subscriptions.EmailSubscription('umer.farooq67.skipq@gmail.com'))
            availability_alarm.add_alarm_action(cw_actions.SnsAction(topic_availability))
            
            '''
                1. Defining our metric for latency.
                2 Defining alarm for latency.
            '''
            latency_metric = cw.Metric(
                metric_name = self.CONSTS["URL_METRIC_LATENCY"],
                namespace = self.CONSTS["URL_NAMESPACE"],
                dimensions_map = _dimensions,
                label = 'Latency Metric',
                period = Duration.minutes(1)
            )
                
                
            latency_alarm = cw.Alarm(
                self,
                id = "{}_alarm_latency".format(web_name),
                metric = latency_metric,
                evaluation_periods = 1,
                threshold = self.CONSTS["THRESHOLD_LATENCY"],
                comparison_operator = cw.ComparisonOperator.GREATER_THAN_THRESHOLD,
                datapoints_to_alarm = 1
            )
            
            topic_latency.add_subscription(subscriptions.EmailSubscription('umer.farooq67.skipq@gmail.com'))
            latency_alarm.add_alarm_action(cw_actions.SnsAction(topic_latency))
             
       
       
    def createS3Bucket(self,_id : str, name : str):
        bucket = s3_.Bucket(
            self, 
            _id,
            versioned = True,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects = True,
            public_read_access = True
        )
     
        s3_deployment.BucketDeployment(
            self, 
            name,
            sources=[s3_deployment.Source.asset('./s3_uploads')],
            destination_bucket=bucket,
            retain_on_delete = False
        )
        
        return bucket
        
       
    def createRole(self):
        new_role = iam.Role(
            self, 'UF67_CW_ROLE',
            role_name = 'CLOUD_WATCH_FULL_ACCESS',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess')]
        )
        
        return new_role

       
    def createLambda(self, _id: str, directory: str, handler_name: str, role_):
        
        lambda_function = lambda_.Function(
            self,
            id = _id,
            handler = handler_name,
            code = lambda_.Code.from_asset(directory),
            runtime = lambda_.Runtime.PYTHON_3_7,
            role = role_)
            
            
        return lambda_function
        
        
        
