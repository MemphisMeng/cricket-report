import os
from infra.lambda_function_stack import LambaFunctionStack
from infra.iam_stack import IAMStack
from infra.rds_stack import RdsStack
from infra.rule_stack import RuleStack
from aws_cdk import App, Tags

# application initiation
app = App()
enviroment = app.node.try_get_context("environment")

account = os.environ["CDK_DEFAULT_ACCOUNT"]
region = os.environ["CDK_DEFAULT_REGION"]

extraction_function = LambaFunctionStack(
    app,
    env=enviroment,
    function="downloader",
    code_directory="code/"
)
rds_cluster = RdsStack(
    app,
    environment=enviroment,
    stack_name="CricketDB",
    cluster_name="cricket"
)

app.synth()