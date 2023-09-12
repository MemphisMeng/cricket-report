'''
# AWS Systems Manager Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Installation

Install the module:

```console
$ npm i @aws-cdk/aws-ssm
```

Import it into your code:

```python
import aws_cdk.aws_ssm as ssm
```

## Using existing SSM Parameters in your CDK app

You can reference existing SSM Parameter Store values that you want to use in
your CDK app by using `ssm.ParameterStoreString`:

[using SSM parameter](test/integ.parameter-store-string.lit.ts)

## Creating new SSM Parameters in your CDK app

You can create either `ssm.StringParameter` or `ssm.StringListParameter`s in
a CDK app. These are public (not secret) values. Parameters of type
*SecureString* cannot be created directly from a CDK application; if you want
to provision secrets automatically, use Secrets Manager Secrets (see the
`@aws-cdk/aws-secretsmanager` package).

```python
ssm.StringParameter(self, "Parameter",
    allowed_pattern=".*",
    description="The value Foo",
    parameter_name="FooParameter",
    string_value="Foo",
    tier=ssm.ParameterTier.ADVANCED
)
```

[creating SSM parameters](test/integ.parameter.lit.ts)

When specifying an `allowedPattern`, the values provided as string literals
are validated against the pattern and an exception is raised if a value
provided does not comply.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_iam import Grant as _Grant_a7ae64f8, IGrantable as _IGrantable_71c4f5de
from ..aws_kms import IKey as _IKey_5f11635f


@jsii.implements(_IInspectable_c2943556)
class CfnAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation",
):
    '''A CloudFormation ``AWS::SSM::Association``.

    The ``AWS::SSM::Association`` resource creates a State Manager association for your managed instances. A State Manager association defines the state that you want to maintain on your instances. For example, an association can specify that anti-virus software must be installed and running on your instances, or that certain ports must be closed. For static targets, the association specifies a schedule for when the configuration is reapplied. For dynamic targets, such as an AWS Resource Groups or an AWS Auto Scaling Group, State Manager applies the configuration when new instances are added to the group. The association also specifies actions to take when applying the configuration. For example, an association for anti-virus software might run once a day. If the software is not installed, then State Manager installs it. If the software is installed, but the service is not running, then the association might instruct State Manager to start the service.

    :cloudformationResource: AWS::SSM::Association
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        # parameters: Any
        
        cfn_association = ssm.CfnAssociation(self, "MyCfnAssociation",
            name="name",
        
            # the properties below are optional
            apply_only_at_cron_interval=False,
            association_name="associationName",
            automation_target_parameter_name="automationTargetParameterName",
            calendar_names=["calendarNames"],
            compliance_severity="complianceSeverity",
            document_version="documentVersion",
            instance_id="instanceId",
            max_concurrency="maxConcurrency",
            max_errors="maxErrors",
            output_location=ssm.CfnAssociation.InstanceAssociationOutputLocationProperty(
                s3_location=ssm.CfnAssociation.S3OutputLocationProperty(
                    output_s3_bucket_name="outputS3BucketName",
                    output_s3_key_prefix="outputS3KeyPrefix",
                    output_s3_region="outputS3Region"
                )
            ),
            parameters={
                "parameters_key": parameters
            },
            schedule_expression="scheduleExpression",
            sync_compliance="syncCompliance",
            targets=[ssm.CfnAssociation.TargetProperty(
                key="key",
                values=["values"]
            )],
            wait_for_success_timeout_seconds=123
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        association_name: typing.Optional[builtins.str] = None,
        automation_target_parameter_name: typing.Optional[builtins.str] = None,
        calendar_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        compliance_severity: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        output_location: typing.Optional[typing.Union["CfnAssociation.InstanceAssociationOutputLocationProperty", _IResolvable_da3f097b]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]] = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        sync_compliance: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnAssociation.TargetProperty", _IResolvable_da3f097b]]]] = None,
        wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::Association``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the SSM document that contains the configuration information for the instance. You can specify ``Command`` or ``Automation`` documents. The documents can be AWS -predefined documents, documents you created, or a document that is shared with you from another account. For SSM documents that are shared with you from other AWS accounts , you must specify the complete SSM document ARN, in the following format: ``arn:partition:ssm:region:account-id:document/document-name`` For example: ``arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document`` For AWS -predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS -ApplyPatchBaseline or My-Document.
        :param apply_only_at_cron_interval: By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified. Specify this option if you don't want an association to run immediately after you create it. This parameter is not supported for rate expressions.
        :param association_name: Specify a descriptive name for the association.
        :param automation_target_parameter_name: Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a capability of AWS Systems Manager .
        :param calendar_names: The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under. The associations only run when that Change Calendar is open. For more information, see `AWS Systems Manager Change Calendar <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar>`_ .
        :param compliance_severity: The severity level that is assigned to the association.
        :param document_version: The version of the SSM document to associate with the target. .. epigraph:: ``DocumentVersion`` is not valid for documents owned by AWS , such as ``AWS-RunPatchBaseline`` or ``AWS-UpdateSSMAgent`` . If you specify ``DocumentVersion`` for an AWS document, the system returns the following error: "Error occurred during operation 'CreateAssociation'." (RequestToken: , HandlerErrorCode: GeneralServiceException).
        :param instance_id: The ID of the instance that the SSM document is associated with. You must specify the ``InstanceId`` or ``Targets`` property. .. epigraph:: ``InstanceId`` has been deprecated. To specify an instance ID for an association, use the ``Targets`` parameter. If you use the parameter ``InstanceId`` , you cannot use the parameters ``AssociationName`` , ``DocumentVersion`` , ``MaxErrors`` , ``MaxConcurrency`` , ``OutputLocation`` , or ``ScheduleExpression`` . To use these parameters, you must use the ``Targets`` parameter.
        :param max_concurrency: The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time. If a new managed node starts and attempts to run an association while Systems Manager is running ``MaxConcurrency`` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for ``MaxConcurrency`` .
        :param max_errors: The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set ``MaxError`` to 10%, then the system stops sending the request when the sixth error is received. Executions that are already running an association when ``MaxErrors`` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set ``MaxConcurrency`` to 1 so that executions proceed one at a time.
        :param output_location: An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.
        :param parameters: The parameters for the runtime configuration of the document.
        :param schedule_expression: A cron expression that specifies a schedule when the association runs. The schedule runs in Coordinated Universal Time (UTC).
        :param sync_compliance: The mode for generating association compliance. You can specify ``AUTO`` or ``MANUAL`` . In ``AUTO`` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is ``COMPLIANT`` . If the association execution doesn't run successfully, the association is ``NON-COMPLIANT`` . In ``MANUAL`` mode, you must specify the ``AssociationId`` as a parameter for the PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the PutComplianceItems API action. By default, all associations use ``AUTO`` mode.
        :param targets: The targets for the association. You must specify the ``InstanceId`` or ``Targets`` property. You can target all instances in an AWS account by specifying the ``InstanceIds`` key with a value of ``*`` . To view a JSON and a YAML example that targets all instances, see "Create an association for all managed instances in an AWS account " on the Examples page.
        :param wait_for_success_timeout_seconds: The number of seconds the service should wait for the association status to show "Success" before proceeding with the stack execution. If the association status doesn't show "Success" after the specified number of seconds, then stack creation fails.
        '''
        props = CfnAssociationProps(
            name=name,
            apply_only_at_cron_interval=apply_only_at_cron_interval,
            association_name=association_name,
            automation_target_parameter_name=automation_target_parameter_name,
            calendar_names=calendar_names,
            compliance_severity=compliance_severity,
            document_version=document_version,
            instance_id=instance_id,
            max_concurrency=max_concurrency,
            max_errors=max_errors,
            output_location=output_location,
            parameters=parameters,
            schedule_expression=schedule_expression,
            sync_compliance=sync_compliance,
            targets=targets,
            wait_for_success_timeout_seconds=wait_for_success_timeout_seconds,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAssociationId")
    def attr_association_id(self) -> builtins.str:
        '''The association ID.

        :cloudformationAttribute: AssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the SSM document that contains the configuration information for the instance.

        You can specify ``Command`` or ``Automation`` documents. The documents can be AWS -predefined documents, documents you created, or a document that is shared with you from another account. For SSM documents that are shared with you from other AWS accounts , you must specify the complete SSM document ARN, in the following format:

        ``arn:partition:ssm:region:account-id:document/document-name``

        For example: ``arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document``

        For AWS -predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS -ApplyPatchBaseline or My-Document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applyOnlyAtCronInterval")
    def apply_only_at_cron_interval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified.

        Specify this option if you don't want an association to run immediately after you create it. This parameter is not supported for rate expressions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-applyonlyatcroninterval
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "applyOnlyAtCronInterval"))

    @apply_only_at_cron_interval.setter
    def apply_only_at_cron_interval(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "applyOnlyAtCronInterval", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="associationName")
    def association_name(self) -> typing.Optional[builtins.str]:
        '''Specify a descriptive name for the association.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-associationname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associationName"))

    @association_name.setter
    def association_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "associationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automationTargetParameterName")
    def automation_target_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Choose the parameter that will define how your automation will branch out.

        This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a capability of AWS Systems Manager .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-automationtargetparametername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "automationTargetParameterName"))

    @automation_target_parameter_name.setter
    def automation_target_parameter_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "automationTargetParameterName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="calendarNames")
    def calendar_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under.

        The associations only run when that Change Calendar is open. For more information, see `AWS Systems Manager Change Calendar <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-calendarnames
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "calendarNames"))

    @calendar_names.setter
    def calendar_names(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "calendarNames", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="complianceSeverity")
    def compliance_severity(self) -> typing.Optional[builtins.str]:
        '''The severity level that is assigned to the association.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-complianceseverity
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complianceSeverity"))

    @compliance_severity.setter
    def compliance_severity(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "complianceSeverity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> typing.Optional[builtins.str]:
        '''The version of the SSM document to associate with the target.

        .. epigraph::

           ``DocumentVersion`` is not valid for documents owned by AWS , such as ``AWS-RunPatchBaseline`` or ``AWS-UpdateSSMAgent`` . If you specify ``DocumentVersion`` for an AWS document, the system returns the following error: "Error occurred during operation 'CreateAssociation'." (RequestToken: , HandlerErrorCode: GeneralServiceException).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-documentversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentVersion"))

    @document_version.setter
    def document_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "documentVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the instance that the SSM document is associated with.

        You must specify the ``InstanceId`` or ``Targets`` property.
        .. epigraph::

           ``InstanceId`` has been deprecated. To specify an instance ID for an association, use the ``Targets`` parameter. If you use the parameter ``InstanceId`` , you cannot use the parameters ``AssociationName`` , ``DocumentVersion`` , ``MaxErrors`` , ``MaxConcurrency`` , ``OutputLocation`` , or ``ScheduleExpression`` . To use these parameters, you must use the ``Targets`` parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-instanceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "instanceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''The maximum number of targets allowed to run the association at the same time.

        You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.

        If a new managed node starts and attempts to run an association while Systems Manager is running ``MaxConcurrency`` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for ``MaxConcurrency`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxconcurrency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "maxConcurrency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''The number of errors that are allowed before the system stops sending requests to run the association on additional targets.

        You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set ``MaxError`` to 10%, then the system stops sending the request when the sixth error is received.

        Executions that are already running an association when ``MaxErrors`` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set ``MaxConcurrency`` to 1 so that executions proceed one at a time.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxerrors
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxErrors"))

    @max_errors.setter
    def max_errors(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "maxErrors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outputLocation")
    def output_location(
        self,
    ) -> typing.Optional[typing.Union["CfnAssociation.InstanceAssociationOutputLocationProperty", _IResolvable_da3f097b]]:
        '''An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-outputlocation
        '''
        return typing.cast(typing.Optional[typing.Union["CfnAssociation.InstanceAssociationOutputLocationProperty", _IResolvable_da3f097b]], jsii.get(self, "outputLocation"))

    @output_location.setter
    def output_location(
        self,
        value: typing.Optional[typing.Union["CfnAssociation.InstanceAssociationOutputLocationProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "outputLocation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]]:
        '''The parameters for the runtime configuration of the document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> typing.Optional[builtins.str]:
        '''A cron expression that specifies a schedule when the association runs.

        The schedule runs in Coordinated Universal Time (UTC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleexpression
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "scheduleExpression", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncCompliance")
    def sync_compliance(self) -> typing.Optional[builtins.str]:
        '''The mode for generating association compliance.

        You can specify ``AUTO`` or ``MANUAL`` . In ``AUTO`` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is ``COMPLIANT`` . If the association execution doesn't run successfully, the association is ``NON-COMPLIANT`` .

        In ``MANUAL`` mode, you must specify the ``AssociationId`` as a parameter for the PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the PutComplianceItems API action.

        By default, all associations use ``AUTO`` mode.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-synccompliance
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncCompliance"))

    @sync_compliance.setter
    def sync_compliance(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "syncCompliance", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnAssociation.TargetProperty", _IResolvable_da3f097b]]]]:
        '''The targets for the association.

        You must specify the ``InstanceId`` or ``Targets`` property. You can target all instances in an AWS account by specifying the ``InstanceIds`` key with a value of ``*`` . To view a JSON and a YAML example that targets all instances, see "Create an association for all managed instances in an AWS account " on the Examples page.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-targets
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnAssociation.TargetProperty", _IResolvable_da3f097b]]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnAssociation.TargetProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "targets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="waitForSuccessTimeoutSeconds")
    def wait_for_success_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds the service should wait for the association status to show "Success" before proceeding with the stack execution.

        If the association status doesn't show "Success" after the specified number of seconds, then stack creation fails.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-waitforsuccesstimeoutseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitForSuccessTimeoutSeconds"))

    @wait_for_success_timeout_seconds.setter
    def wait_for_success_timeout_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        jsii.set(self, "waitForSuccessTimeoutSeconds", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.InstanceAssociationOutputLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_location": "s3Location"},
    )
    class InstanceAssociationOutputLocationProperty:
        def __init__(
            self,
            *,
            s3_location: typing.Optional[typing.Union["CfnAssociation.S3OutputLocationProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''``InstanceAssociationOutputLocation`` is a property of the `AWS::SSM::Association <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html>`_ resource that specifies an Amazon S3 bucket where you want to store the results of this association request.

            For the minimal permissions required to enable Amazon S3 output for an association, see `Creating associations <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc.html>`_ in the *Systems Manager User Guide* .

            :param s3_location: ``S3OutputLocation`` is a property of the `InstanceAssociationOutputLocation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html>`_ property that specifies an Amazon S3 bucket where you want to store the results of this request.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                instance_association_output_location_property = ssm.CfnAssociation.InstanceAssociationOutputLocationProperty(
                    s3_location=ssm.CfnAssociation.S3OutputLocationProperty(
                        output_s3_bucket_name="outputS3BucketName",
                        output_s3_key_prefix="outputS3KeyPrefix",
                        output_s3_region="outputS3Region"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def s3_location(
            self,
        ) -> typing.Optional[typing.Union["CfnAssociation.S3OutputLocationProperty", _IResolvable_da3f097b]]:
            '''``S3OutputLocation`` is a property of the `InstanceAssociationOutputLocation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html>`_ property that specifies an Amazon S3 bucket where you want to store the results of this request.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html#cfn-ssm-association-instanceassociationoutputlocation-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[typing.Union["CfnAssociation.S3OutputLocationProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceAssociationOutputLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.S3OutputLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "output_s3_bucket_name": "outputS3BucketName",
            "output_s3_key_prefix": "outputS3KeyPrefix",
            "output_s3_region": "outputS3Region",
        },
    )
    class S3OutputLocationProperty:
        def __init__(
            self,
            *,
            output_s3_bucket_name: typing.Optional[builtins.str] = None,
            output_s3_key_prefix: typing.Optional[builtins.str] = None,
            output_s3_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``S3OutputLocation`` is a property of the `AWS::SSM::Association <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html>`_ resource that specifies an Amazon S3 bucket where you want to store the results of this association request.

            :param output_s3_bucket_name: The name of the S3 bucket.
            :param output_s3_key_prefix: The S3 bucket subfolder.
            :param output_s3_region: The AWS Region of the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                s3_output_location_property = ssm.CfnAssociation.S3OutputLocationProperty(
                    output_s3_bucket_name="outputS3BucketName",
                    output_s3_key_prefix="outputS3KeyPrefix",
                    output_s3_region="outputS3Region"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if output_s3_bucket_name is not None:
                self._values["output_s3_bucket_name"] = output_s3_bucket_name
            if output_s3_key_prefix is not None:
                self._values["output_s3_key_prefix"] = output_s3_key_prefix
            if output_s3_region is not None:
                self._values["output_s3_region"] = output_s3_region

        @builtins.property
        def output_s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3bucketname
            '''
            result = self._values.get("output_s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 bucket subfolder.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3keyprefix
            '''
            result = self._values.get("output_s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_s3_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region of the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3region
            '''
            result = self._values.get("output_s3_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnAssociation.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''``Target`` is a property of the `AWS::SSM::Association <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html>`_ resource that specifies the targets for an SSM document in Systems Manager . You can target all instances in an AWS account by specifying the ``InstanceIds`` key with a value of ``*`` . To view a JSON and a YAML example that targets all instances, see "Create an association for all managed instances in an AWS account " on the Examples page.

            :param key: User-defined criteria for sending commands that target managed nodes that meet the criteria.
            :param values: User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include EC2 tags of ``ServerRole,WebServer`` . Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                target_property = ssm.CfnAssociation.TargetProperty(
                    key="key",
                    values=["values"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''User-defined criteria for sending commands that target managed nodes that meet the criteria.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''User-defined criteria that maps to ``Key`` .

            For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include EC2 tags of ``ServerRole,WebServer`` .

            Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "apply_only_at_cron_interval": "applyOnlyAtCronInterval",
        "association_name": "associationName",
        "automation_target_parameter_name": "automationTargetParameterName",
        "calendar_names": "calendarNames",
        "compliance_severity": "complianceSeverity",
        "document_version": "documentVersion",
        "instance_id": "instanceId",
        "max_concurrency": "maxConcurrency",
        "max_errors": "maxErrors",
        "output_location": "outputLocation",
        "parameters": "parameters",
        "schedule_expression": "scheduleExpression",
        "sync_compliance": "syncCompliance",
        "targets": "targets",
        "wait_for_success_timeout_seconds": "waitForSuccessTimeoutSeconds",
    },
)
class CfnAssociationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        apply_only_at_cron_interval: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        association_name: typing.Optional[builtins.str] = None,
        automation_target_parameter_name: typing.Optional[builtins.str] = None,
        calendar_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        compliance_severity: typing.Optional[builtins.str] = None,
        document_version: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        output_location: typing.Optional[typing.Union[CfnAssociation.InstanceAssociationOutputLocationProperty, _IResolvable_da3f097b]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]] = None,
        schedule_expression: typing.Optional[builtins.str] = None,
        sync_compliance: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnAssociation.TargetProperty, _IResolvable_da3f097b]]]] = None,
        wait_for_success_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssociation``.

        :param name: The name of the SSM document that contains the configuration information for the instance. You can specify ``Command`` or ``Automation`` documents. The documents can be AWS -predefined documents, documents you created, or a document that is shared with you from another account. For SSM documents that are shared with you from other AWS accounts , you must specify the complete SSM document ARN, in the following format: ``arn:partition:ssm:region:account-id:document/document-name`` For example: ``arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document`` For AWS -predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS -ApplyPatchBaseline or My-Document.
        :param apply_only_at_cron_interval: By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified. Specify this option if you don't want an association to run immediately after you create it. This parameter is not supported for rate expressions.
        :param association_name: Specify a descriptive name for the association.
        :param automation_target_parameter_name: Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a capability of AWS Systems Manager .
        :param calendar_names: The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under. The associations only run when that Change Calendar is open. For more information, see `AWS Systems Manager Change Calendar <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar>`_ .
        :param compliance_severity: The severity level that is assigned to the association.
        :param document_version: The version of the SSM document to associate with the target. .. epigraph:: ``DocumentVersion`` is not valid for documents owned by AWS , such as ``AWS-RunPatchBaseline`` or ``AWS-UpdateSSMAgent`` . If you specify ``DocumentVersion`` for an AWS document, the system returns the following error: "Error occurred during operation 'CreateAssociation'." (RequestToken: , HandlerErrorCode: GeneralServiceException).
        :param instance_id: The ID of the instance that the SSM document is associated with. You must specify the ``InstanceId`` or ``Targets`` property. .. epigraph:: ``InstanceId`` has been deprecated. To specify an instance ID for an association, use the ``Targets`` parameter. If you use the parameter ``InstanceId`` , you cannot use the parameters ``AssociationName`` , ``DocumentVersion`` , ``MaxErrors`` , ``MaxConcurrency`` , ``OutputLocation`` , or ``ScheduleExpression`` . To use these parameters, you must use the ``Targets`` parameter.
        :param max_concurrency: The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time. If a new managed node starts and attempts to run an association while Systems Manager is running ``MaxConcurrency`` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for ``MaxConcurrency`` .
        :param max_errors: The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set ``MaxError`` to 10%, then the system stops sending the request when the sixth error is received. Executions that are already running an association when ``MaxErrors`` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set ``MaxConcurrency`` to 1 so that executions proceed one at a time.
        :param output_location: An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.
        :param parameters: The parameters for the runtime configuration of the document.
        :param schedule_expression: A cron expression that specifies a schedule when the association runs. The schedule runs in Coordinated Universal Time (UTC).
        :param sync_compliance: The mode for generating association compliance. You can specify ``AUTO`` or ``MANUAL`` . In ``AUTO`` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is ``COMPLIANT`` . If the association execution doesn't run successfully, the association is ``NON-COMPLIANT`` . In ``MANUAL`` mode, you must specify the ``AssociationId`` as a parameter for the PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the PutComplianceItems API action. By default, all associations use ``AUTO`` mode.
        :param targets: The targets for the association. You must specify the ``InstanceId`` or ``Targets`` property. You can target all instances in an AWS account by specifying the ``InstanceIds`` key with a value of ``*`` . To view a JSON and a YAML example that targets all instances, see "Create an association for all managed instances in an AWS account " on the Examples page.
        :param wait_for_success_timeout_seconds: The number of seconds the service should wait for the association status to show "Success" before proceeding with the stack execution. If the association status doesn't show "Success" after the specified number of seconds, then stack creation fails.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            # parameters: Any
            
            cfn_association_props = ssm.CfnAssociationProps(
                name="name",
            
                # the properties below are optional
                apply_only_at_cron_interval=False,
                association_name="associationName",
                automation_target_parameter_name="automationTargetParameterName",
                calendar_names=["calendarNames"],
                compliance_severity="complianceSeverity",
                document_version="documentVersion",
                instance_id="instanceId",
                max_concurrency="maxConcurrency",
                max_errors="maxErrors",
                output_location=ssm.CfnAssociation.InstanceAssociationOutputLocationProperty(
                    s3_location=ssm.CfnAssociation.S3OutputLocationProperty(
                        output_s3_bucket_name="outputS3BucketName",
                        output_s3_key_prefix="outputS3KeyPrefix",
                        output_s3_region="outputS3Region"
                    )
                ),
                parameters={
                    "parameters_key": parameters
                },
                schedule_expression="scheduleExpression",
                sync_compliance="syncCompliance",
                targets=[ssm.CfnAssociation.TargetProperty(
                    key="key",
                    values=["values"]
                )],
                wait_for_success_timeout_seconds=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if apply_only_at_cron_interval is not None:
            self._values["apply_only_at_cron_interval"] = apply_only_at_cron_interval
        if association_name is not None:
            self._values["association_name"] = association_name
        if automation_target_parameter_name is not None:
            self._values["automation_target_parameter_name"] = automation_target_parameter_name
        if calendar_names is not None:
            self._values["calendar_names"] = calendar_names
        if compliance_severity is not None:
            self._values["compliance_severity"] = compliance_severity
        if document_version is not None:
            self._values["document_version"] = document_version
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_errors is not None:
            self._values["max_errors"] = max_errors
        if output_location is not None:
            self._values["output_location"] = output_location
        if parameters is not None:
            self._values["parameters"] = parameters
        if schedule_expression is not None:
            self._values["schedule_expression"] = schedule_expression
        if sync_compliance is not None:
            self._values["sync_compliance"] = sync_compliance
        if targets is not None:
            self._values["targets"] = targets
        if wait_for_success_timeout_seconds is not None:
            self._values["wait_for_success_timeout_seconds"] = wait_for_success_timeout_seconds

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the SSM document that contains the configuration information for the instance.

        You can specify ``Command`` or ``Automation`` documents. The documents can be AWS -predefined documents, documents you created, or a document that is shared with you from another account. For SSM documents that are shared with you from other AWS accounts , you must specify the complete SSM document ARN, in the following format:

        ``arn:partition:ssm:region:account-id:document/document-name``

        For example: ``arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document``

        For AWS -predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS -ApplyPatchBaseline or My-Document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_only_at_cron_interval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified.

        Specify this option if you don't want an association to run immediately after you create it. This parameter is not supported for rate expressions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-applyonlyatcroninterval
        '''
        result = self._values.get("apply_only_at_cron_interval")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def association_name(self) -> typing.Optional[builtins.str]:
        '''Specify a descriptive name for the association.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-associationname
        '''
        result = self._values.get("association_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automation_target_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Choose the parameter that will define how your automation will branch out.

        This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a capability of AWS Systems Manager .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-automationtargetparametername
        '''
        result = self._values.get("automation_target_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def calendar_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under.

        The associations only run when that Change Calendar is open. For more information, see `AWS Systems Manager Change Calendar <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-calendarnames
        '''
        result = self._values.get("calendar_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def compliance_severity(self) -> typing.Optional[builtins.str]:
        '''The severity level that is assigned to the association.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-complianceseverity
        '''
        result = self._values.get("compliance_severity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_version(self) -> typing.Optional[builtins.str]:
        '''The version of the SSM document to associate with the target.

        .. epigraph::

           ``DocumentVersion`` is not valid for documents owned by AWS , such as ``AWS-RunPatchBaseline`` or ``AWS-UpdateSSMAgent`` . If you specify ``DocumentVersion`` for an AWS document, the system returns the following error: "Error occurred during operation 'CreateAssociation'." (RequestToken: , HandlerErrorCode: GeneralServiceException).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-documentversion
        '''
        result = self._values.get("document_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the instance that the SSM document is associated with.

        You must specify the ``InstanceId`` or ``Targets`` property.
        .. epigraph::

           ``InstanceId`` has been deprecated. To specify an instance ID for an association, use the ``Targets`` parameter. If you use the parameter ``InstanceId`` , you cannot use the parameters ``AssociationName`` , ``DocumentVersion`` , ``MaxErrors`` , ``MaxConcurrency`` , ``OutputLocation`` , or ``ScheduleExpression`` . To use these parameters, you must use the ``Targets`` parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-instanceid
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''The maximum number of targets allowed to run the association at the same time.

        You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.

        If a new managed node starts and attempts to run an association while Systems Manager is running ``MaxConcurrency`` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for ``MaxConcurrency`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxconcurrency
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''The number of errors that are allowed before the system stops sending requests to run the association on additional targets.

        You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set ``MaxError`` to 10%, then the system stops sending the request when the sixth error is received.

        Executions that are already running an association when ``MaxErrors`` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set ``MaxConcurrency`` to 1 so that executions proceed one at a time.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-maxerrors
        '''
        result = self._values.get("max_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_location(
        self,
    ) -> typing.Optional[typing.Union[CfnAssociation.InstanceAssociationOutputLocationProperty, _IResolvable_da3f097b]]:
        '''An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-outputlocation
        '''
        result = self._values.get("output_location")
        return typing.cast(typing.Optional[typing.Union[CfnAssociation.InstanceAssociationOutputLocationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]]:
        '''The parameters for the runtime configuration of the document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Any]]], result)

    @builtins.property
    def schedule_expression(self) -> typing.Optional[builtins.str]:
        '''A cron expression that specifies a schedule when the association runs.

        The schedule runs in Coordinated Universal Time (UTC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleexpression
        '''
        result = self._values.get("schedule_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_compliance(self) -> typing.Optional[builtins.str]:
        '''The mode for generating association compliance.

        You can specify ``AUTO`` or ``MANUAL`` . In ``AUTO`` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is ``COMPLIANT`` . If the association execution doesn't run successfully, the association is ``NON-COMPLIANT`` .

        In ``MANUAL`` mode, you must specify the ``AssociationId`` as a parameter for the PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the PutComplianceItems API action.

        By default, all associations use ``AUTO`` mode.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-synccompliance
        '''
        result = self._values.get("sync_compliance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnAssociation.TargetProperty, _IResolvable_da3f097b]]]]:
        '''The targets for the association.

        You must specify the ``InstanceId`` or ``Targets`` property. You can target all instances in an AWS account by specifying the ``InstanceIds`` key with a value of ``*`` . To view a JSON and a YAML example that targets all instances, see "Create an association for all managed instances in an AWS account " on the Examples page.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-targets
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnAssociation.TargetProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def wait_for_success_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds the service should wait for the association status to show "Success" before proceeding with the stack execution.

        If the association status doesn't show "Success" after the specified number of seconds, then stack creation fails.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-waitforsuccesstimeoutseconds
        '''
        result = self._values.get("wait_for_success_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDocument(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnDocument",
):
    '''A CloudFormation ``AWS::SSM::Document``.

    The ``AWS::SSM::Document`` resource creates a Systems Manager (SSM) document in AWS Systems Manager . This document defines the actions that Systems Manager performs on your AWS resources.
    .. epigraph::

       This resource does not support CloudFormation drift detection.

    :cloudformationResource: AWS::SSM::Document
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        # content: Any
        
        cfn_document = ssm.CfnDocument(self, "MyCfnDocument",
            content=content,
        
            # the properties below are optional
            attachments=[ssm.CfnDocument.AttachmentsSourceProperty(
                key="key",
                name="name",
                values=["values"]
            )],
            document_format="documentFormat",
            document_type="documentType",
            name="name",
            requires=[ssm.CfnDocument.DocumentRequiresProperty(
                name="name",
                version="version"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_type="targetType",
            version_name="versionName"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        content: typing.Any,
        attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDocument.AttachmentsSourceProperty", _IResolvable_da3f097b]]]] = None,
        document_format: typing.Optional[builtins.str] = None,
        document_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        requires: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnDocument.DocumentRequiresProperty", _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        target_type: typing.Optional[builtins.str] = None,
        version_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::Document``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param content: The content for the new SSM document in JSON or YAML. .. epigraph:: This parameter also supports ``String`` data types.
        :param attachments: A list of key-value pairs that describe attachments to a version of a document.
        :param document_format: Specify the document format for the request. The document format can be JSON or YAML. JSON is the default format. .. epigraph:: ``TEXT`` is not supported, even though it is listed in the ``Allowed values`` .
        :param document_type: The type of document to create. *Allowed Values* : ``ApplicationConfigurationSchema`` | ``Automation`` | ``Automation.ChangeTemplate`` | ``Command`` | ``DeploymentStrategy`` | ``Package`` | ``Policy`` | ``Session``
        :param name: A name for the SSM document. .. epigraph:: You can't use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes: - ``aws-`` - ``amazon`` - ``amzn``
        :param requires: A list of SSM documents required by a document. This parameter is used exclusively by AWS AppConfig . When a user creates an AWS AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an ``ApplicationConfiguration`` document requires an ``ApplicationConfigurationSchema`` document for validation purposes. For more information, see `What is AWS AppConfig ? <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .
        :param tags: AWS CloudFormation resource tags to apply to the document. Use tags to help you identify and categorize resources.
        :param target_type: Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: ``/AWS::EC2::Instance`` . If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see `AWS resource and property types reference <https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ in the *AWS CloudFormation User Guide* .
        :param version_name: An optional field specifying the version of the artifact you are creating with the document. For example, "Release 12, Update 6". This value is unique across all versions of a document, and can't be changed.
        '''
        props = CfnDocumentProps(
            content=content,
            attachments=attachments,
            document_format=document_format,
            document_type=document_type,
            name=name,
            requires=requires,
            tags=tags,
            target_type=target_type,
            version_name=version_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''AWS CloudFormation resource tags to apply to the document.

        Use tags to help you identify and categorize resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> typing.Any:
        '''The content for the new SSM document in JSON or YAML.

        .. epigraph::

           This parameter also supports ``String`` data types.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-content
        '''
        return typing.cast(typing.Any, jsii.get(self, "content"))

    @content.setter
    def content(self, value: typing.Any) -> None:
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attachments")
    def attachments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDocument.AttachmentsSourceProperty", _IResolvable_da3f097b]]]]:
        '''A list of key-value pairs that describe attachments to a version of a document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-attachments
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDocument.AttachmentsSourceProperty", _IResolvable_da3f097b]]]], jsii.get(self, "attachments"))

    @attachments.setter
    def attachments(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDocument.AttachmentsSourceProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "attachments", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="documentFormat")
    def document_format(self) -> typing.Optional[builtins.str]:
        '''Specify the document format for the request.

        The document format can be JSON or YAML. JSON is the default format.
        .. epigraph::

           ``TEXT`` is not supported, even though it is listed in the ``Allowed values`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documentformat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentFormat"))

    @document_format.setter
    def document_format(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "documentFormat", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> typing.Optional[builtins.str]:
        '''The type of document to create.

        *Allowed Values* : ``ApplicationConfigurationSchema`` | ``Automation`` | ``Automation.ChangeTemplate`` | ``Command`` | ``DeploymentStrategy`` | ``Package`` | ``Policy`` | ``Session``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documenttype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentType"))

    @document_type.setter
    def document_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "documentType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the SSM document.

        .. epigraph::

           You can't use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes:

           - ``aws-``
           - ``amazon``
           - ``amzn``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="requires")
    def requires(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDocument.DocumentRequiresProperty", _IResolvable_da3f097b]]]]:
        '''A list of SSM documents required by a document.

        This parameter is used exclusively by AWS AppConfig . When a user creates an AWS AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an ``ApplicationConfiguration`` document requires an ``ApplicationConfigurationSchema`` document for validation purposes. For more information, see `What is AWS AppConfig ? <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-requires
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDocument.DocumentRequiresProperty", _IResolvable_da3f097b]]]], jsii.get(self, "requires"))

    @requires.setter
    def requires(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDocument.DocumentRequiresProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "requires", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> typing.Optional[builtins.str]:
        '''Specify a target type to define the kinds of resources the document can run on.

        For example, to run a document on EC2 instances, specify the following value: ``/AWS::EC2::Instance`` . If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see `AWS resource and property types reference <https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ in the *AWS CloudFormation User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-targettype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "targetType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionName")
    def version_name(self) -> typing.Optional[builtins.str]:
        '''An optional field specifying the version of the artifact you are creating with the document.

        For example, "Release 12, Update 6". This value is unique across all versions of a document, and can't be changed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-versionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionName"))

    @version_name.setter
    def version_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnDocument.AttachmentsSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "name": "name", "values": "values"},
    )
    class AttachmentsSourceProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Identifying information about a document attachment, including the file name and a key-value pair that identifies the location of an attachment to a document.

            :param key: The key of a key-value pair that identifies the location of an attachment to a document.
            :param name: The name of the document attachment file.
            :param values: The value of a key-value pair that identifies the location of an attachment to a document. The format for *Value* depends on the type of key you specify. - For the key *SourceUrl* , the value is an S3 bucket location. For example: ``"Values": [ "s3://doc-example-bucket/my-folder" ]`` - For the key *S3FileUrl* , the value is a file in an S3 bucket. For example: ``"Values": [ "s3://doc-example-bucket/my-folder/my-file.py" ]`` - For the key *AttachmentReference* , the value is constructed from the name of another SSM document in your account, a version number of that document, and a file attached to that document version that you want to reuse. For example: ``"Values": [ "MyOtherDocument/3/my-other-file.py" ]`` However, if the SSM document is shared with you from another account, the full SSM document ARN must be specified instead of the document name only. For example: ``"Values": [ "arn:aws:ssm:us-east-2:111122223333:document/OtherAccountDocument/3/their-file.py" ]``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                attachments_source_property = ssm.CfnDocument.AttachmentsSourceProperty(
                    key="key",
                    name="name",
                    values=["values"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if name is not None:
                self._values["name"] = name
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key of a key-value pair that identifies the location of an attachment to a document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html#cfn-ssm-document-attachmentssource-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the document attachment file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html#cfn-ssm-document-attachmentssource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The value of a key-value pair that identifies the location of an attachment to a document.

            The format for *Value* depends on the type of key you specify.

            - For the key *SourceUrl* , the value is an S3 bucket location. For example:

            ``"Values": [ "s3://doc-example-bucket/my-folder" ]``

            - For the key *S3FileUrl* , the value is a file in an S3 bucket. For example:

            ``"Values": [ "s3://doc-example-bucket/my-folder/my-file.py" ]``

            - For the key *AttachmentReference* , the value is constructed from the name of another SSM document in your account, a version number of that document, and a file attached to that document version that you want to reuse. For example:

            ``"Values": [ "MyOtherDocument/3/my-other-file.py" ]``

            However, if the SSM document is shared with you from another account, the full SSM document ARN must be specified instead of the document name only. For example:

            ``"Values": [ "arn:aws:ssm:us-east-2:111122223333:document/OtherAccountDocument/3/their-file.py" ]``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html#cfn-ssm-document-attachmentssource-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttachmentsSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnDocument.DocumentRequiresProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class DocumentRequiresProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An SSM document required by the current document.

            :param name: The name of the required SSM document. The name can be an Amazon Resource Name (ARN).
            :param version: The document version required by the current document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                document_requires_property = ssm.CfnDocument.DocumentRequiresProperty(
                    name="name",
                    version="version"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the required SSM document.

            The name can be an Amazon Resource Name (ARN).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html#cfn-ssm-document-documentrequires-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The document version required by the current document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html#cfn-ssm-document-documentrequires-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentRequiresProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnDocumentProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "attachments": "attachments",
        "document_format": "documentFormat",
        "document_type": "documentType",
        "name": "name",
        "requires": "requires",
        "tags": "tags",
        "target_type": "targetType",
        "version_name": "versionName",
    },
)
class CfnDocumentProps:
    def __init__(
        self,
        *,
        content: typing.Any,
        attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnDocument.AttachmentsSourceProperty, _IResolvable_da3f097b]]]] = None,
        document_format: typing.Optional[builtins.str] = None,
        document_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        requires: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnDocument.DocumentRequiresProperty, _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
        target_type: typing.Optional[builtins.str] = None,
        version_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDocument``.

        :param content: The content for the new SSM document in JSON or YAML. .. epigraph:: This parameter also supports ``String`` data types.
        :param attachments: A list of key-value pairs that describe attachments to a version of a document.
        :param document_format: Specify the document format for the request. The document format can be JSON or YAML. JSON is the default format. .. epigraph:: ``TEXT`` is not supported, even though it is listed in the ``Allowed values`` .
        :param document_type: The type of document to create. *Allowed Values* : ``ApplicationConfigurationSchema`` | ``Automation`` | ``Automation.ChangeTemplate`` | ``Command`` | ``DeploymentStrategy`` | ``Package`` | ``Policy`` | ``Session``
        :param name: A name for the SSM document. .. epigraph:: You can't use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes: - ``aws-`` - ``amazon`` - ``amzn``
        :param requires: A list of SSM documents required by a document. This parameter is used exclusively by AWS AppConfig . When a user creates an AWS AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an ``ApplicationConfiguration`` document requires an ``ApplicationConfigurationSchema`` document for validation purposes. For more information, see `What is AWS AppConfig ? <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .
        :param tags: AWS CloudFormation resource tags to apply to the document. Use tags to help you identify and categorize resources.
        :param target_type: Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: ``/AWS::EC2::Instance`` . If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see `AWS resource and property types reference <https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ in the *AWS CloudFormation User Guide* .
        :param version_name: An optional field specifying the version of the artifact you are creating with the document. For example, "Release 12, Update 6". This value is unique across all versions of a document, and can't be changed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            # content: Any
            
            cfn_document_props = ssm.CfnDocumentProps(
                content=content,
            
                # the properties below are optional
                attachments=[ssm.CfnDocument.AttachmentsSourceProperty(
                    key="key",
                    name="name",
                    values=["values"]
                )],
                document_format="documentFormat",
                document_type="documentType",
                name="name",
                requires=[ssm.CfnDocument.DocumentRequiresProperty(
                    name="name",
                    version="version"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_type="targetType",
                version_name="versionName"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if attachments is not None:
            self._values["attachments"] = attachments
        if document_format is not None:
            self._values["document_format"] = document_format
        if document_type is not None:
            self._values["document_type"] = document_type
        if name is not None:
            self._values["name"] = name
        if requires is not None:
            self._values["requires"] = requires
        if tags is not None:
            self._values["tags"] = tags
        if target_type is not None:
            self._values["target_type"] = target_type
        if version_name is not None:
            self._values["version_name"] = version_name

    @builtins.property
    def content(self) -> typing.Any:
        '''The content for the new SSM document in JSON or YAML.

        .. epigraph::

           This parameter also supports ``String`` data types.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def attachments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDocument.AttachmentsSourceProperty, _IResolvable_da3f097b]]]]:
        '''A list of key-value pairs that describe attachments to a version of a document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-attachments
        '''
        result = self._values.get("attachments")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDocument.AttachmentsSourceProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def document_format(self) -> typing.Optional[builtins.str]:
        '''Specify the document format for the request.

        The document format can be JSON or YAML. JSON is the default format.
        .. epigraph::

           ``TEXT`` is not supported, even though it is listed in the ``Allowed values`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documentformat
        '''
        result = self._values.get("document_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_type(self) -> typing.Optional[builtins.str]:
        '''The type of document to create.

        *Allowed Values* : ``ApplicationConfigurationSchema`` | ``Automation`` | ``Automation.ChangeTemplate`` | ``Command`` | ``DeploymentStrategy`` | ``Package`` | ``Policy`` | ``Session``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documenttype
        '''
        result = self._values.get("document_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the SSM document.

        .. epigraph::

           You can't use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes:

           - ``aws-``
           - ``amazon``
           - ``amzn``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requires(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDocument.DocumentRequiresProperty, _IResolvable_da3f097b]]]]:
        '''A list of SSM documents required by a document.

        This parameter is used exclusively by AWS AppConfig . When a user creates an AWS AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an ``ApplicationConfiguration`` document requires an ``ApplicationConfigurationSchema`` document for validation purposes. For more information, see `What is AWS AppConfig ? <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-requires
        '''
        result = self._values.get("requires")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDocument.DocumentRequiresProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''AWS CloudFormation resource tags to apply to the document.

        Use tags to help you identify and categorize resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def target_type(self) -> typing.Optional[builtins.str]:
        '''Specify a target type to define the kinds of resources the document can run on.

        For example, to run a document on EC2 instances, specify the following value: ``/AWS::EC2::Instance`` . If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see `AWS resource and property types reference <https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ in the *AWS CloudFormation User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-targettype
        '''
        result = self._values.get("target_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_name(self) -> typing.Optional[builtins.str]:
        '''An optional field specifying the version of the artifact you are creating with the document.

        For example, "Release 12, Update 6". This value is unique across all versions of a document, and can't be changed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-versionname
        '''
        result = self._values.get("version_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaintenanceWindow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindow",
):
    '''A CloudFormation ``AWS::SSM::MaintenanceWindow``.

    The ``AWS::SSM::MaintenanceWindow`` resource represents general information about a maintenance window for AWS Systems Manager . Maintenance Windows let you define a schedule for when to perform potentially disruptive actions on your instances, such as patching an operating system (OS), updating drivers, or installing software. Each maintenance window has a schedule, a duration, a set of registered targets, and a set of registered tasks.

    For more information, see `Systems Manager Maintenance Windows <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html>`_ in the *AWS Systems Manager User Guide* and `CreateMaintenanceWindow <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateMaintenanceWindow.html>`_ in the *AWS Systems Manager API Reference* .

    :cloudformationResource: AWS::SSM::MaintenanceWindow
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        cfn_maintenance_window = ssm.CfnMaintenanceWindow(self, "MyCfnMaintenanceWindow",
            allow_unassociated_targets=False,
            cutoff=123,
            duration=123,
            name="name",
            schedule="schedule",
        
            # the properties below are optional
            description="description",
            end_date="endDate",
            schedule_offset=123,
            schedule_timezone="scheduleTimezone",
            start_date="startDate",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allow_unassociated_targets: typing.Union[builtins.bool, _IResolvable_da3f097b],
        cutoff: jsii.Number,
        duration: jsii.Number,
        name: builtins.str,
        schedule: builtins.str,
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::MaintenanceWindow``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param allow_unassociated_targets: Enables a maintenance window task to run on managed instances, even if you have not registered those instances as targets. If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the maintenance window.
        :param cutoff: The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.
        :param duration: The duration of the maintenance window in hours.
        :param name: The name of the maintenance window.
        :param schedule: The schedule of the maintenance window in the form of a cron or rate expression.
        :param description: A description of the maintenance window.
        :param end_date: The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.
        :param schedule_offset: The number of days to wait to run a maintenance window after the scheduled cron expression date and time.
        :param schedule_timezone: The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.
        :param start_date: The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. StartDate allows you to delay activation of the Maintenance Window until the specified future date.
        :param tags: Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in.
        '''
        props = CfnMaintenanceWindowProps(
            allow_unassociated_targets=allow_unassociated_targets,
            cutoff=cutoff,
            duration=duration,
            name=name,
            schedule=schedule,
            description=description,
            end_date=end_date,
            schedule_offset=schedule_offset,
            schedule_timezone=schedule_timezone,
            start_date=start_date,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs).

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowUnassociatedTargets")
    def allow_unassociated_targets(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Enables a maintenance window task to run on managed instances, even if you have not registered those instances as targets.

        If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-allowunassociatedtargets
        '''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "allowUnassociatedTargets"))

    @allow_unassociated_targets.setter
    def allow_unassociated_targets(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "allowUnassociatedTargets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cutoff")
    def cutoff(self) -> jsii.Number:
        '''The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-cutoff
        '''
        return typing.cast(jsii.Number, jsii.get(self, "cutoff"))

    @cutoff.setter
    def cutoff(self, value: jsii.Number) -> None:
        jsii.set(self, "cutoff", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        '''The duration of the maintenance window in hours.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-duration
        '''
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        jsii.set(self, "duration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        '''The schedule of the maintenance window in the form of a cron or rate expression.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-schedule
        '''
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        jsii.set(self, "schedule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> typing.Optional[builtins.str]:
        '''The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-enddate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endDate"))

    @end_date.setter
    def end_date(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endDate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scheduleOffset")
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''The number of days to wait to run a maintenance window after the scheduled cron expression date and time.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduleoffset
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scheduleOffset"))

    @schedule_offset.setter
    def schedule_offset(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "scheduleOffset", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scheduleTimezone")
    def schedule_timezone(self) -> typing.Optional[builtins.str]:
        '''The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduletimezone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleTimezone"))

    @schedule_timezone.setter
    def schedule_timezone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "scheduleTimezone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> typing.Optional[builtins.str]:
        '''The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active.

        StartDate allows you to delay activation of the Maintenance Window until the specified future date.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-startdate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startDate"))

    @start_date.setter
    def start_date(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "startDate", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowProps",
    jsii_struct_bases=[],
    name_mapping={
        "allow_unassociated_targets": "allowUnassociatedTargets",
        "cutoff": "cutoff",
        "duration": "duration",
        "name": "name",
        "schedule": "schedule",
        "description": "description",
        "end_date": "endDate",
        "schedule_offset": "scheduleOffset",
        "schedule_timezone": "scheduleTimezone",
        "start_date": "startDate",
        "tags": "tags",
    },
)
class CfnMaintenanceWindowProps:
    def __init__(
        self,
        *,
        allow_unassociated_targets: typing.Union[builtins.bool, _IResolvable_da3f097b],
        cutoff: jsii.Number,
        duration: jsii.Number,
        name: builtins.str,
        schedule: builtins.str,
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMaintenanceWindow``.

        :param allow_unassociated_targets: Enables a maintenance window task to run on managed instances, even if you have not registered those instances as targets. If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the maintenance window.
        :param cutoff: The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.
        :param duration: The duration of the maintenance window in hours.
        :param name: The name of the maintenance window.
        :param schedule: The schedule of the maintenance window in the form of a cron or rate expression.
        :param description: A description of the maintenance window.
        :param end_date: The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.
        :param schedule_offset: The number of days to wait to run a maintenance window after the scheduled cron expression date and time.
        :param schedule_timezone: The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.
        :param start_date: The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. StartDate allows you to delay activation of the Maintenance Window until the specified future date.
        :param tags: Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            cfn_maintenance_window_props = ssm.CfnMaintenanceWindowProps(
                allow_unassociated_targets=False,
                cutoff=123,
                duration=123,
                name="name",
                schedule="schedule",
            
                # the properties below are optional
                description="description",
                end_date="endDate",
                schedule_offset=123,
                schedule_timezone="scheduleTimezone",
                start_date="startDate",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "allow_unassociated_targets": allow_unassociated_targets,
            "cutoff": cutoff,
            "duration": duration,
            "name": name,
            "schedule": schedule,
        }
        if description is not None:
            self._values["description"] = description
        if end_date is not None:
            self._values["end_date"] = end_date
        if schedule_offset is not None:
            self._values["schedule_offset"] = schedule_offset
        if schedule_timezone is not None:
            self._values["schedule_timezone"] = schedule_timezone
        if start_date is not None:
            self._values["start_date"] = start_date
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def allow_unassociated_targets(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Enables a maintenance window task to run on managed instances, even if you have not registered those instances as targets.

        If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-allowunassociatedtargets
        '''
        result = self._values.get("allow_unassociated_targets")
        assert result is not None, "Required property 'allow_unassociated_targets' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def cutoff(self) -> jsii.Number:
        '''The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-cutoff
        '''
        result = self._values.get("cutoff")
        assert result is not None, "Required property 'cutoff' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def duration(self) -> jsii.Number:
        '''The duration of the maintenance window in hours.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-duration
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(self) -> builtins.str:
        '''The schedule of the maintenance window in the form of a cron or rate expression.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-schedule
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_date(self) -> typing.Optional[builtins.str]:
        '''The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-enddate
        '''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''The number of days to wait to run a maintenance window after the scheduled cron expression date and time.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduleoffset
        '''
        result = self._values.get("schedule_offset")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def schedule_timezone(self) -> typing.Optional[builtins.str]:
        '''The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduletimezone
        '''
        result = self._values.get("schedule_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_date(self) -> typing.Optional[builtins.str]:
        '''The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active.

        StartDate allows you to delay activation of the Maintenance Window until the specified future date.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-startdate
        '''
        result = self._values.get("start_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs).

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaintenanceWindowTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTarget",
):
    '''A CloudFormation ``AWS::SSM::MaintenanceWindowTarget``.

    The ``AWS::SSM::MaintenanceWindowTarget`` resource registers a target with a maintenance window for AWS Systems Manager . For more information, see `RegisterTargetWithMaintenanceWindow <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterTargetWithMaintenanceWindow.html>`_ in the *AWS Systems Manager API Reference* .

    :cloudformationResource: AWS::SSM::MaintenanceWindowTarget
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        cfn_maintenance_window_target = ssm.CfnMaintenanceWindowTarget(self, "MyCfnMaintenanceWindowTarget",
            resource_type="resourceType",
            targets=[ssm.CfnMaintenanceWindowTarget.TargetsProperty(
                key="key",
                values=["values"]
            )],
            window_id="windowId",
        
            # the properties below are optional
            description="description",
            name="name",
            owner_information="ownerInformation"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        resource_type: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnMaintenanceWindowTarget.TargetsProperty", _IResolvable_da3f097b]]],
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_information: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::MaintenanceWindowTarget``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_type: The type of target that is being registered with the maintenance window.
        :param targets: The targets to register with the maintenance window. In other words, the instances to run commands on when the maintenance window runs. You must specify targets by using the ``WindowTargetIds`` parameter.
        :param window_id: The ID of the maintenance window to register the target with.
        :param description: A description for the target.
        :param name: The name for the maintenance window target.
        :param owner_information: A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.
        '''
        props = CfnMaintenanceWindowTargetProps(
            resource_type=resource_type,
            targets=targets,
            window_id=window_id,
            description=description,
            name=name,
            owner_information=owner_information,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The type of target that is being registered with the maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-resourcetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        jsii.set(self, "resourceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTarget.TargetsProperty", _IResolvable_da3f097b]]]:
        '''The targets to register with the maintenance window.

        In other words, the instances to run commands on when the maintenance window runs.

        You must specify targets by using the ``WindowTargetIds`` parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-targets
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTarget.TargetsProperty", _IResolvable_da3f097b]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTarget.TargetsProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "targets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> builtins.str:
        '''The ID of the maintenance window to register the target with.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-windowid
        '''
        return typing.cast(builtins.str, jsii.get(self, "windowId"))

    @window_id.setter
    def window_id(self, value: builtins.str) -> None:
        jsii.set(self, "windowId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the target.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the maintenance window target.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ownerInformation")
    def owner_information(self) -> typing.Optional[builtins.str]:
        '''A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-ownerinformation
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInformation"))

    @owner_information.setter
    def owner_information(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ownerInformation", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTarget.TargetsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TargetsProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''The ``Targets`` property type specifies adding a target to a maintenance window target in AWS Systems Manager .

            ``Targets`` is a property of the `AWS::SSM::MaintenanceWindowTarget <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html>`_ resource.

            :param key: User-defined criteria for sending commands that target managed nodes that meet the criteria.
            :param values: User-defined criteria that maps to ``Key`` . For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include EC2 tags of ``ServerRole,WebServer`` . Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                targets_property = ssm.CfnMaintenanceWindowTarget.TargetsProperty(
                    key="key",
                    values=["values"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''User-defined criteria for sending commands that target managed nodes that meet the criteria.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''User-defined criteria that maps to ``Key`` .

            For example, if you specified ``tag:ServerRole`` , you could specify ``value:WebServer`` to run a command on instances that include EC2 tags of ``ServerRole,WebServer`` .

            Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_type": "resourceType",
        "targets": "targets",
        "window_id": "windowId",
        "description": "description",
        "name": "name",
        "owner_information": "ownerInformation",
    },
)
class CfnMaintenanceWindowTargetProps:
    def __init__(
        self,
        *,
        resource_type: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnMaintenanceWindowTarget.TargetsProperty, _IResolvable_da3f097b]]],
        window_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_information: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMaintenanceWindowTarget``.

        :param resource_type: The type of target that is being registered with the maintenance window.
        :param targets: The targets to register with the maintenance window. In other words, the instances to run commands on when the maintenance window runs. You must specify targets by using the ``WindowTargetIds`` parameter.
        :param window_id: The ID of the maintenance window to register the target with.
        :param description: A description for the target.
        :param name: The name for the maintenance window target.
        :param owner_information: A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            cfn_maintenance_window_target_props = ssm.CfnMaintenanceWindowTargetProps(
                resource_type="resourceType",
                targets=[ssm.CfnMaintenanceWindowTarget.TargetsProperty(
                    key="key",
                    values=["values"]
                )],
                window_id="windowId",
            
                # the properties below are optional
                description="description",
                name="name",
                owner_information="ownerInformation"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_type": resource_type,
            "targets": targets,
            "window_id": window_id,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if owner_information is not None:
            self._values["owner_information"] = owner_information

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''The type of target that is being registered with the maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-resourcetype
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMaintenanceWindowTarget.TargetsProperty, _IResolvable_da3f097b]]]:
        '''The targets to register with the maintenance window.

        In other words, the instances to run commands on when the maintenance window runs.

        You must specify targets by using the ``WindowTargetIds`` parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-targets
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMaintenanceWindowTarget.TargetsProperty, _IResolvable_da3f097b]]], result)

    @builtins.property
    def window_id(self) -> builtins.str:
        '''The ID of the maintenance window to register the target with.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-windowid
        '''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the target.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the maintenance window target.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner_information(self) -> typing.Optional[builtins.str]:
        '''A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-ownerinformation
        '''
        result = self._values.get("owner_information")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMaintenanceWindowTask(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask",
):
    '''A CloudFormation ``AWS::SSM::MaintenanceWindowTask``.

    The ``AWS::SSM::MaintenanceWindowTask`` resource defines information about a task for an AWS Systems Manager maintenance window. For more information, see `RegisterTaskWithMaintenanceWindow <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterTaskWithMaintenanceWindow.html>`_ in the *AWS Systems Manager API Reference* .

    :cloudformationResource: AWS::SSM::MaintenanceWindowTask
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        # parameters: Any
        # task_parameters: Any
        
        cfn_maintenance_window_task = ssm.CfnMaintenanceWindowTask(self, "MyCfnMaintenanceWindowTask",
            priority=123,
            task_arn="taskArn",
            task_type="taskType",
            window_id="windowId",
        
            # the properties below are optional
            cutoff_behavior="cutoffBehavior",
            description="description",
            logging_info=ssm.CfnMaintenanceWindowTask.LoggingInfoProperty(
                region="region",
                s3_bucket="s3Bucket",
        
                # the properties below are optional
                s3_prefix="s3Prefix"
            ),
            max_concurrency="maxConcurrency",
            max_errors="maxErrors",
            name="name",
            service_role_arn="serviceRoleArn",
            targets=[ssm.CfnMaintenanceWindowTask.TargetProperty(
                key="key",
                values=["values"]
            )],
            task_invocation_parameters=ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty(
                maintenance_window_automation_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty(
                    document_version="documentVersion",
                    parameters=parameters
                ),
                maintenance_window_lambda_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty(
                    client_context="clientContext",
                    payload="payload",
                    qualifier="qualifier"
                ),
                maintenance_window_run_command_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty(
                    cloud_watch_output_config=ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                        cloud_watch_log_group_name="cloudWatchLogGroupName",
                        cloud_watch_output_enabled=False
                    ),
                    comment="comment",
                    document_hash="documentHash",
                    document_hash_type="documentHashType",
                    document_version="documentVersion",
                    notification_config=ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                        notification_arn="notificationArn",
        
                        # the properties below are optional
                        notification_events=["notificationEvents"],
                        notification_type="notificationType"
                    ),
                    output_s3_bucket_name="outputS3BucketName",
                    output_s3_key_prefix="outputS3KeyPrefix",
                    parameters=parameters,
                    service_role_arn="serviceRoleArn",
                    timeout_seconds=123
                ),
                maintenance_window_step_functions_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty(
                    input="input",
                    name="name"
                )
            ),
            task_parameters=task_parameters
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        priority: jsii.Number,
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        cutoff_behavior: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union["CfnMaintenanceWindowTask.LoggingInfoProperty", _IResolvable_da3f097b]] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnMaintenanceWindowTask.TargetProperty", _IResolvable_da3f097b]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.TaskInvocationParametersProperty", _IResolvable_da3f097b]] = None,
        task_parameters: typing.Any = None,
    ) -> None:
        '''Create a new ``AWS::SSM::MaintenanceWindowTask``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param priority: The priority of the task in the maintenance window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
        :param task_arn: The resource that the task uses during execution. For ``RUN_COMMAND`` and ``AUTOMATION`` task types, ``TaskArn`` is the SSM document name or Amazon Resource Name (ARN). For ``LAMBDA`` tasks, ``TaskArn`` is the function name or ARN. For ``STEP_FUNCTIONS`` tasks, ``TaskArn`` is the state machine ARN.
        :param task_type: The type of task. Valid values: ``RUN_COMMAND`` , ``AUTOMATION`` , ``LAMBDA`` , ``STEP_FUNCTIONS`` .
        :param window_id: The ID of the maintenance window where the task is registered.
        :param cutoff_behavior: The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.
        :param description: A description of the task.
        :param logging_info: Information about an Amazon S3 bucket to write task-level logs to. .. epigraph:: ``LoggingInfo`` has been deprecated. To specify an Amazon S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `AWS Systems Manager MaintenanceWindowTask TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ .
        :param max_concurrency: The maximum number of targets this task can be run for, in parallel. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases. For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.
        :param max_errors: The maximum number of errors allowed before this task stops being scheduled. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases. For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.
        :param name: The task name.
        :param service_role_arn: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.
        :param targets: The targets, either instances or window target IDs. - Specify instances using ``Key=InstanceIds,Values= *instanceid1* , *instanceid2*`` . - Specify window target IDs using ``Key=WindowTargetIds,Values= *window-target-id-1* , *window-target-id-2*`` .
        :param task_invocation_parameters: The parameters to pass to the task when it runs. Populate only the fields that match the task type. All other fields should be empty. .. epigraph:: When you update a maintenance window task that has options specified in ``TaskInvocationParameters`` , you must provide again all the ``TaskInvocationParameters`` values that you want to retain. The values you do not specify again are removed. For example, suppose that when you registered a Run Command task, you specified ``TaskInvocationParameters`` values for ``Comment`` , ``NotificationConfig`` , and ``OutputS3BucketName`` . If you update the maintenance window task and specify only a different ``OutputS3BucketName`` value, the values for ``Comment`` and ``NotificationConfig`` are removed.
        :param task_parameters: The parameters to pass to the task when it runs. .. epigraph:: ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `MaintenanceWindowTaskInvocationParameters <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTaskInvocationParameters.html>`_ .
        '''
        props = CfnMaintenanceWindowTaskProps(
            priority=priority,
            task_arn=task_arn,
            task_type=task_type,
            window_id=window_id,
            cutoff_behavior=cutoff_behavior,
            description=description,
            logging_info=logging_info,
            max_concurrency=max_concurrency,
            max_errors=max_errors,
            name=name,
            service_role_arn=service_role_arn,
            targets=targets,
            task_invocation_parameters=task_invocation_parameters,
            task_parameters=task_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        '''The priority of the task in the maintenance window.

        The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-priority
        '''
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        jsii.set(self, "priority", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taskArn")
    def task_arn(self) -> builtins.str:
        '''The resource that the task uses during execution.

        For ``RUN_COMMAND`` and ``AUTOMATION`` task types, ``TaskArn`` is the SSM document name or Amazon Resource Name (ARN).

        For ``LAMBDA`` tasks, ``TaskArn`` is the function name or ARN.

        For ``STEP_FUNCTIONS`` tasks, ``TaskArn`` is the state machine ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "taskArn"))

    @task_arn.setter
    def task_arn(self, value: builtins.str) -> None:
        jsii.set(self, "taskArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taskParameters")
    def task_parameters(self) -> typing.Any:
        '''The parameters to pass to the task when it runs.

        .. epigraph::

           ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `MaintenanceWindowTaskInvocationParameters <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTaskInvocationParameters.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskparameters
        '''
        return typing.cast(typing.Any, jsii.get(self, "taskParameters"))

    @task_parameters.setter
    def task_parameters(self, value: typing.Any) -> None:
        jsii.set(self, "taskParameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        '''The type of task.

        Valid values: ``RUN_COMMAND`` , ``AUTOMATION`` , ``LAMBDA`` , ``STEP_FUNCTIONS`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-tasktype
        '''
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        jsii.set(self, "taskType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> builtins.str:
        '''The ID of the maintenance window where the task is registered.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-windowid
        '''
        return typing.cast(builtins.str, jsii.get(self, "windowId"))

    @window_id.setter
    def window_id(self, value: builtins.str) -> None:
        jsii.set(self, "windowId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cutoffBehavior")
    def cutoff_behavior(self) -> typing.Optional[builtins.str]:
        '''The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-cutoffbehavior
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cutoffBehavior"))

    @cutoff_behavior.setter
    def cutoff_behavior(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cutoffBehavior", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingInfo")
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.LoggingInfoProperty", _IResolvable_da3f097b]]:
        '''Information about an Amazon S3 bucket to write task-level logs to.

        .. epigraph::

           ``LoggingInfo`` has been deprecated. To specify an Amazon S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `AWS Systems Manager MaintenanceWindowTask TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-logginginfo
        '''
        return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.LoggingInfoProperty", _IResolvable_da3f097b]], jsii.get(self, "loggingInfo"))

    @logging_info.setter
    def logging_info(
        self,
        value: typing.Optional[typing.Union["CfnMaintenanceWindowTask.LoggingInfoProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "loggingInfo", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''The maximum number of targets this task can be run for, in parallel.

        .. epigraph::

           Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases.

           For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxconcurrency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "maxConcurrency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''The maximum number of errors allowed before this task stops being scheduled.

        .. epigraph::

           Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases.

           For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxerrors
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxErrors"))

    @max_errors.setter
    def max_errors(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "maxErrors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The task name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-servicerolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTask.TargetProperty", _IResolvable_da3f097b]]]]:
        '''The targets, either instances or window target IDs.

        - Specify instances using ``Key=InstanceIds,Values= *instanceid1* , *instanceid2*`` .
        - Specify window target IDs using ``Key=WindowTargetIds,Values= *window-target-id-1* , *window-target-id-2*`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-targets
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTask.TargetProperty", _IResolvable_da3f097b]]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnMaintenanceWindowTask.TargetProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "targets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taskInvocationParameters")
    def task_invocation_parameters(
        self,
    ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.TaskInvocationParametersProperty", _IResolvable_da3f097b]]:
        '''The parameters to pass to the task when it runs.

        Populate only the fields that match the task type. All other fields should be empty.
        .. epigraph::

           When you update a maintenance window task that has options specified in ``TaskInvocationParameters`` , you must provide again all the ``TaskInvocationParameters`` values that you want to retain. The values you do not specify again are removed. For example, suppose that when you registered a Run Command task, you specified ``TaskInvocationParameters`` values for ``Comment`` , ``NotificationConfig`` , and ``OutputS3BucketName`` . If you update the maintenance window task and specify only a different ``OutputS3BucketName`` value, the values for ``Comment`` and ``NotificationConfig`` are removed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters
        '''
        return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.TaskInvocationParametersProperty", _IResolvable_da3f097b]], jsii.get(self, "taskInvocationParameters"))

    @task_invocation_parameters.setter
    def task_invocation_parameters(
        self,
        value: typing.Optional[typing.Union["CfnMaintenanceWindowTask.TaskInvocationParametersProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "taskInvocationParameters", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_log_group_name": "cloudWatchLogGroupName",
            "cloud_watch_output_enabled": "cloudWatchOutputEnabled",
        },
    )
    class CloudWatchOutputConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_log_group_name: typing.Optional[builtins.str] = None,
            cloud_watch_output_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Configuration options for sending command output to Amazon CloudWatch Logs.

            :param cloud_watch_log_group_name: The name of the CloudWatch Logs log group where you want to send command output. If you don't specify a group name, AWS Systems Manager automatically creates a log group for you. The log group uses the following naming format: ``aws/ssm/ *SystemsManagerDocumentName*``
            :param cloud_watch_output_enabled: Enables Systems Manager to send command output to CloudWatch Logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                cloud_watch_output_config_property = ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                    cloud_watch_log_group_name="cloudWatchLogGroupName",
                    cloud_watch_output_enabled=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_watch_log_group_name is not None:
                self._values["cloud_watch_log_group_name"] = cloud_watch_log_group_name
            if cloud_watch_output_enabled is not None:
                self._values["cloud_watch_output_enabled"] = cloud_watch_output_enabled

        @builtins.property
        def cloud_watch_log_group_name(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudWatch Logs log group where you want to send command output.

            If you don't specify a group name, AWS Systems Manager automatically creates a log group for you. The log group uses the following naming format:

            ``aws/ssm/ *SystemsManagerDocumentName*``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchloggroupname
            '''
            result = self._values.get("cloud_watch_log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cloud_watch_output_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables Systems Manager to send command output to CloudWatch Logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchoutputenabled
            '''
            result = self._values.get("cloud_watch_output_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.LoggingInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region": "region",
            "s3_bucket": "s3Bucket",
            "s3_prefix": "s3Prefix",
        },
    )
    class LoggingInfoProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            s3_bucket: builtins.str,
            s3_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LoggingInfo`` property type specifies information about the Amazon S3 bucket to write instance-level logs to.

            ``LoggingInfo`` is a property of the `AWS::SSM::MaintenanceWindowTask <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html>`_ resource.
            .. epigraph::

               ``LoggingInfo`` has been deprecated. To specify an Amazon S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `AWS Systems Manager MaintenanceWindowTask TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ .

            :param region: The AWS Region where the S3 bucket is located.
            :param s3_bucket: The name of an S3 bucket where execution logs are stored .
            :param s3_prefix: The Amazon S3 bucket subfolder.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                logging_info_property = ssm.CfnMaintenanceWindowTask.LoggingInfoProperty(
                    region="region",
                    s3_bucket="s3Bucket",
                
                    # the properties below are optional
                    s3_prefix="s3Prefix"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "region": region,
                "s3_bucket": s3_bucket,
            }
            if s3_prefix is not None:
                self._values["s3_prefix"] = s3_prefix

        @builtins.property
        def region(self) -> builtins.str:
            '''The AWS Region where the S3 bucket is located.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The name of an S3 bucket where execution logs are stored .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_prefix(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 bucket subfolder.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3prefix
            '''
            result = self._values.get("s3_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_version": "documentVersion",
            "parameters": "parameters",
        },
    )
    class MaintenanceWindowAutomationParametersProperty:
        def __init__(
            self,
            *,
            document_version: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
        ) -> None:
            '''The ``MaintenanceWindowAutomationParameters`` property type specifies the parameters for an ``AUTOMATION`` task type for a maintenance window task in AWS Systems Manager .

            ``MaintenanceWindowAutomationParameters`` is a property of the `TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ property type.

            For information about available parameters in Automation runbooks, you can view the content of the runbook itself in the Systems Manager console. For information, see `View runbook content <https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents-reference-details.html#view-automation-json>`_ in the *AWS Systems Manager User Guide* .

            :param document_version: The version of an Automation runbook to use during task execution.
            :param parameters: The parameters for the AUTOMATION task.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                # parameters: Any
                
                maintenance_window_automation_parameters_property = ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty(
                    document_version="documentVersion",
                    parameters=parameters
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if document_version is not None:
                self._values["document_version"] = document_version
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def document_version(self) -> typing.Optional[builtins.str]:
            '''The version of an Automation runbook to use during task execution.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-documentversion
            '''
            result = self._values.get("document_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''The parameters for the AUTOMATION task.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowAutomationParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_context": "clientContext",
            "payload": "payload",
            "qualifier": "qualifier",
        },
    )
    class MaintenanceWindowLambdaParametersProperty:
        def __init__(
            self,
            *,
            client_context: typing.Optional[builtins.str] = None,
            payload: typing.Optional[builtins.str] = None,
            qualifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``MaintenanceWindowLambdaParameters`` property type specifies the parameters for a ``LAMBDA`` task type for a maintenance window task in AWS Systems Manager .

            ``MaintenanceWindowLambdaParameters`` is a property of the `TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ property type.

            :param client_context: Client-specific information to pass to the AWS Lambda function that you're invoking. You can then use the ``context`` variable to process the client information in your AWS Lambda function.
            :param payload: JSON to provide to your AWS Lambda function as input. .. epigraph:: Although ``Type`` is listed as "String" for this property, the payload content must be formatted as a Base64-encoded binary data object. *Length Constraint:* 4096
            :param qualifier: An AWS Lambda function version or alias name. If you specify a function version, the action uses the qualified function Amazon Resource Name (ARN) to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version that the alias points to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                maintenance_window_lambda_parameters_property = ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty(
                    client_context="clientContext",
                    payload="payload",
                    qualifier="qualifier"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if client_context is not None:
                self._values["client_context"] = client_context
            if payload is not None:
                self._values["payload"] = payload
            if qualifier is not None:
                self._values["qualifier"] = qualifier

        @builtins.property
        def client_context(self) -> typing.Optional[builtins.str]:
            '''Client-specific information to pass to the AWS Lambda function that you're invoking.

            You can then use the ``context`` variable to process the client information in your AWS Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-clientcontext
            '''
            result = self._values.get("client_context")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload(self) -> typing.Optional[builtins.str]:
            '''JSON to provide to your AWS Lambda function as input.

            .. epigraph::

               Although ``Type`` is listed as "String" for this property, the payload content must be formatted as a Base64-encoded binary data object.

            *Length Constraint:* 4096

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def qualifier(self) -> typing.Optional[builtins.str]:
            '''An AWS Lambda function version or alias name.

            If you specify a function version, the action uses the qualified function Amazon Resource Name (ARN) to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version that the alias points to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-qualifier
            '''
            result = self._values.get("qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowLambdaParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_output_config": "cloudWatchOutputConfig",
            "comment": "comment",
            "document_hash": "documentHash",
            "document_hash_type": "documentHashType",
            "document_version": "documentVersion",
            "notification_config": "notificationConfig",
            "output_s3_bucket_name": "outputS3BucketName",
            "output_s3_key_prefix": "outputS3KeyPrefix",
            "parameters": "parameters",
            "service_role_arn": "serviceRoleArn",
            "timeout_seconds": "timeoutSeconds",
        },
    )
    class MaintenanceWindowRunCommandParametersProperty:
        def __init__(
            self,
            *,
            cloud_watch_output_config: typing.Optional[typing.Union["CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty", _IResolvable_da3f097b]] = None,
            comment: typing.Optional[builtins.str] = None,
            document_hash: typing.Optional[builtins.str] = None,
            document_hash_type: typing.Optional[builtins.str] = None,
            document_version: typing.Optional[builtins.str] = None,
            notification_config: typing.Optional[typing.Union["CfnMaintenanceWindowTask.NotificationConfigProperty", _IResolvable_da3f097b]] = None,
            output_s3_bucket_name: typing.Optional[builtins.str] = None,
            output_s3_key_prefix: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
            service_role_arn: typing.Optional[builtins.str] = None,
            timeout_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``MaintenanceWindowRunCommandParameters`` property type specifies the parameters for a ``RUN_COMMAND`` task type for a maintenance window task in AWS Systems Manager .

            This means that these parameters are the same as those for the ``SendCommand`` API call. For more information about ``SendCommand`` parameters, see `SendCommand <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html>`_ in the *AWS Systems Manager API Reference* .

            For information about available parameters in SSM Command documents, you can view the content of the document itself in the Systems Manager console. For information, see `Viewing SSM command document content <https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-ssm-document-content.html>`_ in the *AWS Systems Manager User Guide* .

            ``MaintenanceWindowRunCommandParameters`` is a property of the `TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ property type.

            :param cloud_watch_output_config: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.CloudWatchOutputConfig``.
            :param comment: Information about the command or commands to run.
            :param document_hash: The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
            :param document_hash_type: The SHA-256 or SHA-1 hash type. SHA-1 hashes are deprecated.
            :param document_version: The AWS Systems Manager document (SSM document) version to use in the request. You can specify ``$DEFAULT`` , ``$LATEST`` , or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don't need to use the backslash. For example: ``--document-version "\\$DEFAULT"`` ``--document-version "\\$LATEST"`` ``--document-version "3"``
            :param notification_config: Configurations for sending notifications about command status changes on a per-managed node basis.
            :param output_s3_bucket_name: The name of the Amazon Simple Storage Service (Amazon S3) bucket.
            :param output_s3_key_prefix: The S3 bucket subfolder.
            :param parameters: The parameters for the ``RUN_COMMAND`` task execution. The supported parameters are the same as those for the ``SendCommand`` API call. For more information, see `SendCommand <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html>`_ in the *AWS Systems Manager API Reference* .
            :param service_role_arn: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.
            :param timeout_seconds: If this time is reached and the command hasn't already started running, it doesn't run.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                # parameters: Any
                
                maintenance_window_run_command_parameters_property = ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty(
                    cloud_watch_output_config=ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                        cloud_watch_log_group_name="cloudWatchLogGroupName",
                        cloud_watch_output_enabled=False
                    ),
                    comment="comment",
                    document_hash="documentHash",
                    document_hash_type="documentHashType",
                    document_version="documentVersion",
                    notification_config=ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                        notification_arn="notificationArn",
                
                        # the properties below are optional
                        notification_events=["notificationEvents"],
                        notification_type="notificationType"
                    ),
                    output_s3_bucket_name="outputS3BucketName",
                    output_s3_key_prefix="outputS3KeyPrefix",
                    parameters=parameters,
                    service_role_arn="serviceRoleArn",
                    timeout_seconds=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_watch_output_config is not None:
                self._values["cloud_watch_output_config"] = cloud_watch_output_config
            if comment is not None:
                self._values["comment"] = comment
            if document_hash is not None:
                self._values["document_hash"] = document_hash
            if document_hash_type is not None:
                self._values["document_hash_type"] = document_hash_type
            if document_version is not None:
                self._values["document_version"] = document_version
            if notification_config is not None:
                self._values["notification_config"] = notification_config
            if output_s3_bucket_name is not None:
                self._values["output_s3_bucket_name"] = output_s3_bucket_name
            if output_s3_key_prefix is not None:
                self._values["output_s3_key_prefix"] = output_s3_key_prefix
            if parameters is not None:
                self._values["parameters"] = parameters
            if service_role_arn is not None:
                self._values["service_role_arn"] = service_role_arn
            if timeout_seconds is not None:
                self._values["timeout_seconds"] = timeout_seconds

        @builtins.property
        def cloud_watch_output_config(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty", _IResolvable_da3f097b]]:
            '''``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.CloudWatchOutputConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-cloudwatchoutputconfig
            '''
            result = self._values.get("cloud_watch_output_config")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            '''Information about the command or commands to run.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-comment
            '''
            result = self._values.get("comment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_hash(self) -> typing.Optional[builtins.str]:
            '''The SHA-256 or SHA-1 hash created by the system when the document was created.

            SHA-1 hashes have been deprecated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthash
            '''
            result = self._values.get("document_hash")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_hash_type(self) -> typing.Optional[builtins.str]:
            '''The SHA-256 or SHA-1 hash type.

            SHA-1 hashes are deprecated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthashtype
            '''
            result = self._values.get("document_hash_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_version(self) -> typing.Optional[builtins.str]:
            '''The AWS Systems Manager document (SSM document) version to use in the request.

            You can specify ``$DEFAULT`` , ``$LATEST`` , or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don't need to use the backslash. For example:

            ``--document-version "\\$DEFAULT"``

            ``--document-version "\\$LATEST"``

            ``--document-version "3"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documentversion
            '''
            result = self._values.get("document_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def notification_config(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.NotificationConfigProperty", _IResolvable_da3f097b]]:
            '''Configurations for sending notifications about command status changes on a per-managed node basis.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-notificationconfig
            '''
            result = self._values.get("notification_config")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.NotificationConfigProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def output_s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the Amazon Simple Storage Service (Amazon S3) bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3bucketname
            '''
            result = self._values.get("output_s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 bucket subfolder.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3keyprefix
            '''
            result = self._values.get("output_s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''The parameters for the ``RUN_COMMAND`` task execution.

            The supported parameters are the same as those for the ``SendCommand`` API call. For more information, see `SendCommand <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html>`_ in the *AWS Systems Manager API Reference* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def service_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-servicerolearn
            '''
            result = self._values.get("service_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout_seconds(self) -> typing.Optional[jsii.Number]:
            '''If this time is reached and the command hasn't already started running, it doesn't run.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-timeoutseconds
            '''
            result = self._values.get("timeout_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowRunCommandParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"input": "input", "name": "name"},
    )
    class MaintenanceWindowStepFunctionsParametersProperty:
        def __init__(
            self,
            *,
            input: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``MaintenanceWindowStepFunctionsParameters`` property type specifies the parameters for the execution of a ``STEP_FUNCTIONS`` task in a Systems Manager maintenance window.

            ``MaintenanceWindowStepFunctionsParameters`` is a property of the `TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ property type.

            :param input: The inputs for the ``STEP_FUNCTIONS`` task.
            :param name: The name of the ``STEP_FUNCTIONS`` task.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                maintenance_window_step_functions_parameters_property = ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty(
                    input="input",
                    name="name"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if input is not None:
                self._values["input"] = input
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''The inputs for the ``STEP_FUNCTIONS`` task.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the ``STEP_FUNCTIONS`` task.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowStepFunctionsParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.NotificationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "notification_arn": "notificationArn",
            "notification_events": "notificationEvents",
            "notification_type": "notificationType",
        },
    )
    class NotificationConfigProperty:
        def __init__(
            self,
            *,
            notification_arn: builtins.str,
            notification_events: typing.Optional[typing.Sequence[builtins.str]] = None,
            notification_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``NotificationConfig`` property type specifies configurations for sending notifications for a maintenance window task in AWS Systems Manager .

            ``NotificationConfig`` is a property of the `MaintenanceWindowRunCommandParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html>`_ property type.

            :param notification_arn: An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.
            :param notification_events: The different events that you can receive notifications for. These events include the following: ``All`` (events), ``InProgress`` , ``Success`` , ``TimedOut`` , ``Cancelled`` , ``Failed`` . To learn more about these events, see `Configuring Amazon SNS Notifications for AWS Systems Manager <https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html>`_ in the *AWS Systems Manager User Guide* .
            :param notification_type: The notification type. - ``Command`` : Receive notification when the status of a command changes. - ``Invocation`` : For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                notification_config_property = ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                    notification_arn="notificationArn",
                
                    # the properties below are optional
                    notification_events=["notificationEvents"],
                    notification_type="notificationType"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "notification_arn": notification_arn,
            }
            if notification_events is not None:
                self._values["notification_events"] = notification_events
            if notification_type is not None:
                self._values["notification_type"] = notification_type

        @builtins.property
        def notification_arn(self) -> builtins.str:
            '''An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic.

            Run Command pushes notifications about command status changes to this topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationarn
            '''
            result = self._values.get("notification_arn")
            assert result is not None, "Required property 'notification_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def notification_events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The different events that you can receive notifications for.

            These events include the following: ``All`` (events), ``InProgress`` , ``Success`` , ``TimedOut`` , ``Cancelled`` , ``Failed`` . To learn more about these events, see `Configuring Amazon SNS Notifications for AWS Systems Manager <https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html>`_ in the *AWS Systems Manager User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationevents
            '''
            result = self._values.get("notification_events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def notification_type(self) -> typing.Optional[builtins.str]:
            '''The notification type.

            - ``Command`` : Receive notification when the status of a command changes.
            - ``Invocation`` : For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationtype
            '''
            result = self._values.get("notification_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''The ``Target`` property type specifies targets (either instances or window target IDs).

            You specify instances by using ``Key=InstanceIds,Values=< *instanceid1* >,< *instanceid2* >`` . You specify window target IDs using ``Key=WindowTargetIds,Values=< *window-target-id-1* >,< *window-target-id-2* >`` for a maintenance window task in AWS Systems Manager .

            ``Target`` is a property of the `AWS::SSM::MaintenanceWindowTask <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html>`_ property type.
            .. epigraph::

               To use ``resource-groups:Name`` as the key for a maintenance window target, specify the resource group as a ``AWS::SSM::MaintenanceWindowTarget`` type, and use the ``Ref`` function to specify the target for ``AWS::SSM::MaintenanceWindowTask`` . For an example, see *Create a Run Command task that targets instances using a resource group name* in `AWS::SSM::MaintenanceWindowTask Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#aws-resource-ssm-maintenancewindowtask--examples>`_ .

            :param key: User-defined criteria for sending commands that target instances that meet the criteria. ``Key`` can be ``InstanceIds`` or ``WindowTargetIds`` . For more information about how to target instances within a maintenance window task, see `About 'register-task-with-maintenance-window' Options and Values <https://docs.aws.amazon.com/systems-manager/latest/userguide/register-tasks-options.html>`_ in the *AWS Systems Manager User Guide* .
            :param values: User-defined criteria that maps to ``Key`` . For example, if you specify ``InstanceIds`` , you can specify ``i-1234567890abcdef0,i-9876543210abcdef0`` to run a command on two EC2 instances. For more information about how to target instances within a maintenance window task, see `About 'register-task-with-maintenance-window' Options and Values <https://docs.aws.amazon.com/systems-manager/latest/userguide/register-tasks-options.html>`_ in the *AWS Systems Manager User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                target_property = ssm.CfnMaintenanceWindowTask.TargetProperty(
                    key="key",
                    values=["values"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''User-defined criteria for sending commands that target instances that meet the criteria.

            ``Key`` can be ``InstanceIds`` or ``WindowTargetIds`` . For more information about how to target instances within a maintenance window task, see `About 'register-task-with-maintenance-window' Options and Values <https://docs.aws.amazon.com/systems-manager/latest/userguide/register-tasks-options.html>`_ in the *AWS Systems Manager User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''User-defined criteria that maps to ``Key`` .

            For example, if you specify ``InstanceIds`` , you can specify ``i-1234567890abcdef0,i-9876543210abcdef0`` to run a command on two EC2 instances. For more information about how to target instances within a maintenance window task, see `About 'register-task-with-maintenance-window' Options and Values <https://docs.aws.amazon.com/systems-manager/latest/userguide/register-tasks-options.html>`_ in the *AWS Systems Manager User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maintenance_window_automation_parameters": "maintenanceWindowAutomationParameters",
            "maintenance_window_lambda_parameters": "maintenanceWindowLambdaParameters",
            "maintenance_window_run_command_parameters": "maintenanceWindowRunCommandParameters",
            "maintenance_window_step_functions_parameters": "maintenanceWindowStepFunctionsParameters",
        },
    )
    class TaskInvocationParametersProperty:
        def __init__(
            self,
            *,
            maintenance_window_automation_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty", _IResolvable_da3f097b]] = None,
            maintenance_window_lambda_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty", _IResolvable_da3f097b]] = None,
            maintenance_window_run_command_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty", _IResolvable_da3f097b]] = None,
            maintenance_window_step_functions_parameters: typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``TaskInvocationParameters`` property type specifies the task execution parameters for a maintenance window task in AWS Systems Manager .

            ``TaskInvocationParameters`` is a property of the `AWS::SSM::MaintenanceWindowTask <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html>`_ property type.

            :param maintenance_window_automation_parameters: The parameters for an ``AUTOMATION`` task type.
            :param maintenance_window_lambda_parameters: The parameters for a ``LAMBDA`` task type.
            :param maintenance_window_run_command_parameters: The parameters for a ``RUN_COMMAND`` task type.
            :param maintenance_window_step_functions_parameters: The parameters for a ``STEP_FUNCTIONS`` task type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                # parameters: Any
                
                task_invocation_parameters_property = ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty(
                    maintenance_window_automation_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty(
                        document_version="documentVersion",
                        parameters=parameters
                    ),
                    maintenance_window_lambda_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty(
                        client_context="clientContext",
                        payload="payload",
                        qualifier="qualifier"
                    ),
                    maintenance_window_run_command_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty(
                        cloud_watch_output_config=ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                            cloud_watch_log_group_name="cloudWatchLogGroupName",
                            cloud_watch_output_enabled=False
                        ),
                        comment="comment",
                        document_hash="documentHash",
                        document_hash_type="documentHashType",
                        document_version="documentVersion",
                        notification_config=ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                            notification_arn="notificationArn",
                
                            # the properties below are optional
                            notification_events=["notificationEvents"],
                            notification_type="notificationType"
                        ),
                        output_s3_bucket_name="outputS3BucketName",
                        output_s3_key_prefix="outputS3KeyPrefix",
                        parameters=parameters,
                        service_role_arn="serviceRoleArn",
                        timeout_seconds=123
                    ),
                    maintenance_window_step_functions_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty(
                        input="input",
                        name="name"
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if maintenance_window_automation_parameters is not None:
                self._values["maintenance_window_automation_parameters"] = maintenance_window_automation_parameters
            if maintenance_window_lambda_parameters is not None:
                self._values["maintenance_window_lambda_parameters"] = maintenance_window_lambda_parameters
            if maintenance_window_run_command_parameters is not None:
                self._values["maintenance_window_run_command_parameters"] = maintenance_window_run_command_parameters
            if maintenance_window_step_functions_parameters is not None:
                self._values["maintenance_window_step_functions_parameters"] = maintenance_window_step_functions_parameters

        @builtins.property
        def maintenance_window_automation_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty", _IResolvable_da3f097b]]:
            '''The parameters for an ``AUTOMATION`` task type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowautomationparameters
            '''
            result = self._values.get("maintenance_window_automation_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def maintenance_window_lambda_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty", _IResolvable_da3f097b]]:
            '''The parameters for a ``LAMBDA`` task type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowlambdaparameters
            '''
            result = self._values.get("maintenance_window_lambda_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def maintenance_window_run_command_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty", _IResolvable_da3f097b]]:
            '''The parameters for a ``RUN_COMMAND`` task type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowruncommandparameters
            '''
            result = self._values.get("maintenance_window_run_command_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def maintenance_window_step_functions_parameters(
            self,
        ) -> typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty", _IResolvable_da3f097b]]:
            '''The parameters for a ``STEP_FUNCTIONS`` task type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowstepfunctionsparameters
            '''
            result = self._values.get("maintenance_window_step_functions_parameters")
            return typing.cast(typing.Optional[typing.Union["CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskInvocationParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnMaintenanceWindowTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "priority": "priority",
        "task_arn": "taskArn",
        "task_type": "taskType",
        "window_id": "windowId",
        "cutoff_behavior": "cutoffBehavior",
        "description": "description",
        "logging_info": "loggingInfo",
        "max_concurrency": "maxConcurrency",
        "max_errors": "maxErrors",
        "name": "name",
        "service_role_arn": "serviceRoleArn",
        "targets": "targets",
        "task_invocation_parameters": "taskInvocationParameters",
        "task_parameters": "taskParameters",
    },
)
class CfnMaintenanceWindowTaskProps:
    def __init__(
        self,
        *,
        priority: jsii.Number,
        task_arn: builtins.str,
        task_type: builtins.str,
        window_id: builtins.str,
        cutoff_behavior: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union[CfnMaintenanceWindowTask.LoggingInfoProperty, _IResolvable_da3f097b]] = None,
        max_concurrency: typing.Optional[builtins.str] = None,
        max_errors: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnMaintenanceWindowTask.TargetProperty, _IResolvable_da3f097b]]]] = None,
        task_invocation_parameters: typing.Optional[typing.Union[CfnMaintenanceWindowTask.TaskInvocationParametersProperty, _IResolvable_da3f097b]] = None,
        task_parameters: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnMaintenanceWindowTask``.

        :param priority: The priority of the task in the maintenance window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
        :param task_arn: The resource that the task uses during execution. For ``RUN_COMMAND`` and ``AUTOMATION`` task types, ``TaskArn`` is the SSM document name or Amazon Resource Name (ARN). For ``LAMBDA`` tasks, ``TaskArn`` is the function name or ARN. For ``STEP_FUNCTIONS`` tasks, ``TaskArn`` is the state machine ARN.
        :param task_type: The type of task. Valid values: ``RUN_COMMAND`` , ``AUTOMATION`` , ``LAMBDA`` , ``STEP_FUNCTIONS`` .
        :param window_id: The ID of the maintenance window where the task is registered.
        :param cutoff_behavior: The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.
        :param description: A description of the task.
        :param logging_info: Information about an Amazon S3 bucket to write task-level logs to. .. epigraph:: ``LoggingInfo`` has been deprecated. To specify an Amazon S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `AWS Systems Manager MaintenanceWindowTask TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ .
        :param max_concurrency: The maximum number of targets this task can be run for, in parallel. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases. For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.
        :param max_errors: The maximum number of errors allowed before this task stops being scheduled. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases. For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.
        :param name: The task name.
        :param service_role_arn: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.
        :param targets: The targets, either instances or window target IDs. - Specify instances using ``Key=InstanceIds,Values= *instanceid1* , *instanceid2*`` . - Specify window target IDs using ``Key=WindowTargetIds,Values= *window-target-id-1* , *window-target-id-2*`` .
        :param task_invocation_parameters: The parameters to pass to the task when it runs. Populate only the fields that match the task type. All other fields should be empty. .. epigraph:: When you update a maintenance window task that has options specified in ``TaskInvocationParameters`` , you must provide again all the ``TaskInvocationParameters`` values that you want to retain. The values you do not specify again are removed. For example, suppose that when you registered a Run Command task, you specified ``TaskInvocationParameters`` values for ``Comment`` , ``NotificationConfig`` , and ``OutputS3BucketName`` . If you update the maintenance window task and specify only a different ``OutputS3BucketName`` value, the values for ``Comment`` and ``NotificationConfig`` are removed.
        :param task_parameters: The parameters to pass to the task when it runs. .. epigraph:: ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `MaintenanceWindowTaskInvocationParameters <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTaskInvocationParameters.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            # parameters: Any
            # task_parameters: Any
            
            cfn_maintenance_window_task_props = ssm.CfnMaintenanceWindowTaskProps(
                priority=123,
                task_arn="taskArn",
                task_type="taskType",
                window_id="windowId",
            
                # the properties below are optional
                cutoff_behavior="cutoffBehavior",
                description="description",
                logging_info=ssm.CfnMaintenanceWindowTask.LoggingInfoProperty(
                    region="region",
                    s3_bucket="s3Bucket",
            
                    # the properties below are optional
                    s3_prefix="s3Prefix"
                ),
                max_concurrency="maxConcurrency",
                max_errors="maxErrors",
                name="name",
                service_role_arn="serviceRoleArn",
                targets=[ssm.CfnMaintenanceWindowTask.TargetProperty(
                    key="key",
                    values=["values"]
                )],
                task_invocation_parameters=ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty(
                    maintenance_window_automation_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty(
                        document_version="documentVersion",
                        parameters=parameters
                    ),
                    maintenance_window_lambda_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty(
                        client_context="clientContext",
                        payload="payload",
                        qualifier="qualifier"
                    ),
                    maintenance_window_run_command_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty(
                        cloud_watch_output_config=ssm.CfnMaintenanceWindowTask.CloudWatchOutputConfigProperty(
                            cloud_watch_log_group_name="cloudWatchLogGroupName",
                            cloud_watch_output_enabled=False
                        ),
                        comment="comment",
                        document_hash="documentHash",
                        document_hash_type="documentHashType",
                        document_version="documentVersion",
                        notification_config=ssm.CfnMaintenanceWindowTask.NotificationConfigProperty(
                            notification_arn="notificationArn",
            
                            # the properties below are optional
                            notification_events=["notificationEvents"],
                            notification_type="notificationType"
                        ),
                        output_s3_bucket_name="outputS3BucketName",
                        output_s3_key_prefix="outputS3KeyPrefix",
                        parameters=parameters,
                        service_role_arn="serviceRoleArn",
                        timeout_seconds=123
                    ),
                    maintenance_window_step_functions_parameters=ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty(
                        input="input",
                        name="name"
                    )
                ),
                task_parameters=task_parameters
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
            "task_arn": task_arn,
            "task_type": task_type,
            "window_id": window_id,
        }
        if cutoff_behavior is not None:
            self._values["cutoff_behavior"] = cutoff_behavior
        if description is not None:
            self._values["description"] = description
        if logging_info is not None:
            self._values["logging_info"] = logging_info
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_errors is not None:
            self._values["max_errors"] = max_errors
        if name is not None:
            self._values["name"] = name
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn
        if targets is not None:
            self._values["targets"] = targets
        if task_invocation_parameters is not None:
            self._values["task_invocation_parameters"] = task_invocation_parameters
        if task_parameters is not None:
            self._values["task_parameters"] = task_parameters

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The priority of the task in the maintenance window.

        The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-priority
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def task_arn(self) -> builtins.str:
        '''The resource that the task uses during execution.

        For ``RUN_COMMAND`` and ``AUTOMATION`` task types, ``TaskArn`` is the SSM document name or Amazon Resource Name (ARN).

        For ``LAMBDA`` tasks, ``TaskArn`` is the function name or ARN.

        For ``STEP_FUNCTIONS`` tasks, ``TaskArn`` is the state machine ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskarn
        '''
        result = self._values.get("task_arn")
        assert result is not None, "Required property 'task_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''The type of task.

        Valid values: ``RUN_COMMAND`` , ``AUTOMATION`` , ``LAMBDA`` , ``STEP_FUNCTIONS`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-tasktype
        '''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def window_id(self) -> builtins.str:
        '''The ID of the maintenance window where the task is registered.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-windowid
        '''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cutoff_behavior(self) -> typing.Optional[builtins.str]:
        '''The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-cutoffbehavior
        '''
        result = self._values.get("cutoff_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union[CfnMaintenanceWindowTask.LoggingInfoProperty, _IResolvable_da3f097b]]:
        '''Information about an Amazon S3 bucket to write task-level logs to.

        .. epigraph::

           ``LoggingInfo`` has been deprecated. To specify an Amazon S3 bucket to contain logs, instead use the ``OutputS3BucketName`` and ``OutputS3KeyPrefix`` options in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `AWS Systems Manager MaintenanceWindowTask TaskInvocationParameters <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-logginginfo
        '''
        result = self._values.get("logging_info")
        return typing.cast(typing.Optional[typing.Union[CfnMaintenanceWindowTask.LoggingInfoProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[builtins.str]:
        '''The maximum number of targets this task can be run for, in parallel.

        .. epigraph::

           Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases.

           For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxconcurrency
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_errors(self) -> typing.Optional[builtins.str]:
        '''The maximum number of errors allowed before this task stops being scheduled.

        .. epigraph::

           Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a `targetless task <https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html>`_ You must provide a value in all other cases.

           For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of ``1`` . This value doesn't affect the running of your task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxerrors
        '''
        result = self._values.get("max_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The task name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-servicerolearn
        '''
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMaintenanceWindowTask.TargetProperty, _IResolvable_da3f097b]]]]:
        '''The targets, either instances or window target IDs.

        - Specify instances using ``Key=InstanceIds,Values= *instanceid1* , *instanceid2*`` .
        - Specify window target IDs using ``Key=WindowTargetIds,Values= *window-target-id-1* , *window-target-id-2*`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-targets
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnMaintenanceWindowTask.TargetProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def task_invocation_parameters(
        self,
    ) -> typing.Optional[typing.Union[CfnMaintenanceWindowTask.TaskInvocationParametersProperty, _IResolvable_da3f097b]]:
        '''The parameters to pass to the task when it runs.

        Populate only the fields that match the task type. All other fields should be empty.
        .. epigraph::

           When you update a maintenance window task that has options specified in ``TaskInvocationParameters`` , you must provide again all the ``TaskInvocationParameters`` values that you want to retain. The values you do not specify again are removed. For example, suppose that when you registered a Run Command task, you specified ``TaskInvocationParameters`` values for ``Comment`` , ``NotificationConfig`` , and ``OutputS3BucketName`` . If you update the maintenance window task and specify only a different ``OutputS3BucketName`` value, the values for ``Comment`` and ``NotificationConfig`` are removed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters
        '''
        result = self._values.get("task_invocation_parameters")
        return typing.cast(typing.Optional[typing.Union[CfnMaintenanceWindowTask.TaskInvocationParametersProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def task_parameters(self) -> typing.Any:
        '''The parameters to pass to the task when it runs.

        .. epigraph::

           ``TaskParameters`` has been deprecated. To specify parameters to pass to a task when it runs, instead use the ``Parameters`` option in the ``TaskInvocationParameters`` structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see `MaintenanceWindowTaskInvocationParameters <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTaskInvocationParameters.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskparameters
        '''
        result = self._values.get("task_parameters")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMaintenanceWindowTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnParameter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnParameter",
):
    '''A CloudFormation ``AWS::SSM::Parameter``.

    The ``AWS::SSM::Parameter`` resource creates an SSM parameter in AWS Systems Manager Parameter Store.
    .. epigraph::

       To create an SSM parameter, you must have the AWS Identity and Access Management ( IAM ) permissions ``ssm:PutParameter`` and ``ssm:AddTagsToResource`` . On stack creation, AWS CloudFormation adds the following three tags to the parameter: ``aws:cloudformation:stack-name`` , ``aws:cloudformation:logical-id`` , and ``aws:cloudformation:stack-id`` , in addition to any custom tags you specify.

       To add, update, or remove tags during stack update, you must have IAM permissions for both ``ssm:AddTagsToResource`` and ``ssm:RemoveTagsFromResource`` . For more information, see `Managing Access Using Policies <https://docs.aws.amazon.com/systems-manager/latest/userguide/security-iam.html#security_iam_access-manage>`_ in the *AWS Systems Manager User Guide* .

    For information about valid values for parameters, see `Requirements and Constraints for Parameter Names <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html#sysman-parameter-name-constraints>`_ in the *AWS Systems Manager User Guide* and `PutParameter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html>`_ in the *AWS Systems Manager API Reference* .

    :cloudformationResource: AWS::SSM::Parameter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        # tags: Any
        
        cfn_parameter = ssm.CfnParameter(self, "MyCfnParameter",
            type="type",
            value="value",
        
            # the properties below are optional
            allowed_pattern="allowedPattern",
            data_type="dataType",
            description="description",
            name="name",
            policies="policies",
            tags=tags,
            tier="tier"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        value: builtins.str,
        allowed_pattern: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        policies: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::Parameter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param type: The type of parameter. .. epigraph:: AWS CloudFormation doesn't support creating a ``SecureString`` parameter type. *Allowed Values* : String | StringList
        :param value: The parameter value. .. epigraph:: If type is ``StringList`` , the system returns a comma-separated string with no spaces between commas in the ``Value`` field.
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``AllowedPattern=^\\d+$``
        :param data_type: The data type of the parameter, such as ``text`` or ``aws:ec2:image`` . The default is ``text`` .
        :param description: Information about the parameter.
        :param name: The name of the parameter. .. epigraph:: The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter ARN, is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter/ExampleParameterName``
        :param policies: Information about the policies assigned to a parameter. `Assigning parameter policies <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html>`_ in the *AWS Systems Manager User Guide* .
        :param tags: Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.
        :param tier: The parameter tier.
        '''
        props = CfnParameterProps(
            type=type,
            value=value,
            allowed_pattern=allowed_pattern,
            data_type=data_type,
            description=description,
            name=name,
            policies=policies,
            tags=tags,
            tier=tier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''Returns the type of the parameter.

        Valid values are ``String`` or ``StringList`` .

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrValue")
    def attr_value(self) -> builtins.str:
        '''Returns the value of the parameter.

        :cloudformationAttribute: Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs).

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of parameter.

        .. epigraph::

           AWS CloudFormation doesn't support creating a ``SecureString`` parameter type.

        *Allowed Values* : String | StringList

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''The parameter value.

        .. epigraph::

           If type is ``StringList`` , the system returns a comma-separated string with no spaces between commas in the ``Value`` field.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value
        '''
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        jsii.set(self, "value", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowedPattern")
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.

        For example, for String types with values restricted to numbers, you can specify the following: ``AllowedPattern=^\\d+$``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-allowedpattern
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedPattern"))

    @allowed_pattern.setter
    def allowed_pattern(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "allowedPattern", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The data type of the parameter, such as ``text`` or ``aws:ec2:image`` .

        The default is ``text`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-datatype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dataType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.

        .. epigraph::

           The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter ARN, is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter/ExampleParameterName``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.Optional[builtins.str]:
        '''Information about the policies assigned to a parameter.

        `Assigning parameter policies <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html>`_ in the *AWS Systems Manager User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-policies
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "policies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tier")
    def tier(self) -> typing.Optional[builtins.str]:
        '''The parameter tier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tier", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnParameterProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "value": "value",
        "allowed_pattern": "allowedPattern",
        "data_type": "dataType",
        "description": "description",
        "name": "name",
        "policies": "policies",
        "tags": "tags",
        "tier": "tier",
    },
)
class CfnParameterProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: builtins.str,
        allowed_pattern: typing.Optional[builtins.str] = None,
        data_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        policies: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnParameter``.

        :param type: The type of parameter. .. epigraph:: AWS CloudFormation doesn't support creating a ``SecureString`` parameter type. *Allowed Values* : String | StringList
        :param value: The parameter value. .. epigraph:: If type is ``StringList`` , the system returns a comma-separated string with no spaces between commas in the ``Value`` field.
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``AllowedPattern=^\\d+$``
        :param data_type: The data type of the parameter, such as ``text`` or ``aws:ec2:image`` . The default is ``text`` .
        :param description: Information about the parameter.
        :param name: The name of the parameter. .. epigraph:: The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter ARN, is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter/ExampleParameterName``
        :param policies: Information about the policies assigned to a parameter. `Assigning parameter policies <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html>`_ in the *AWS Systems Manager User Guide* .
        :param tags: Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.
        :param tier: The parameter tier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            # tags: Any
            
            cfn_parameter_props = ssm.CfnParameterProps(
                type="type",
                value="value",
            
                # the properties below are optional
                allowed_pattern="allowedPattern",
                data_type="dataType",
                description="description",
                name="name",
                policies="policies",
                tags=tags,
                tier="tier"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "value": value,
        }
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if data_type is not None:
            self._values["data_type"] = data_type
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if policies is not None:
            self._values["policies"] = policies
        if tags is not None:
            self._values["tags"] = tags
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of parameter.

        .. epigraph::

           AWS CloudFormation doesn't support creating a ``SecureString`` parameter type.

        *Allowed Values* : String | StringList

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The parameter value.

        .. epigraph::

           If type is ``StringList`` , the system returns a comma-separated string with no spaces between commas in the ``Value`` field.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.

        For example, for String types with values restricted to numbers, you can specify the following: ``AllowedPattern=^\\d+$``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-allowedpattern
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_type(self) -> typing.Optional[builtins.str]:
        '''The data type of the parameter, such as ``text`` or ``aws:ec2:image`` .

        The default is ``text`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-datatype
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.

        .. epigraph::

           The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter ARN, is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter/ExampleParameterName``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[builtins.str]:
        '''Information about the policies assigned to a parameter.

        `Assigning parameter policies <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html>`_ in the *AWS Systems Manager User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-policies
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs).

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''The parameter tier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tier
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPatchBaseline(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline",
):
    '''A CloudFormation ``AWS::SSM::PatchBaseline``.

    The ``AWS::SSM::PatchBaseline`` resource defines the basic information for an AWS Systems Manager patch baseline. A patch baseline defines which patches are approved for installation on your instances.

    For more information, see `CreatePatchBaseline <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html>`_ in the *AWS Systems Manager API Reference* .

    :cloudformationResource: AWS::SSM::PatchBaseline
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        cfn_patch_baseline = ssm.CfnPatchBaseline(self, "MyCfnPatchBaseline",
            name="name",
        
            # the properties below are optional
            approval_rules=ssm.CfnPatchBaseline.RuleGroupProperty(
                patch_rules=[ssm.CfnPatchBaseline.RuleProperty(
                    approve_after_days=123,
                    approve_until_date="approveUntilDate",
                    compliance_level="complianceLevel",
                    enable_non_security=False,
                    patch_filter_group=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                        patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                            key="key",
                            values=["values"]
                        )]
                    )
                )]
            ),
            approved_patches=["approvedPatches"],
            approved_patches_compliance_level="approvedPatchesComplianceLevel",
            approved_patches_enable_non_security=False,
            description="description",
            global_filters=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                    key="key",
                    values=["values"]
                )]
            ),
            operating_system="operatingSystem",
            patch_groups=["patchGroups"],
            rejected_patches=["rejectedPatches"],
            rejected_patches_action="rejectedPatchesAction",
            sources=[ssm.CfnPatchBaseline.PatchSourceProperty(
                configuration="configuration",
                name="name",
                products=["products"]
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        approval_rules: typing.Optional[typing.Union["CfnPatchBaseline.RuleGroupProperty", _IResolvable_da3f097b]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filters: typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]] = None,
        operating_system: typing.Optional[builtins.str] = None,
        patch_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnPatchBaseline.PatchSourceProperty", _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::PatchBaseline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the patch baseline.
        :param approval_rules: A set of rules used to include patches in the baseline.
        :param approved_patches: A list of explicitly approved patches for the baseline. For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .
        :param approved_patches_compliance_level: Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is ``UNSPECIFIED`` .
        :param approved_patches_enable_non_security: Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is ``false`` . Applies to Linux managed nodes only.
        :param description: A description of the patch baseline.
        :param global_filters: A set of global filters used to include patches in the baseline.
        :param operating_system: Defines the operating system the patch baseline applies to. The default value is ``WINDOWS`` .
        :param patch_groups: The name of the patch group to be registered with the patch baseline.
        :param rejected_patches: A list of explicitly rejected patches for the baseline. For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .
        :param rejected_patches_action: The action for Patch Manager to take on patches included in the ``RejectedPackages`` list. - *``ALLOW_AS_DEPENDENCY``* : A package in the ``Rejected`` patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as ``InstalledOther`` . This is the default action if no option is specified. - *``BLOCK``* : Packages in the ``RejectedPatches`` list, and packages that include them as dependencies, aren't installed under any circumstances. If a package was installed before it was added to the Rejected patches list, it is considered non-compliant with the patch baseline, and its status is reported as ``InstalledRejected`` .
        :param sources: Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
        :param tags: Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to.
        '''
        props = CfnPatchBaselineProps(
            name=name,
            approval_rules=approval_rules,
            approved_patches=approved_patches,
            approved_patches_compliance_level=approved_patches_compliance_level,
            approved_patches_enable_non_security=approved_patches_enable_non_security,
            description=description,
            global_filters=global_filters,
            operating_system=operating_system,
            patch_groups=patch_groups,
            rejected_patches=rejected_patches,
            rejected_patches_action=rejected_patches_action,
            sources=sources,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Optional metadata that you assign to a resource.

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the patch baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="approvalRules")
    def approval_rules(
        self,
    ) -> typing.Optional[typing.Union["CfnPatchBaseline.RuleGroupProperty", _IResolvable_da3f097b]]:
        '''A set of rules used to include patches in the baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvalrules
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPatchBaseline.RuleGroupProperty", _IResolvable_da3f097b]], jsii.get(self, "approvalRules"))

    @approval_rules.setter
    def approval_rules(
        self,
        value: typing.Optional[typing.Union["CfnPatchBaseline.RuleGroupProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "approvalRules", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="approvedPatches")
    def approved_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of explicitly approved patches for the baseline.

        For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatches
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "approvedPatches"))

    @approved_patches.setter
    def approved_patches(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "approvedPatches", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> typing.Optional[builtins.str]:
        '''Defines the compliance level for approved patches.

        When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is ``UNSPECIFIED`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchescompliancelevel
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approvedPatchesComplianceLevel"))

    @approved_patches_compliance_level.setter
    def approved_patches_compliance_level(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "approvedPatchesComplianceLevel", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes.

        The default value is ``false`` . Applies to Linux managed nodes only.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "approvedPatchesEnableNonSecurity"))

    @approved_patches_enable_non_security.setter
    def approved_patches_enable_non_security(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "approvedPatchesEnableNonSecurity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the patch baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalFilters")
    def global_filters(
        self,
    ) -> typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]]:
        '''A set of global filters used to include patches in the baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-globalfilters
        '''
        return typing.cast(typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]], jsii.get(self, "globalFilters"))

    @global_filters.setter
    def global_filters(
        self,
        value: typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "globalFilters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''Defines the operating system the patch baseline applies to.

        The default value is ``WINDOWS`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-operatingsystem
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "operatingSystem", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="patchGroups")
    def patch_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the patch group to be registered with the patch baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-patchgroups
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patchGroups"))

    @patch_groups.setter
    def patch_groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "patchGroups", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rejectedPatches")
    def rejected_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of explicitly rejected patches for the baseline.

        For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatches
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rejectedPatches"))

    @rejected_patches.setter
    def rejected_patches(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "rejectedPatches", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rejectedPatchesAction")
    def rejected_patches_action(self) -> typing.Optional[builtins.str]:
        '''The action for Patch Manager to take on patches included in the ``RejectedPackages`` list.

        - *``ALLOW_AS_DEPENDENCY``* : A package in the ``Rejected`` patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as ``InstalledOther`` . This is the default action if no option is specified.
        - *``BLOCK``* : Packages in the ``RejectedPatches`` list, and packages that include them as dependencies, aren't installed under any circumstances. If a package was installed before it was added to the Rejected patches list, it is considered non-compliant with the patch baseline, and its status is reported as ``InstalledRejected`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatchesaction
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rejectedPatchesAction"))

    @rejected_patches_action.setter
    def rejected_patches_action(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "rejectedPatchesAction", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchSourceProperty", _IResolvable_da3f097b]]]]:
        '''Information about the patches to use to update the managed nodes, including target operating systems and source repositories.

        Applies to Linux managed nodes only.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-sources
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchSourceProperty", _IResolvable_da3f097b]]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchSourceProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        jsii.set(self, "sources", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.PatchFilterGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"patch_filters": "patchFilters"},
    )
    class PatchFilterGroupProperty:
        def __init__(
            self,
            *,
            patch_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnPatchBaseline.PatchFilterProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The ``PatchFilterGroup`` property type specifies a set of patch filters for an AWS Systems Manager patch baseline, typically used for approval rules for a Systems Manager patch baseline.

            ``PatchFilterGroup`` is the property type for the ``GlobalFilters`` property of the `AWS::SSM::PatchBaseline <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html>`_ resource and the ``PatchFilterGroup`` property of the `Rule <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html>`_ property type.

            :param patch_filters: The set of patch filters that make up the group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                patch_filter_group_property = ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                    patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                        key="key",
                        values=["values"]
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if patch_filters is not None:
                self._values["patch_filters"] = patch_filters

        @builtins.property
        def patch_filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchFilterProperty", _IResolvable_da3f097b]]]]:
            '''The set of patch filters that make up the group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html#cfn-ssm-patchbaseline-patchfiltergroup-patchfilters
            '''
            result = self._values.get("patch_filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.PatchFilterProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PatchFilterGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.PatchFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class PatchFilterProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The ``PatchFilter`` property type defines a patch filter for an AWS Systems Manager patch baseline.

            The ``PatchFilters`` property of the `PatchFilterGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html>`_ property type contains a list of ``PatchFilter`` property types.

            You can view lists of valid values for the patch properties by running the ``DescribePatchProperties`` command. For more information, see `DescribePatchProperties <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchProperties.html>`_ in the *AWS Systems Manager API Reference* .

            :param key: The key for the filter. For information about valid keys, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .
            :param values: The value for the filter key. For information about valid values for each key based on operating system type, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                patch_filter_property = ssm.CfnPatchBaseline.PatchFilterProperty(
                    key="key",
                    values=["values"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key for the filter.

            For information about valid keys, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The value for the filter key.

            For information about valid values for each key based on operating system type, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PatchFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.PatchSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration": "configuration",
            "name": "name",
            "products": "products",
        },
    )
    class PatchSourceProperty:
        def __init__(
            self,
            *,
            configuration: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            products: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''``PatchSource`` is the property type for the ``Sources`` resource of the `AWS::SSM::PatchBaseline <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html>`_ resource.

            The AWS CloudFormation ``AWS::SSM::PatchSource`` resource is used to provide information about the patches to use to update target instances, including target operating systems and source repository. Applies to Linux instances only.

            :param configuration: The value of the yum repo configuration. For example:. ``[main]`` ``name=MyCustomRepository`` ``baseurl=https://my-custom-repository`` ``enabled=1`` .. epigraph:: For information about other options available for your yum repository configuration, see `dnf.conf(5) <https://docs.aws.amazon.com/https://man7.org/linux/man-pages/man5/dnf.conf.5.html>`_ .
            :param name: The name specified to identify the patch source.
            :param products: The specific operating system versions a patch repository applies to, such as "Ubuntu16.04", "AmazonLinux2016.09", "RedhatEnterpriseLinux7.2" or "Suse12.7". For lists of supported product values, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                patch_source_property = ssm.CfnPatchBaseline.PatchSourceProperty(
                    configuration="configuration",
                    name="name",
                    products=["products"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if configuration is not None:
                self._values["configuration"] = configuration
            if name is not None:
                self._values["name"] = name
            if products is not None:
                self._values["products"] = products

        @builtins.property
        def configuration(self) -> typing.Optional[builtins.str]:
            '''The value of the yum repo configuration. For example:.

            ``[main]``

            ``name=MyCustomRepository``

            ``baseurl=https://my-custom-repository``

            ``enabled=1``
            .. epigraph::

               For information about other options available for your yum repository configuration, see `dnf.conf(5) <https://docs.aws.amazon.com/https://man7.org/linux/man-pages/man5/dnf.conf.5.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-configuration
            '''
            result = self._values.get("configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name specified to identify the patch source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def products(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The specific operating system versions a patch repository applies to, such as "Ubuntu16.04", "AmazonLinux2016.09", "RedhatEnterpriseLinux7.2" or "Suse12.7". For lists of supported product values, see `PatchFilter <https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html>`_ in the *AWS Systems Manager API Reference* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-products
            '''
            result = self._values.get("products")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PatchSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.RuleGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"patch_rules": "patchRules"},
    )
    class RuleGroupProperty:
        def __init__(
            self,
            *,
            patch_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnPatchBaseline.RuleProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''The ``RuleGroup`` property type specifies a set of rules that define the approval rules for an AWS Systems Manager patch baseline.

            ``RuleGroup`` is the property type for the ``ApprovalRules`` property of the `AWS::SSM::PatchBaseline <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html>`_ resource.

            :param patch_rules: The rules that make up the rule group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                rule_group_property = ssm.CfnPatchBaseline.RuleGroupProperty(
                    patch_rules=[ssm.CfnPatchBaseline.RuleProperty(
                        approve_after_days=123,
                        approve_until_date="approveUntilDate",
                        compliance_level="complianceLevel",
                        enable_non_security=False,
                        patch_filter_group=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                            patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                                key="key",
                                values=["values"]
                            )]
                        )
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if patch_rules is not None:
                self._values["patch_rules"] = patch_rules

        @builtins.property
        def patch_rules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.RuleProperty", _IResolvable_da3f097b]]]]:
            '''The rules that make up the rule group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html#cfn-ssm-patchbaseline-rulegroup-patchrules
            '''
            result = self._values.get("patch_rules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnPatchBaseline.RuleProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaseline.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "approve_after_days": "approveAfterDays",
            "approve_until_date": "approveUntilDate",
            "compliance_level": "complianceLevel",
            "enable_non_security": "enableNonSecurity",
            "patch_filter_group": "patchFilterGroup",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            approve_after_days: typing.Optional[jsii.Number] = None,
            approve_until_date: typing.Optional[builtins.str] = None,
            compliance_level: typing.Optional[builtins.str] = None,
            enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            patch_filter_group: typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``Rule`` property type specifies an approval rule for a Systems Manager patch baseline.

            The ``PatchRules`` property of the `RuleGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html>`_ property type contains a list of ``Rule`` property types.

            :param approve_after_days: The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of ``7`` means that patches are approved seven days after they are released. You must specify a value for ``ApproveAfterDays`` . Exception: Not supported on Debian Server or Ubuntu Server.
            :param approve_until_date: The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically. Not supported on Debian Server or Ubuntu Server. Enter dates in the format ``YYYY-MM-DD`` . For example, ``2021-12-31`` .
            :param compliance_level: A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: ``UNSPECIFIED`` , ``CRITICAL`` , ``HIGH`` , ``MEDIUM`` , ``LOW`` , and ``INFORMATIONAL`` .
            :param enable_non_security: For managed nodes identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is ``false`` . Applies to Linux managed nodes only.
            :param patch_filter_group: The patch filter group that defines the criteria for the rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                rule_property = ssm.CfnPatchBaseline.RuleProperty(
                    approve_after_days=123,
                    approve_until_date="approveUntilDate",
                    compliance_level="complianceLevel",
                    enable_non_security=False,
                    patch_filter_group=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                        patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                            key="key",
                            values=["values"]
                        )]
                    )
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if approve_after_days is not None:
                self._values["approve_after_days"] = approve_after_days
            if approve_until_date is not None:
                self._values["approve_until_date"] = approve_until_date
            if compliance_level is not None:
                self._values["compliance_level"] = compliance_level
            if enable_non_security is not None:
                self._values["enable_non_security"] = enable_non_security
            if patch_filter_group is not None:
                self._values["patch_filter_group"] = patch_filter_group

        @builtins.property
        def approve_after_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline.

            For example, a value of ``7`` means that patches are approved seven days after they are released.

            You must specify a value for ``ApproveAfterDays`` .

            Exception: Not supported on Debian Server or Ubuntu Server.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-approveafterdays
            '''
            result = self._values.get("approve_after_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def approve_until_date(self) -> typing.Optional[builtins.str]:
            '''The cutoff date for auto approval of released patches.

            Any patches released on or before this date are installed automatically. Not supported on Debian Server or Ubuntu Server.

            Enter dates in the format ``YYYY-MM-DD`` . For example, ``2021-12-31`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-approveuntildate
            '''
            result = self._values.get("approve_until_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def compliance_level(self) -> typing.Optional[builtins.str]:
            '''A compliance severity level for all approved patches in a patch baseline.

            Valid compliance severity levels include the following: ``UNSPECIFIED`` , ``CRITICAL`` , ``HIGH`` , ``MEDIUM`` , ``LOW`` , and ``INFORMATIONAL`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-compliancelevel
            '''
            result = self._values.get("compliance_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_non_security(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''For managed nodes identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository.

            The default value is ``false`` . Applies to Linux managed nodes only.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-enablenonsecurity
            '''
            result = self._values.get("enable_non_security")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def patch_filter_group(
            self,
        ) -> typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]]:
            '''The patch filter group that defines the criteria for the rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-patchfiltergroup
            '''
            result = self._values.get("patch_filter_group")
            return typing.cast(typing.Optional[typing.Union["CfnPatchBaseline.PatchFilterGroupProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnPatchBaselineProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "approval_rules": "approvalRules",
        "approved_patches": "approvedPatches",
        "approved_patches_compliance_level": "approvedPatchesComplianceLevel",
        "approved_patches_enable_non_security": "approvedPatchesEnableNonSecurity",
        "description": "description",
        "global_filters": "globalFilters",
        "operating_system": "operatingSystem",
        "patch_groups": "patchGroups",
        "rejected_patches": "rejectedPatches",
        "rejected_patches_action": "rejectedPatchesAction",
        "sources": "sources",
        "tags": "tags",
    },
)
class CfnPatchBaselineProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        approval_rules: typing.Optional[typing.Union[CfnPatchBaseline.RuleGroupProperty, _IResolvable_da3f097b]] = None,
        approved_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        approved_patches_compliance_level: typing.Optional[builtins.str] = None,
        approved_patches_enable_non_security: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        global_filters: typing.Optional[typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, _IResolvable_da3f097b]] = None,
        operating_system: typing.Optional[builtins.str] = None,
        patch_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches: typing.Optional[typing.Sequence[builtins.str]] = None,
        rejected_patches_action: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnPatchBaseline.PatchSourceProperty, _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[_CfnTag_f6864754]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPatchBaseline``.

        :param name: The name of the patch baseline.
        :param approval_rules: A set of rules used to include patches in the baseline.
        :param approved_patches: A list of explicitly approved patches for the baseline. For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .
        :param approved_patches_compliance_level: Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is ``UNSPECIFIED`` .
        :param approved_patches_enable_non_security: Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is ``false`` . Applies to Linux managed nodes only.
        :param description: A description of the patch baseline.
        :param global_filters: A set of global filters used to include patches in the baseline.
        :param operating_system: Defines the operating system the patch baseline applies to. The default value is ``WINDOWS`` .
        :param patch_groups: The name of the patch group to be registered with the patch baseline.
        :param rejected_patches: A list of explicitly rejected patches for the baseline. For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .
        :param rejected_patches_action: The action for Patch Manager to take on patches included in the ``RejectedPackages`` list. - *``ALLOW_AS_DEPENDENCY``* : A package in the ``Rejected`` patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as ``InstalledOther`` . This is the default action if no option is specified. - *``BLOCK``* : Packages in the ``RejectedPatches`` list, and packages that include them as dependencies, aren't installed under any circumstances. If a package was installed before it was added to the Rejected patches list, it is considered non-compliant with the patch baseline, and its status is reported as ``InstalledRejected`` .
        :param sources: Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
        :param tags: Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            cfn_patch_baseline_props = ssm.CfnPatchBaselineProps(
                name="name",
            
                # the properties below are optional
                approval_rules=ssm.CfnPatchBaseline.RuleGroupProperty(
                    patch_rules=[ssm.CfnPatchBaseline.RuleProperty(
                        approve_after_days=123,
                        approve_until_date="approveUntilDate",
                        compliance_level="complianceLevel",
                        enable_non_security=False,
                        patch_filter_group=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                            patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                                key="key",
                                values=["values"]
                            )]
                        )
                    )]
                ),
                approved_patches=["approvedPatches"],
                approved_patches_compliance_level="approvedPatchesComplianceLevel",
                approved_patches_enable_non_security=False,
                description="description",
                global_filters=ssm.CfnPatchBaseline.PatchFilterGroupProperty(
                    patch_filters=[ssm.CfnPatchBaseline.PatchFilterProperty(
                        key="key",
                        values=["values"]
                    )]
                ),
                operating_system="operatingSystem",
                patch_groups=["patchGroups"],
                rejected_patches=["rejectedPatches"],
                rejected_patches_action="rejectedPatchesAction",
                sources=[ssm.CfnPatchBaseline.PatchSourceProperty(
                    configuration="configuration",
                    name="name",
                    products=["products"]
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if approval_rules is not None:
            self._values["approval_rules"] = approval_rules
        if approved_patches is not None:
            self._values["approved_patches"] = approved_patches
        if approved_patches_compliance_level is not None:
            self._values["approved_patches_compliance_level"] = approved_patches_compliance_level
        if approved_patches_enable_non_security is not None:
            self._values["approved_patches_enable_non_security"] = approved_patches_enable_non_security
        if description is not None:
            self._values["description"] = description
        if global_filters is not None:
            self._values["global_filters"] = global_filters
        if operating_system is not None:
            self._values["operating_system"] = operating_system
        if patch_groups is not None:
            self._values["patch_groups"] = patch_groups
        if rejected_patches is not None:
            self._values["rejected_patches"] = rejected_patches
        if rejected_patches_action is not None:
            self._values["rejected_patches_action"] = rejected_patches_action
        if sources is not None:
            self._values["sources"] = sources
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the patch baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def approval_rules(
        self,
    ) -> typing.Optional[typing.Union[CfnPatchBaseline.RuleGroupProperty, _IResolvable_da3f097b]]:
        '''A set of rules used to include patches in the baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvalrules
        '''
        result = self._values.get("approval_rules")
        return typing.cast(typing.Optional[typing.Union[CfnPatchBaseline.RuleGroupProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def approved_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of explicitly approved patches for the baseline.

        For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatches
        '''
        result = self._values.get("approved_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def approved_patches_compliance_level(self) -> typing.Optional[builtins.str]:
        '''Defines the compliance level for approved patches.

        When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is ``UNSPECIFIED`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchescompliancelevel
        '''
        result = self._values.get("approved_patches_compliance_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def approved_patches_enable_non_security(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes.

        The default value is ``false`` . Applies to Linux managed nodes only.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity
        '''
        result = self._values.get("approved_patches_enable_non_security")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the patch baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_filters(
        self,
    ) -> typing.Optional[typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, _IResolvable_da3f097b]]:
        '''A set of global filters used to include patches in the baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-globalfilters
        '''
        result = self._values.get("global_filters")
        return typing.cast(typing.Optional[typing.Union[CfnPatchBaseline.PatchFilterGroupProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''Defines the operating system the patch baseline applies to.

        The default value is ``WINDOWS`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-operatingsystem
        '''
        result = self._values.get("operating_system")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def patch_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the patch group to be registered with the patch baseline.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-patchgroups
        '''
        result = self._values.get("patch_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejected_patches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of explicitly rejected patches for the baseline.

        For information about accepted formats for lists of approved patches and rejected patches, see `About package name formats for approved and rejected patch lists <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html>`_ in the *AWS Systems Manager User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatches
        '''
        result = self._values.get("rejected_patches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rejected_patches_action(self) -> typing.Optional[builtins.str]:
        '''The action for Patch Manager to take on patches included in the ``RejectedPackages`` list.

        - *``ALLOW_AS_DEPENDENCY``* : A package in the ``Rejected`` patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as ``InstalledOther`` . This is the default action if no option is specified.
        - *``BLOCK``* : Packages in the ``RejectedPatches`` list, and packages that include them as dependencies, aren't installed under any circumstances. If a package was installed before it was added to the Rejected patches list, it is considered non-compliant with the patch baseline, and its status is reported as ``InstalledRejected`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatchesaction
        '''
        result = self._values.get("rejected_patches_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnPatchBaseline.PatchSourceProperty, _IResolvable_da3f097b]]]]:
        '''Information about the patches to use to update the managed nodes, including target operating systems and source repositories.

        Applies to Linux managed nodes only.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-sources
        '''
        result = self._values.get("sources")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnPatchBaseline.PatchSourceProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional metadata that you assign to a resource.

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPatchBaselineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceDataSync(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync",
):
    '''A CloudFormation ``AWS::SSM::ResourceDataSync``.

    The ``AWS::SSM::ResourceDataSync`` resource creates, updates, or deletes a resource data sync for AWS Systems Manager . A resource data sync helps you view data from multiple sources in a single location. Systems Manager offers two types of resource data sync: ``SyncToDestination`` and ``SyncFromSource`` .

    You can configure Systems Manager Inventory to use the ``SyncToDestination`` type to synchronize Inventory data from multiple AWS Regions to a single Amazon S3 bucket.

    You can configure Systems Manager Explorer to use the ``SyncFromSource`` type to synchronize operational work items (OpsItems) and operational data (OpsData) from multiple AWS Regions . This type can synchronize OpsItems and OpsData from multiple AWS accounts and Regions or from an ``EntireOrganization`` by using AWS Organizations .

    A resource data sync is an asynchronous operation that returns immediately. After a successful initial sync is completed, the system continuously syncs data.

    By default, data is not encrypted in Amazon S3 . We strongly recommend that you enable encryption in Amazon S3 to ensure secure data storage. We also recommend that you secure access to the Amazon S3 bucket by creating a restrictive bucket policy.

    For more information, see `Configuring Inventory Collection <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html#sysman-inventory-datasync>`_ and `Setting Up Systems Manager Explorer to Display Data from Multiple Accounts and Regions <https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html>`_ in the *AWS Systems Manager User Guide* .

    Important: The following *Syntax* section shows all fields that are supported for a resource data sync. The *Examples* section below shows the recommended way to specify configurations for each sync type. Please see the *Examples* section when you create your resource data sync.

    :cloudformationResource: AWS::SSM::ResourceDataSync
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        cfn_resource_data_sync = ssm.CfnResourceDataSync(self, "MyCfnResourceDataSync",
            sync_name="syncName",
        
            # the properties below are optional
            bucket_name="bucketName",
            bucket_prefix="bucketPrefix",
            bucket_region="bucketRegion",
            kms_key_arn="kmsKeyArn",
            s3_destination=ssm.CfnResourceDataSync.S3DestinationProperty(
                bucket_name="bucketName",
                bucket_region="bucketRegion",
                sync_format="syncFormat",
        
                # the properties below are optional
                bucket_prefix="bucketPrefix",
                kms_key_arn="kmsKeyArn"
            ),
            sync_format="syncFormat",
            sync_source=ssm.CfnResourceDataSync.SyncSourceProperty(
                source_regions=["sourceRegions"],
                source_type="sourceType",
        
                # the properties below are optional
                aws_organizations_source=ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty(
                    organization_source_type="organizationSourceType",
        
                    # the properties below are optional
                    organizational_units=["organizationalUnits"]
                ),
                include_future_regions=False
            ),
            sync_type="syncType"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        sync_name: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        s3_destination: typing.Optional[typing.Union["CfnResourceDataSync.S3DestinationProperty", _IResolvable_da3f097b]] = None,
        sync_format: typing.Optional[builtins.str] = None,
        sync_source: typing.Optional[typing.Union["CfnResourceDataSync.SyncSourceProperty", _IResolvable_da3f097b]] = None,
        sync_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SSM::ResourceDataSync``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param sync_name: A name for the resource data sync.
        :param bucket_name: The name of the S3 bucket where the aggregated data is stored.
        :param bucket_prefix: An Amazon S3 prefix for the bucket.
        :param bucket_region: The AWS Region with the S3 bucket targeted by the resource data sync.
        :param kms_key_arn: The ARN of an encryption key for a destination in Amazon S3 . You can use a KMS key to encrypt inventory data in Amazon S3 . You must specify a key that exist in the same region as the destination Amazon S3 bucket.
        :param s3_destination: Configuration information for the target S3 bucket.
        :param sync_format: A supported sync format. The following format is currently supported: JsonSerDe
        :param sync_source: Information about the source where the data was synchronized.
        :param sync_type: The type of resource data sync. If ``SyncType`` is ``SyncToDestination`` , then the resource data sync synchronizes data to an S3 bucket. If the ``SyncType`` is ``SyncFromSource`` then the resource data sync synchronizes data from AWS Organizations or from multiple AWS Regions .
        '''
        props = CfnResourceDataSyncProps(
            sync_name=sync_name,
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            bucket_region=bucket_region,
            kms_key_arn=kms_key_arn,
            s3_destination=s3_destination,
            sync_format=sync_format,
            sync_source=sync_source,
            sync_type=sync_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSyncName")
    def attr_sync_name(self) -> builtins.str:
        '''The name of the resource data sync.

        :cloudformationAttribute: SyncName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSyncName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncName")
    def sync_name(self) -> builtins.str:
        '''A name for the resource data sync.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncname
        '''
        return typing.cast(builtins.str, jsii.get(self, "syncName"))

    @sync_name.setter
    def sync_name(self, value: builtins.str) -> None:
        jsii.set(self, "syncName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the S3 bucket where the aggregated data is stored.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bucketName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''An Amazon S3 prefix for the bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketprefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bucketPrefix", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucketRegion")
    def bucket_region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region with the S3 bucket targeted by the resource data sync.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketregion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketRegion"))

    @bucket_region.setter
    def bucket_region(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bucketRegion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an encryption key for a destination in Amazon S3 .

        You can use a KMS key to encrypt inventory data in Amazon S3 . You must specify a key that exist in the same region as the destination Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-kmskeyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3Destination")
    def s3_destination(
        self,
    ) -> typing.Optional[typing.Union["CfnResourceDataSync.S3DestinationProperty", _IResolvable_da3f097b]]:
        '''Configuration information for the target S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-s3destination
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResourceDataSync.S3DestinationProperty", _IResolvable_da3f097b]], jsii.get(self, "s3Destination"))

    @s3_destination.setter
    def s3_destination(
        self,
        value: typing.Optional[typing.Union["CfnResourceDataSync.S3DestinationProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "s3Destination", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncFormat")
    def sync_format(self) -> typing.Optional[builtins.str]:
        '''A supported sync format.

        The following format is currently supported: JsonSerDe

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncformat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncFormat"))

    @sync_format.setter
    def sync_format(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "syncFormat", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncSource")
    def sync_source(
        self,
    ) -> typing.Optional[typing.Union["CfnResourceDataSync.SyncSourceProperty", _IResolvable_da3f097b]]:
        '''Information about the source where the data was synchronized.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncsource
        '''
        return typing.cast(typing.Optional[typing.Union["CfnResourceDataSync.SyncSourceProperty", _IResolvable_da3f097b]], jsii.get(self, "syncSource"))

    @sync_source.setter
    def sync_source(
        self,
        value: typing.Optional[typing.Union["CfnResourceDataSync.SyncSourceProperty", _IResolvable_da3f097b]],
    ) -> None:
        jsii.set(self, "syncSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="syncType")
    def sync_type(self) -> typing.Optional[builtins.str]:
        '''The type of resource data sync.

        If ``SyncType`` is ``SyncToDestination`` , then the resource data sync synchronizes data to an S3 bucket. If the ``SyncType`` is ``SyncFromSource`` then the resource data sync synchronizes data from AWS Organizations or from multiple AWS Regions .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-synctype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncType"))

    @sync_type.setter
    def sync_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "syncType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "organization_source_type": "organizationSourceType",
            "organizational_units": "organizationalUnits",
        },
    )
    class AwsOrganizationsSourceProperty:
        def __init__(
            self,
            *,
            organization_source_type: builtins.str,
            organizational_units: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Information about the ``AwsOrganizationsSource`` resource data sync source.

            A sync source of this type can synchronize data from AWS Organizations or, if an AWS organization isn't present, from multiple AWS Regions .

            :param organization_source_type: If an AWS organization is present, this is either ``OrganizationalUnits`` or ``EntireOrganization`` . For ``OrganizationalUnits`` , the data is aggregated from a set of organization units. For ``EntireOrganization`` , the data is aggregated from the entire AWS organization.
            :param organizational_units: The AWS Organizations organization units included in the sync.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                aws_organizations_source_property = ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty(
                    organization_source_type="organizationSourceType",
                
                    # the properties below are optional
                    organizational_units=["organizationalUnits"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "organization_source_type": organization_source_type,
            }
            if organizational_units is not None:
                self._values["organizational_units"] = organizational_units

        @builtins.property
        def organization_source_type(self) -> builtins.str:
            '''If an AWS organization is present, this is either ``OrganizationalUnits`` or ``EntireOrganization`` .

            For ``OrganizationalUnits`` , the data is aggregated from a set of organization units. For ``EntireOrganization`` , the data is aggregated from the entire AWS organization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html#cfn-ssm-resourcedatasync-awsorganizationssource-organizationsourcetype
            '''
            result = self._values.get("organization_source_type")
            assert result is not None, "Required property 'organization_source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def organizational_units(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The AWS Organizations organization units included in the sync.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html#cfn-ssm-resourcedatasync-awsorganizationssource-organizationalunits
            '''
            result = self._values.get("organizational_units")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsOrganizationsSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync.S3DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "bucket_region": "bucketRegion",
            "sync_format": "syncFormat",
            "bucket_prefix": "bucketPrefix",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class S3DestinationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_region: builtins.str,
            sync_format: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the target S3 bucket for the resource data sync.

            :param bucket_name: The name of the S3 bucket where the aggregated data is stored.
            :param bucket_region: The AWS Region with the S3 bucket targeted by the resource data sync.
            :param sync_format: A supported sync format. The following format is currently supported: JsonSerDe
            :param bucket_prefix: An Amazon S3 prefix for the bucket.
            :param kms_key_arn: The ARN of an encryption key for a destination in Amazon S3. Must belong to the same Region as the destination S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                s3_destination_property = ssm.CfnResourceDataSync.S3DestinationProperty(
                    bucket_name="bucketName",
                    bucket_region="bucketRegion",
                    sync_format="syncFormat",
                
                    # the properties below are optional
                    bucket_prefix="bucketPrefix",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_name": bucket_name,
                "bucket_region": bucket_region,
                "sync_format": sync_format,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of the S3 bucket where the aggregated data is stored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_region(self) -> builtins.str:
            '''The AWS Region with the S3 bucket targeted by the resource data sync.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketregion
            '''
            result = self._values.get("bucket_region")
            assert result is not None, "Required property 'bucket_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sync_format(self) -> builtins.str:
            '''A supported sync format.

            The following format is currently supported: JsonSerDe

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-syncformat
            '''
            result = self._values.get("sync_format")
            assert result is not None, "Required property 'sync_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''An Amazon S3 prefix for the bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of an encryption key for a destination in Amazon S3.

            Must belong to the same Region as the destination S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html#cfn-ssm-resourcedatasync-s3destination-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSync.SyncSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_regions": "sourceRegions",
            "source_type": "sourceType",
            "aws_organizations_source": "awsOrganizationsSource",
            "include_future_regions": "includeFutureRegions",
        },
    )
    class SyncSourceProperty:
        def __init__(
            self,
            *,
            source_regions: typing.Sequence[builtins.str],
            source_type: builtins.str,
            aws_organizations_source: typing.Optional[typing.Union["CfnResourceDataSync.AwsOrganizationsSourceProperty", _IResolvable_da3f097b]] = None,
            include_future_regions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Information about the source of the data included in the resource data sync.

            :param source_regions: The ``SyncSource`` AWS Regions included in the resource data sync.
            :param source_type: The type of data source for the resource data sync. ``SourceType`` is either ``AwsOrganizations`` (if an organization is present in AWS Organizations ) or ``SingleAccountMultiRegions`` .
            :param aws_organizations_source: Information about the AwsOrganizationsSource resource data sync source. A sync source of this type can synchronize data from AWS Organizations .
            :param include_future_regions: Whether to automatically synchronize and aggregate data from new AWS Regions when those Regions come online.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssm as ssm
                
                sync_source_property = ssm.CfnResourceDataSync.SyncSourceProperty(
                    source_regions=["sourceRegions"],
                    source_type="sourceType",
                
                    # the properties below are optional
                    aws_organizations_source=ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty(
                        organization_source_type="organizationSourceType",
                
                        # the properties below are optional
                        organizational_units=["organizationalUnits"]
                    ),
                    include_future_regions=False
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "source_regions": source_regions,
                "source_type": source_type,
            }
            if aws_organizations_source is not None:
                self._values["aws_organizations_source"] = aws_organizations_source
            if include_future_regions is not None:
                self._values["include_future_regions"] = include_future_regions

        @builtins.property
        def source_regions(self) -> typing.List[builtins.str]:
            '''The ``SyncSource`` AWS Regions included in the resource data sync.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-sourceregions
            '''
            result = self._values.get("source_regions")
            assert result is not None, "Required property 'source_regions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def source_type(self) -> builtins.str:
            '''The type of data source for the resource data sync.

            ``SourceType`` is either ``AwsOrganizations`` (if an organization is present in AWS Organizations ) or ``SingleAccountMultiRegions`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-sourcetype
            '''
            result = self._values.get("source_type")
            assert result is not None, "Required property 'source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_organizations_source(
            self,
        ) -> typing.Optional[typing.Union["CfnResourceDataSync.AwsOrganizationsSourceProperty", _IResolvable_da3f097b]]:
            '''Information about the AwsOrganizationsSource resource data sync source.

            A sync source of this type can synchronize data from AWS Organizations .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-awsorganizationssource
            '''
            result = self._values.get("aws_organizations_source")
            return typing.cast(typing.Optional[typing.Union["CfnResourceDataSync.AwsOrganizationsSourceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def include_future_regions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether to automatically synchronize and aggregate data from new AWS Regions when those Regions come online.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html#cfn-ssm-resourcedatasync-syncsource-includefutureregions
            '''
            result = self._values.get("include_future_regions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CfnResourceDataSyncProps",
    jsii_struct_bases=[],
    name_mapping={
        "sync_name": "syncName",
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "bucket_region": "bucketRegion",
        "kms_key_arn": "kmsKeyArn",
        "s3_destination": "s3Destination",
        "sync_format": "syncFormat",
        "sync_source": "syncSource",
        "sync_type": "syncType",
    },
)
class CfnResourceDataSyncProps:
    def __init__(
        self,
        *,
        sync_name: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        bucket_region: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        s3_destination: typing.Optional[typing.Union[CfnResourceDataSync.S3DestinationProperty, _IResolvable_da3f097b]] = None,
        sync_format: typing.Optional[builtins.str] = None,
        sync_source: typing.Optional[typing.Union[CfnResourceDataSync.SyncSourceProperty, _IResolvable_da3f097b]] = None,
        sync_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourceDataSync``.

        :param sync_name: A name for the resource data sync.
        :param bucket_name: The name of the S3 bucket where the aggregated data is stored.
        :param bucket_prefix: An Amazon S3 prefix for the bucket.
        :param bucket_region: The AWS Region with the S3 bucket targeted by the resource data sync.
        :param kms_key_arn: The ARN of an encryption key for a destination in Amazon S3 . You can use a KMS key to encrypt inventory data in Amazon S3 . You must specify a key that exist in the same region as the destination Amazon S3 bucket.
        :param s3_destination: Configuration information for the target S3 bucket.
        :param sync_format: A supported sync format. The following format is currently supported: JsonSerDe
        :param sync_source: Information about the source where the data was synchronized.
        :param sync_type: The type of resource data sync. If ``SyncType`` is ``SyncToDestination`` , then the resource data sync synchronizes data to an S3 bucket. If the ``SyncType`` is ``SyncFromSource`` then the resource data sync synchronizes data from AWS Organizations or from multiple AWS Regions .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            cfn_resource_data_sync_props = ssm.CfnResourceDataSyncProps(
                sync_name="syncName",
            
                # the properties below are optional
                bucket_name="bucketName",
                bucket_prefix="bucketPrefix",
                bucket_region="bucketRegion",
                kms_key_arn="kmsKeyArn",
                s3_destination=ssm.CfnResourceDataSync.S3DestinationProperty(
                    bucket_name="bucketName",
                    bucket_region="bucketRegion",
                    sync_format="syncFormat",
            
                    # the properties below are optional
                    bucket_prefix="bucketPrefix",
                    kms_key_arn="kmsKeyArn"
                ),
                sync_format="syncFormat",
                sync_source=ssm.CfnResourceDataSync.SyncSourceProperty(
                    source_regions=["sourceRegions"],
                    source_type="sourceType",
            
                    # the properties below are optional
                    aws_organizations_source=ssm.CfnResourceDataSync.AwsOrganizationsSourceProperty(
                        organization_source_type="organizationSourceType",
            
                        # the properties below are optional
                        organizational_units=["organizationalUnits"]
                    ),
                    include_future_regions=False
                ),
                sync_type="syncType"
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "sync_name": sync_name,
        }
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if bucket_region is not None:
            self._values["bucket_region"] = bucket_region
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if s3_destination is not None:
            self._values["s3_destination"] = s3_destination
        if sync_format is not None:
            self._values["sync_format"] = sync_format
        if sync_source is not None:
            self._values["sync_source"] = sync_source
        if sync_type is not None:
            self._values["sync_type"] = sync_type

    @builtins.property
    def sync_name(self) -> builtins.str:
        '''A name for the resource data sync.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncname
        '''
        result = self._values.get("sync_name")
        assert result is not None, "Required property 'sync_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the S3 bucket where the aggregated data is stored.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketname
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''An Amazon S3 prefix for the bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketprefix
        '''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_region(self) -> typing.Optional[builtins.str]:
        '''The AWS Region with the S3 bucket targeted by the resource data sync.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketregion
        '''
        result = self._values.get("bucket_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an encryption key for a destination in Amazon S3 .

        You can use a KMS key to encrypt inventory data in Amazon S3 . You must specify a key that exist in the same region as the destination Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_destination(
        self,
    ) -> typing.Optional[typing.Union[CfnResourceDataSync.S3DestinationProperty, _IResolvable_da3f097b]]:
        '''Configuration information for the target S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-s3destination
        '''
        result = self._values.get("s3_destination")
        return typing.cast(typing.Optional[typing.Union[CfnResourceDataSync.S3DestinationProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def sync_format(self) -> typing.Optional[builtins.str]:
        '''A supported sync format.

        The following format is currently supported: JsonSerDe

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncformat
        '''
        result = self._values.get("sync_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_source(
        self,
    ) -> typing.Optional[typing.Union[CfnResourceDataSync.SyncSourceProperty, _IResolvable_da3f097b]]:
        '''Information about the source where the data was synchronized.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncsource
        '''
        result = self._values.get("sync_source")
        return typing.cast(typing.Optional[typing.Union[CfnResourceDataSync.SyncSourceProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def sync_type(self) -> typing.Optional[builtins.str]:
        '''The type of resource data sync.

        If ``SyncType`` is ``SyncToDestination`` , then the resource data sync synchronizes data to an S3 bucket. If the ``SyncType`` is ``SyncFromSource`` then the resource data sync synchronizes data from AWS Organizations or from multiple AWS Regions .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-synctype
        '''
        result = self._values.get("sync_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceDataSyncProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.CommonStringParameterAttributes",
    jsii_struct_bases=[],
    name_mapping={"parameter_name": "parameterName", "simple_name": "simpleName"},
)
class CommonStringParameterAttributes:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Common attributes for string parameters.

        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            common_string_parameter_attributes = ssm.CommonStringParameterAttributes(
                parameter_name="parameterName",
            
                # the properties below are optional
                simple_name=False
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonStringParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_ssm.IParameter")
class IParameter(_IResource_c80c4260, typing_extensions.Protocol):
    '''An SSM Parameter reference.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''The ARN of the SSM Parameter resource.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''The name of the SSM Parameter resource.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''The type of the SSM Parameter resource.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: the role to be granted read-only access to the parameter.
        '''
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: the role to be granted write access to the parameter.
        '''
        ...


class _IParameterProxy(
    jsii.proxy_for(_IResource_c80c4260) # type: ignore[misc]
):
    '''An SSM Parameter reference.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ssm.IParameter"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''The ARN of the SSM Parameter resource.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''The name of the SSM Parameter resource.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''The type of the SSM Parameter resource.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: the role to be granted read-only access to the parameter.
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: the role to be granted write access to the parameter.
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameter).__jsii_proxy_class__ = lambda : _IParameterProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ssm.IStringListParameter")
class IStringListParameter(IParameter, typing_extensions.Protocol):
    '''A StringList SSM Parameter.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).

        :attribute: Value
        '''
        ...


class _IStringListParameterProxy(
    jsii.proxy_for(IParameter) # type: ignore[misc]
):
    '''A StringList SSM Parameter.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ssm.IStringListParameter"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).

        :attribute: Value
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStringListParameter).__jsii_proxy_class__ = lambda : _IStringListParameterProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ssm.IStringParameter")
class IStringParameter(IParameter, typing_extensions.Protocol):
    '''A String SSM Parameter.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.

        :attribute: Value
        '''
        ...


class _IStringParameterProxy(
    jsii.proxy_for(IParameter) # type: ignore[misc]
):
    '''A String SSM Parameter.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ssm.IStringParameter"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.

        :attribute: Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStringParameter).__jsii_proxy_class__ = lambda : _IStringParameterProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_ssm.ParameterDataType")
class ParameterDataType(enum.Enum):
    '''SSM parameter data type.'''

    TEXT = "TEXT"
    '''Text.'''
    AWS_EC2_IMAGE = "AWS_EC2_IMAGE"
    '''Aws Ec2 Image.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.ParameterOptions",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "description": "description",
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "tier": "tier",
    },
)
class ParameterOptions:
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional["ParameterTier"] = None,
    ) -> None:
        '''Properties needed to create a new SSM Parameter.

        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            parameter_options = ssm.ParameterOptions(
                allowed_pattern="allowedPattern",
                description="description",
                parameter_name="parameterName",
                simple_name=False,
                tier=ssm.ParameterTier.ADVANCED
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if description is not None:
            self._values["description"] = description
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\\d+$``

        :default: no validation is performed
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter that you want to add to the system.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.

        :default: - a name will be generated by CloudFormation
        '''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tier(self) -> typing.Optional["ParameterTier"]:
        '''The tier of the string parameter.

        :default: - undefined
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional["ParameterTier"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParameterOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ssm.ParameterTier")
class ParameterTier(enum.Enum):
    '''SSM parameter tier.

    :exampleMetadata: infused

    Example::

        ssm.StringParameter(self, "Parameter",
            allowed_pattern=".*",
            description="The value Foo",
            parameter_name="FooParameter",
            string_value="Foo",
            tier=ssm.ParameterTier.ADVANCED
        )
    '''

    ADVANCED = "ADVANCED"
    '''String.'''
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    '''String.'''
    STANDARD = "STANDARD"
    '''String.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_ssm.ParameterType")
class ParameterType(enum.Enum):
    '''SSM parameter type.'''

    STRING = "STRING"
    '''String.'''
    SECURE_STRING = "SECURE_STRING"
    '''Secure String.

    Parameter Store uses an AWS Key Management Service (KMS) customer master key (CMK) to encrypt the parameter value.
    Parameters of type SecureString cannot be created directly from a CDK application.
    '''
    STRING_LIST = "STRING_LIST"
    '''String List.'''
    AWS_EC2_IMAGE_ID = "AWS_EC2_IMAGE_ID"
    '''An Amazon EC2 image ID, such as ami-0ff8a91507f77f867.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.SecureStringParameterAttributes",
    jsii_struct_bases=[CommonStringParameterAttributes],
    name_mapping={
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "encryption_key": "encryptionKey",
        "version": "version",
    },
)
class SecureStringParameterAttributes(CommonStringParameterAttributes):
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Attributes for secure string parameters.

        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param encryption_key: The encryption key that is used to encrypt this parameter. Default: - default master key
        :param version: The version number of the value you wish to retrieve. Default: - AWS CloudFormation uses the latest version of the parameter

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kms as kms
            from aws_cdk import aws_ssm as ssm
            
            # key: kms.Key
            
            secure_string_parameter_attributes = ssm.SecureStringParameterAttributes(
                parameter_name="parameterName",
            
                # the properties below are optional
                encryption_key=key,
                simple_name=False,
                version=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The encryption key that is used to encrypt this parameter.

        :default: - default master key
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''The version number of the value you wish to retrieve.

        :default: - AWS CloudFormation uses the latest version of the parameter
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecureStringParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStringListParameter, IParameter)
class StringListParameter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.StringListParameter",
):
    '''Creates a new StringList SSM Parameter.

    :resource: AWS::SSM::Parameter
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssm as ssm
        
        string_list_parameter = ssm.StringListParameter(self, "MyStringListParameter",
            string_list_value=["stringListValue"],
        
            # the properties below are optional
            allowed_pattern="allowedPattern",
            description="description",
            parameter_name="parameterName",
            simple_name=False,
            tier=ssm.ParameterTier.ADVANCED
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        string_list_value: typing.Sequence[builtins.str],
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param string_list_value: The values of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined
        '''
        props = StringListParameterProps(
            string_list_value=string_list_value,
            allowed_pattern=allowed_pattern,
            description=description,
            parameter_name=parameter_name,
            simple_name=simple_name,
            tier=tier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromStringListParameterName") # type: ignore[misc]
    @builtins.classmethod
    def from_string_list_parameter_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        string_list_parameter_name: builtins.str,
    ) -> IStringListParameter:
        '''Imports an external parameter of type string list.

        Returns a token and should not be parsed.

        :param scope: -
        :param id: -
        :param string_list_parameter_name: -
        '''
        return typing.cast(IStringListParameter, jsii.sinvoke(cls, "fromStringListParameterName", [scope, id, string_list_parameter_name]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: -
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: -
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''The ARN of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''The name of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''The type of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The encryption key that is used to encrypt this parameter.

        - @default - default master key
        '''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "encryptionKey"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.StringListParameterProps",
    jsii_struct_bases=[ParameterOptions],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "description": "description",
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "tier": "tier",
        "string_list_value": "stringListValue",
    },
)
class StringListParameterProps(ParameterOptions):
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
        string_list_value: typing.Sequence[builtins.str],
    ) -> None:
        '''Properties needed to create a StringList SSM Parameter.

        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined
        :param string_list_value: The values of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            string_list_parameter_props = ssm.StringListParameterProps(
                string_list_value=["stringListValue"],
            
                # the properties below are optional
                allowed_pattern="allowedPattern",
                description="description",
                parameter_name="parameterName",
                simple_name=False,
                tier=ssm.ParameterTier.ADVANCED
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "string_list_value": string_list_value,
        }
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if description is not None:
            self._values["description"] = description
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\\d+$``

        :default: no validation is performed
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter that you want to add to the system.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.

        :default: - a name will be generated by CloudFormation
        '''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tier(self) -> typing.Optional[ParameterTier]:
        '''The tier of the string parameter.

        :default: - undefined
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[ParameterTier], result)

    @builtins.property
    def string_list_value(self) -> typing.List[builtins.str]:
        '''The values of the parameter.

        It may not reference another parameter and ``{{}}`` cannot be used in the value.
        '''
        result = self._values.get("string_list_value")
        assert result is not None, "Required property 'string_list_value' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringListParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStringParameter, IParameter)
class StringParameter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssm.StringParameter",
):
    '''Creates a new String SSM Parameter.

    :exampleMetadata: infused
    :resource: AWS::SSM::Parameter

    Example::

        # Example automatically generated from non-compiling source. May contain errors.
        vpc = ec2.Vpc.from_vpc_attributes(self, "VPC",
            vpc_id="vpc-1234",
            availability_zones=["us-east-1a", "us-east-1b"],
        
            # Either pass literals for all IDs
            public_subnet_ids=["s-12345", "s-67890"],
        
            # OR: import a list of known length
            private_subnet_ids=Fn.import_list_value("PrivateSubnetIds", 2),
        
            # OR: split an imported string to a list of known length
            isolated_subnet_ids=Fn.split(",", ssm.StringParameter.value_for_string_parameter(self, "MyParameter"), 2)
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        string_value: builtins.str,
        data_type: typing.Optional[ParameterDataType] = None,
        type: typing.Optional[ParameterType] = None,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param string_value: The value of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param data_type: The data type of the parameter, such as ``text`` or ``aws:ec2:image``. Default: - undefined
        :param type: The type of the string parameter. Default: ParameterType.STRING
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined
        '''
        props = StringParameterProps(
            string_value=string_value,
            data_type=data_type,
            type=type,
            allowed_pattern=allowed_pattern,
            description=description,
            parameter_name=parameter_name,
            simple_name=simple_name,
            tier=tier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromSecureStringParameterAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_secure_string_parameter_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        version: typing.Optional[jsii.Number] = None,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> IStringParameter:
        '''Imports a secure string parameter from the SSM parameter store.

        :param scope: -
        :param id: -
        :param encryption_key: The encryption key that is used to encrypt this parameter. Default: - default master key
        :param version: The version number of the value you wish to retrieve. Default: - AWS CloudFormation uses the latest version of the parameter
        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        '''
        attrs = SecureStringParameterAttributes(
            encryption_key=encryption_key,
            version=version,
            parameter_name=parameter_name,
            simple_name=simple_name,
        )

        return typing.cast(IStringParameter, jsii.sinvoke(cls, "fromSecureStringParameterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromStringParameterAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_string_parameter_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        type: typing.Optional[ParameterType] = None,
        version: typing.Optional[jsii.Number] = None,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
    ) -> IStringParameter:
        '''Imports an external string parameter with name and optional version.

        :param scope: -
        :param id: -
        :param type: The type of the string parameter. Default: ParameterType.STRING
        :param version: The version number of the value you wish to retrieve. Default: The latest version will be retrieved.
        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        '''
        attrs = StringParameterAttributes(
            type=type,
            version=version,
            parameter_name=parameter_name,
            simple_name=simple_name,
        )

        return typing.cast(IStringParameter, jsii.sinvoke(cls, "fromStringParameterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromStringParameterName") # type: ignore[misc]
    @builtins.classmethod
    def from_string_parameter_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        string_parameter_name: builtins.str,
    ) -> IStringParameter:
        '''Imports an external string parameter by name.

        :param scope: -
        :param id: -
        :param string_parameter_name: -
        '''
        return typing.cast(IStringParameter, jsii.sinvoke(cls, "fromStringParameterName", [scope, id, string_parameter_name]))

    @jsii.member(jsii_name="valueForSecureStringParameter") # type: ignore[misc]
    @builtins.classmethod
    def value_for_secure_string_parameter(
        cls,
        scope: constructs.Construct,
        parameter_name: builtins.str,
        version: jsii.Number,
    ) -> builtins.str:
        '''Returns a token that will resolve (during deployment).

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param version: The parameter version (required for secure strings).
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForSecureStringParameter", [scope, parameter_name, version]))

    @jsii.member(jsii_name="valueForStringParameter") # type: ignore[misc]
    @builtins.classmethod
    def value_for_string_parameter(
        cls,
        scope: constructs.Construct,
        parameter_name: builtins.str,
        version: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Returns a token that will resolve (during deployment) to the string value of an SSM string parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForStringParameter", [scope, parameter_name, version]))

    @jsii.member(jsii_name="valueForTypedStringParameter") # type: ignore[misc]
    @builtins.classmethod
    def value_for_typed_string_parameter(
        cls,
        scope: constructs.Construct,
        parameter_name: builtins.str,
        type: typing.Optional[ParameterType] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Returns a token that will resolve (during deployment) to the string value of an SSM string parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param type: The type of the SSM parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueForTypedStringParameter", [scope, parameter_name, type, version]))

    @jsii.member(jsii_name="valueFromLookup") # type: ignore[misc]
    @builtins.classmethod
    def value_from_lookup(
        cls,
        scope: constructs.Construct,
        parameter_name: builtins.str,
    ) -> builtins.str:
        '''Reads the value of an SSM parameter during synthesis through an environmental context provider.

        Requires that the stack this scope is defined in will have explicit
        account/region information. Otherwise, it will fail during synthesis.

        :param scope: -
        :param parameter_name: -
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueFromLookup", [scope, parameter_name]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: -
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: -
        '''
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> builtins.str:
        '''The ARN of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        '''The name of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''The type of the SSM Parameter resource.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        '''The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.
        '''
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The encryption key that is used to encrypt this parameter.

        - @default - default master key
        '''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "encryptionKey"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.StringParameterAttributes",
    jsii_struct_bases=[CommonStringParameterAttributes],
    name_mapping={
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "type": "type",
        "version": "version",
    },
)
class StringParameterAttributes(CommonStringParameterAttributes):
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        simple_name: typing.Optional[builtins.bool] = None,
        type: typing.Optional[ParameterType] = None,
        version: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Attributes for parameters of various types of string.

        :param parameter_name: The name of the parameter store value. This value can be a token or a concrete string. If it is a concrete string and includes "/" it must also be prefixed with a "/" (fully-qualified).
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param type: The type of the string parameter. Default: ParameterType.STRING
        :param version: The version number of the value you wish to retrieve. Default: The latest version will be retrieved.

        :see: ParameterType
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssm as ssm
            
            string_parameter_attributes = ssm.StringParameterAttributes(
                parameter_name="parameterName",
            
                # the properties below are optional
                simple_name=False,
                type=ssm.ParameterType.STRING,
                version=123
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
        }
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if type is not None:
            self._values["type"] = type
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The name of the parameter store value.

        This value can be a token or a concrete string. If it is a concrete string
        and includes "/" it must also be prefixed with a "/" (fully-qualified).
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def type(self) -> typing.Optional[ParameterType]:
        '''The type of the string parameter.

        :default: ParameterType.STRING
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ParameterType], result)

    @builtins.property
    def version(self) -> typing.Optional[jsii.Number]:
        '''The version number of the value you wish to retrieve.

        :default: The latest version will be retrieved.
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringParameterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssm.StringParameterProps",
    jsii_struct_bases=[ParameterOptions],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "description": "description",
        "parameter_name": "parameterName",
        "simple_name": "simpleName",
        "tier": "tier",
        "string_value": "stringValue",
        "data_type": "dataType",
        "type": "type",
    },
)
class StringParameterProps(ParameterOptions):
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        parameter_name: typing.Optional[builtins.str] = None,
        simple_name: typing.Optional[builtins.bool] = None,
        tier: typing.Optional[ParameterTier] = None,
        string_value: builtins.str,
        data_type: typing.Optional[ParameterDataType] = None,
        type: typing.Optional[ParameterType] = None,
    ) -> None:
        '''Properties needed to create a String SSM parameter.

        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param simple_name: Indicates of the parameter name is a simple name (i.e. does not include "/" separators). This is only required only if ``parameterName`` is a token, which means we are unable to detect if the name is simple or "path-like" for the purpose of rendering SSM parameter ARNs. If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or undefined) since the name generated by AWS CloudFormation is always a simple name. Default: - auto-detect based on ``parameterName``
        :param tier: The tier of the string parameter. Default: - undefined
        :param string_value: The value of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param data_type: The data type of the parameter, such as ``text`` or ``aws:ec2:image``. Default: - undefined
        :param type: The type of the string parameter. Default: ParameterType.STRING

        :exampleMetadata: infused

        Example::

            ssm.StringParameter(self, "Parameter",
                allowed_pattern=".*",
                description="The value Foo",
                parameter_name="FooParameter",
                string_value="Foo",
                tier=ssm.ParameterTier.ADVANCED
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "string_value": string_value,
        }
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if description is not None:
            self._values["description"] = description
        if parameter_name is not None:
            self._values["parameter_name"] = parameter_name
        if simple_name is not None:
            self._values["simple_name"] = simple_name
        if tier is not None:
            self._values["tier"] = tier
        if data_type is not None:
            self._values["data_type"] = data_type
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\\d+$``

        :default: no validation is performed
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the parameter that you want to add to the system.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter.

        :default: - a name will be generated by CloudFormation
        '''
        result = self._values.get("parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def simple_name(self) -> typing.Optional[builtins.bool]:
        '''Indicates of the parameter name is a simple name (i.e. does not include "/" separators).

        This is only required only if ``parameterName`` is a token, which means we
        are unable to detect if the name is simple or "path-like" for the purpose
        of rendering SSM parameter ARNs.

        If ``parameterName`` is not specified, ``simpleName`` must be ``true`` (or
        undefined) since the name generated by AWS CloudFormation is always a
        simple name.

        :default: - auto-detect based on ``parameterName``
        '''
        result = self._values.get("simple_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tier(self) -> typing.Optional[ParameterTier]:
        '''The tier of the string parameter.

        :default: - undefined
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[ParameterTier], result)

    @builtins.property
    def string_value(self) -> builtins.str:
        '''The value of the parameter.

        It may not reference another parameter and ``{{}}`` cannot be used in the value.
        '''
        result = self._values.get("string_value")
        assert result is not None, "Required property 'string_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_type(self) -> typing.Optional[ParameterDataType]:
        '''The data type of the parameter, such as ``text`` or ``aws:ec2:image``.

        :default: - undefined
        '''
        result = self._values.get("data_type")
        return typing.cast(typing.Optional[ParameterDataType], result)

    @builtins.property
    def type(self) -> typing.Optional[ParameterType]:
        '''The type of the string parameter.

        :default: ParameterType.STRING
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ParameterType], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssociation",
    "CfnAssociationProps",
    "CfnDocument",
    "CfnDocumentProps",
    "CfnMaintenanceWindow",
    "CfnMaintenanceWindowProps",
    "CfnMaintenanceWindowTarget",
    "CfnMaintenanceWindowTargetProps",
    "CfnMaintenanceWindowTask",
    "CfnMaintenanceWindowTaskProps",
    "CfnParameter",
    "CfnParameterProps",
    "CfnPatchBaseline",
    "CfnPatchBaselineProps",
    "CfnResourceDataSync",
    "CfnResourceDataSyncProps",
    "CommonStringParameterAttributes",
    "IParameter",
    "IStringListParameter",
    "IStringParameter",
    "ParameterDataType",
    "ParameterOptions",
    "ParameterTier",
    "ParameterType",
    "SecureStringParameterAttributes",
    "StringListParameter",
    "StringListParameterProps",
    "StringParameter",
    "StringParameterAttributes",
    "StringParameterProps",
]

publication.publish()
