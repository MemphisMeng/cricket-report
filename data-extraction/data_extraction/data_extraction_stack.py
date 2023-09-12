from constructs import Construct
from aws_cdk.aws_iam import Role, ServicePrincipal, PolicyDocument, PolicyStatement, Effect, ManagedPolicy
from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk.aws_lambda_python_alpha import PythonLayerVersion
from aws_cdk.aws_ec2 import (
    Vpc,
    SubnetType,
    SubnetSelection,
)
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk.aws_events_targets import LambdaFunction
from aws_cdk import Stack, BundlingOptions, Environment


class DataExtractionStack(Stack):

    def __init__(
        self, scope: Construct, construct_id: str, environment: str, code_directory:str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.role = Role(self, "ExecutionRole",
                role_name=f"{environment}-execution-role",
                assumed_by=ServicePrincipal('lambda.amazonaws.com'),
                description=f"The IAM Role assumed to execute the part that downloads data from the website to the database in the {environment} environment",
                managed_policies=[
                    ManagedPolicy.from_aws_managed_policy_name('AWSLambda_FullAccess'),
                    ManagedPolicy.from_aws_managed_policy_name('AmazonRDSFullAccess'),
                    ManagedPolicy.from_aws_managed_policy_name('AmazonRDSDataFullAccess'),
                    ManagedPolicy.from_aws_managed_policy_name('SecretsManagerReadWrite')
                ], 
                inline_policies={
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
                        ),
                        PolicyStatement(
                            actions=['ec2:CreateNetworkInterface', 'ec2:DescribeNetworkInterfaces', 'ec2:DeleteNetworkInterface'],
                            effect=Effect.ALLOW,
                            resources=['*']
                        )
                        ]
                    )
                })

        vpc = Vpc.from_lookup(
                self, f"ImportVPC",
                vpc_id='vpc-06feb24bad800e677' 
                # vpc_name=f"{environment}-Vpc"
            )
        selection = vpc.select_subnets(
                    subnet_type=SubnetType.PRIVATE_WITH_EGRESS
                )
        self.downloader_function = Function(
            self, f"{environment}-Downloader", 
            runtime=Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            function_name=f"{environment}-downloader",
            code=Code.from_asset(
                code_directory,
                bundling=BundlingOptions(
                image=Runtime.PYTHON_3_9.bundling_image,
                command=["bash", "-c", "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output"]
            )),
            role=self.role,
            # layers=[
            #     PythonLayerVersion(
            #         self, f"{environment}-Python-Layer",
            #         entry=code_directory,
            #         compatible_runtimes=[Runtime.PYTHON_3_9]
            #     )
            # ],
            vpc=vpc,
            vpc_subnets=SubnetSelection(subnets=selection.subnets),
            environment={'environment': environment}
            )
        self.event_rule = Rule(
                self,
                "LambdaWorkerRule",
                schedule=Schedule.cron(
                    year='*',
                    month='*',
                    day='1',
                    hour='0',
                    minute='0'
                ),
            )
        self.event_rule.add_target(
                LambdaFunction(self.downloader_function, retry_attempts=2)
            )