import builtins
import typing
from aws_cdk.aws_iam import Role, ServicePrincipal, PolicyDocument, PolicyStatement, Effect, ManagedPolicy
from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk import core as cdk
import constructs
from aws_cdk.core import Environment, IStackSynthesizer

class DownloaderStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, env: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # function
        self.lambda_function = Function(
            self, "Downloader", 
            runtime=Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            function_name=f"{env}-downloader",
            code=Code.from_asset(''),
            ) # TODO: input the directory of function
        # triggering event of the function
        self.event_rule = Rule(self, "Trigger", 
                          schedule=Schedule.cron(
                            year='*',
                            month='*',
                            day='*',
                            week_day='*',
                            hour='?',
                            minute='0'),
                            targets=[self.lambda_function])
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
        