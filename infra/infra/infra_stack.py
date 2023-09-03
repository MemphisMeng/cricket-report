from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk.aws_ec2 import Vpc

class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, environemnt:str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "InfraQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        self.vpc = Vpc(self, f"{environemnt}-Vpc",
                       vpc_name=f"{environemnt}-Vpc"
            # ip_addresses=IpAddresses.cidr("10.0.0.0/16")
            )