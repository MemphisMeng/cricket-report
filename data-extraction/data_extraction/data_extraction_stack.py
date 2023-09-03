import os, json
from constructs import Construct
from aws_cdk.aws_secretsmanager import Secret, SecretStringGenerator
from aws_cdk.aws_iam import Role, ServicePrincipal, PolicyDocument, PolicyStatement, Effect, ManagedPolicy
from aws_cdk.aws_rds import (
    Credentials,
    DatabaseCluster,
    DatabaseClusterEngine,
    AuroraPostgresEngineVersion,
    InstanceProps,
)
from aws_cdk.aws_ec2 import (
    Vpc,
    InstanceClass,
    InstanceType,
    InstanceSize,
    SecurityGroup,
    Port,
    Peer,
)
from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk import Stack


class DataExtractionStack(Stack):

    def __init__(
        self, scope: Construct, construct_id: str, environment: str, code_directory:str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.role = Role(self, "ExecutionRole",
                role_name=f"{environment}-execution-role",
                description=f"The IAM Role assumed to execute the part that downloads data from the website to the database in the {environment} environment",
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

        self.downloader_function = Function(
            self, f"{environment}-Downloader", 
            runtime=Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            function_name=f"{environment}-downloader",
            code=Code.from_asset(code_directory),
            role=self.role
            )
        
        self.rds = DatabaseCluster(
            self,
            f"{environment}-cluster-database",
            engine=DatabaseClusterEngine.aurora_postgres(
                version=AuroraPostgresEngineVersion.VER_14_4
            ),
            credentials=Credentials.from_secret(
                Secret(
                    self,
                    "RDSCricketSecret",
                    description=f"Secrets for {environment} Cricket DB",
                    secret_name=f"rds-credentials/cricket-db-{environment}",
                    generate_secret_string=SecretStringGenerator(
                        secret_string_template=json.dumps({"username": "admin"}),
                        generate_string_key="password",
                        exclude_punctuation=True,
                    ),
                )
            ),
            cluster_identifier=f"{environment}-cricket-cluster",
            # default_database_name="athlete_performance_metrics",
            port=5432,
            # instance_props=InstanceProps(
            #     instance_type=InstanceType.of(InstanceClass.T3, InstanceSize.MEDIUM),
            #     # security_groups=[security_group],
            #     # vpc=vpc,
            # ),
        )