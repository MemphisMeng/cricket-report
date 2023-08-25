import builtins
import typing
from aws_cdk.aws_iam import Role, ServicePrincipal, PolicyDocument, PolicyStatement, Effect, ManagedPolicy
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk import core as cdk
import constructs
from aws_cdk.core import Environment, IStackSynthesizer

class InfraStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, env:str, **kwargs) -> None:
        super().__init__(scope, construct_id, env=env, **kwargs)
        self.role = Role(self, "ExecutionRole",
                         role_name=f"{env}-execution-role",
                         description=f"The IAM Role assumed to execute the part that downloads data from the website to the database in the {env} environment",
                        managed_policies=[
                            'arn:aws:iam::aws:policy/AWSLambdaExecute',
                            'arn:aws:iam::aws:policy/AmazonSQSFullAccess',
                            'arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess'
                        ], inline_policies={
                            'misc-policies': PolicyDocument(
                                statements=[
                                    PolicyStatement(
                                        actions=['events:PutEvents'],
                                        effect=Effect.ALLOW,
                                        resources=['*']
                                    ),
                                    PolicyStatement(
                                        actions=['logs:CreateLogGroup', 'logs:CreateLogStream', 'logs:PutLogEvents'],
                                        effect=Effect.ALLOW,
                                        resources=['arn:aws:logs:*:*:*']
                                    )
                                ]
                            )
                        })