from aws_cdk.aws_events import Rule, Schedule
from aws_cdk import core as cdk

class RuleStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, name:str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # triggering event of the function
        self.event_rule = Rule(self, name, 
                          schedule=Schedule.cron(
                            year='*',
                            month='*',
                            day='*',
                            week_day='*',
                            hour='?',
                            minute='0'),
                            targets=[self.lambda_function])