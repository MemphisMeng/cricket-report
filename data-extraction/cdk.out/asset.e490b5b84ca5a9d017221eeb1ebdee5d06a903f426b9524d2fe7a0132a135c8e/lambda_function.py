from service import service
from functions import *
import logging
from pythonjsonlogger import jsonlogger

# Load environment
ENV = config.load_env()

LOGGER = logging.getLogger()
# Replace the LambdaLoggerHandler formatter :
LOGGER.handlers[0].setFormatter(jsonlogger.JsonFormatter())
# Set default logging level
LOGGING_LEVEL = getattr(logging, ENV["LOGGING_LEVEL"])
LOGGER.setLevel(LOGGING_LEVEL)


def _lambda_context(context):
    """
    Extract information relevant from context object.

    Args:
        context: The context object provided by the Lambda runtime.

    Returns:
        dict: A dictionary containing relevant information from the context object.

    """
    return {
        "function_name": context.function_name,
        "function_version": context.function_version,
    }


# @datadog_lambda_wrapper
def lambda_handler(event, context):
    """
    Handle the Lambda event.

    Args:
        event(dict): The event object containing input data for the Lambda function.
        context(dict): The context object provided by the Lambda runtime.

    Returns:
        dict: A dictionary containing the response for the Lambda function.

    """
    LOGGER.info("Starting lambda executing.", extra=_lambda_context(context))
    service.main(event, ENV)
    LOGGER.info("Successful lambda execution.", extra=_lambda_context(context))
    return {"statusCode": 200}
