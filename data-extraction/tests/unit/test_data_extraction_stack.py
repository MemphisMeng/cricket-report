import aws_cdk as core
import os
import aws_cdk.assertions as assertions

from data_extraction.data_extraction_stack import DataExtractionStack

# example tests. To run these tests, uncomment this file along with the example
# resource in data_extraction/data_extraction_stack.py
def test_sqs_queue_created():
    app = core.App()
    ENV = {"account": os.environ['CDK_DEFAULT_ACCOUNT'], "region": os.environ['CDK_DEFAULT_REGION']} # environment context
    stack = DataExtractionStack(app, "data-extraction", environment="test", code_directory="lambda/", env=ENV)
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
