from constructs import Construct
from aws_cdk import Stack
from aws_cdk.aws_secretsmanager import Secret, SecretStringGenerator
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
import json

class RdsStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, environment: str, stack_name:str, cluster_name:str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.cluster = DatabaseCluster(
            self,
            f"{environment}-{stack_name}",
            engine=DatabaseClusterEngine.aurora_postgres(
                version=AuroraPostgresEngineVersion.VER_14_4
            ),
            # credentials=Credentials.from_secret(rds_secret),
            cluster_identifier=f"{environment}-{cluster_name}",
            # default_database_name="athlete_performance_metrics",
            port=5432,
            instance_props=InstanceProps(
                instance_type=InstanceType.of(InstanceClass.T3, InstanceSize.MEDIUM),
                # security_groups=[security_group],
                # vpc=vpc,
            ),
        )