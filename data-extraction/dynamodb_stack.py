from aws_cdk.aws_dynamodb import Table, Attribute, AttributeType, StreamViewType, BillingMode
from aws_cdk import core as cdk

class DynamoDBStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, environment: str, 
                 table_name: str, sort_key:str, partition_key:str, lsi_key:str, gsi_key:str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        if sort_key=='':
            table_creation = Table(self, 
                    table_name, 
                    table_name=f"{table_name}-{environment}",
                    partition_key=Attribute(name=partition_key, type=AttributeType.STRING),
                    billing_mode=BillingMode.PAY_PER_REQUEST, 
                    stream = StreamViewType.NEW_AND_OLD_IMAGES
                )
        else:
            table_creation = Table(self, 
                        table_name, 
                        table_name=f"{table_name}-{environment}",
                        partition_key=Attribute(name=partition_key, type=AttributeType.STRING),
                        sort_key=Attribute(name=sort_key,type=AttributeType.STRING),
                        billing_mode=BillingMode.PAY_PER_REQUEST, 
                        stream = StreamViewType.NEW_AND_OLD_IMAGES
                    )
        if lsi_key!='':
            table_creation.add_local_secondary_index( 
                sort_key=Attribute(name=lsi_key,type=AttributeType.STRING),
                index_name=f"{table_name}-{environment}-{lsi_key}-LSI"
            )
        
        if gsi_key!='':
            table_creation.add_global_secondary_index(
                partition_key=Attribute(name=gsi_key,type=AttributeType.STRING),
                index_name=f"{table_name}-{environment}-{gsi_key}-GSI"
            )
            
        # turn on DynamoDB Table Export Stream
        cdk.CfnOutput(self, f"{table_name}-stream-arn", value=table_creation.table_stream_arn,export_name=f"{table_name}-stream-arn-{environment}")