from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
    RemovalPolicy
)
from constructs import Construct

class Sprint2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

       
        WH_Lambda_Hanlder = self.createLambda("UF_WH_Lambda_Function",'./libs','WHLambda.lambdaHandlerWebHealth')
        WH_Lambda_Hanlder.apply_removal_policy(RemovalPolicy.DESTROY)
       
       
    def createLambda(self, _id: str, directory: str, handler_name: str):
        
        lambda_function = lambda_.Function(
            self,
            id = _id,
            handler = handler_name,
            code = lambda_.Code.from_asset(directory),
            runtime = lambda_.Runtime.PYTHON_3_7)
            
            
        return lambda_function
        
        
        
