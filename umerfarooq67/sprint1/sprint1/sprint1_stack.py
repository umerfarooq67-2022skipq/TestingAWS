from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_, # aws_lambda package.
    RemovalPolicy # Removal policy to update the lambda in case of changes.
)
from constructs import Construct

class Sprint1Stack(Stack):

    # Constructor
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Calling Lambda Functon with id, directory path and handler name.
        output_hw_lambda = self.createHWLambda("UF_HW_Lambda", "./libs", "HWLambda.handlerHWLambda")
        
        # Applying Removal policy.
        output_hw_lambda.apply_removal_policy(RemovalPolicy.DESTROY)
    
    
    # Lambda Method Config.
    def createHWLambda(self, _id: str, hanlderPath: str, handlerName: str):
        
        '''
        Input: _id, path for lambda function (hellow world), lambda function hanlder nam
        Config: id, handler name, handler path using asset method and runtime
        Output: lambda_method
        '''
        
        lambda_method = lambda_.Function(
            self,
            id = _id,
            handler = handlerName,
            code = lambda_.Code.from_asset(hanlderPath),
            runtime = lambda_.Runtime.PYTHON_3_7
            )
            
        
        return lambda_method

        
        
        