from constructs import Construct
from aws_cdk.aws_iam import Role, ServicePrincipal, PolicyDocument, PolicyStatement, Effect, ManagedPolicy

from aws_cdk.aws_ec2 import Vpc
from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk import Stack


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
                            )
                        ]
                    )
                })

        self.downloader_function = Function(
            self, f"{environment}-Downloader", 
            runtime=Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            function_name=f"{environment}-downloader",
            code=Code.from_asset(code_directory),
            role=self.role
            )
        vpc = Vpc.from_lookup(self, f"VPC", vpc_name=f"{environment}-Vpc")
        