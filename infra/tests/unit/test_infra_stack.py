import aws_cdk as core
import aws_cdk.assertions as assertions
import os
from infra.infra_stack import InfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in infra/infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    ENV = {"account": os.environ['CDK_DEFAULT_ACCOUNT'], "region": os.environ['CDK_DEFAULT_REGION']} # environment context
    stack = InfraStack(app, "infra", environment="test", env=ENV)
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
