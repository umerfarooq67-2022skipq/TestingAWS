from aws_cdk import (
    # Duration,
    aws_lambda as lambda_,
    Stack,
    RemovalPolicy
    # aws_sqs as sqs,
)
from constructs import Construct

class Sprint1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        HWLambda_Function = self.create_lambda("Suleman_HW_Lambda",'./resources','HWLambda.lambda_handler')
        HWLambda_Function.apply_removal_policy(RemovalPolicy.DESTROY)
        # The code that defines your stack goes here
        # example resource
        # queue = sqs.Queue(
        #     self, "Sprint1Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
    def create_lambda(self,id,asset,handler):
        return lambda_.Function(
            self,
            id=id,
            code=lambda_.Code.from_asset(asset),
            handler=handler,
            runtime=lambda_.Runtime.PYTHON_3_6)

