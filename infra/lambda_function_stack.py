import builtins
import typing
from aws_cdk.aws_iam import Role, ServicePrincipal, PolicyDocument, PolicyStatement, Effect, ManagedPolicy
from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk import core as cdk
import constructs
from aws_cdk.core import Environment, IStackSynthesizer

class LambaFunctionStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, env: str, function:str, code_directory:str, role:Role, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # function
        self.lambda_function = Function(
            self, f"{env}-{function}-Lamba-Function", 
            runtime=Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            function_name=f"{env}-{function}-function",
            code=Code.from_asset(code_directory),
            role=role
            )