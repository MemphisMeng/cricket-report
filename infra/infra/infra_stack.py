from aws_cdk import Stack
from aws_cdk.aws_rds import (
    Credentials,
    DatabaseCluster,
    DatabaseClusterEngine,
    AuroraPostgresEngineVersion,
    InstanceProps,
)
import json
from aws_cdk.aws_secretsmanager import Secret, SecretStringGenerator
from constructs import Construct
from aws_cdk.aws_ec2 import Vpc

class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, environment:str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "InfraQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        self.vpc = Vpc(self, f"{environment}-Vpc",
                       vpc_name=f"{environment}-Vpc"
            # ip_addresses=IpAddresses.cidr("10.0.0.0/16")
            )
        self.rds = DatabaseCluster(
            self,
            f"{environment}-cluster-database",
            engine=DatabaseClusterEngine.aurora_postgres(
                version=AuroraPostgresEngineVersion.VER_13_4
            ),
            credentials=Credentials.from_secret(
                Secret(
                    self,
                    "RDSCricketSecret",
                    description=f"Secrets for {environment} Cricket DB",
                    secret_name=f"rds-credentials/cricket-db-{environment}",
                    generate_secret_string=SecretStringGenerator(
                        secret_string_template=json.dumps({"username": "memphis"}),
                        generate_string_key="password",
                        exclude_punctuation=True,
                    ),
                )
            ),
            cluster_identifier=f"{environment}-cricket-cluster",
            port=5432,
            instance_props=InstanceProps(
                vpc=self.vpc,
            ),
        )