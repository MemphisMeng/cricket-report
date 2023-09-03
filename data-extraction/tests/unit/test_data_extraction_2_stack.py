import aws_cdk as core
import aws_cdk.assertions as assertions

from data_extraction.data_extraction_stack import DataExtractionStack

# example tests. To run these tests, uncomment this file along with the example
# resource in data_extraction/data_extraction_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DataExtractionStack(app, "data-extraction-2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
