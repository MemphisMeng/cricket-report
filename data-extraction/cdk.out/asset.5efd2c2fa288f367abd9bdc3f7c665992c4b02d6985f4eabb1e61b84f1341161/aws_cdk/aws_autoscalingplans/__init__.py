'''
# AWS Auto Scaling Plans Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_autoscalingplans as autoscalingplans
```

> The construct library for this service is in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-autoscalingplans-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AutoScalingPlans](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AutoScalingPlans.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnScalingPlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan",
):
    '''A CloudFormation ``AWS::AutoScalingPlans::ScalingPlan``.

    The ``AWS::AutoScalingPlans::ScalingPlan`` resource defines an AWS Auto Scaling scaling plan. A scaling plan is used to scale application resources to size them appropriately to ensure that enough resource is available in the application at peak times and to reduce allocated resource during periods of low utilization. The following resources can be added to a scaling plan:

    - Amazon EC2 Auto Scaling groups
    - Amazon EC2 Spot Fleet requests
    - Amazon ECS services
    - Amazon DynamoDB tables and global secondary indexes
    - Amazon Aurora Replicas

    For more information, see the `AWS Auto Scaling User Guide <https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html>`_ .

    :cloudformationResource: AWS::AutoScalingPlans::ScalingPlan
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_autoscalingplans as autoscalingplans
        
        cfn_scaling_plan = autoscalingplans.CfnScalingPlan(self, "MyCfnScalingPlan",
            application_source=autoscalingplans.CfnScalingPlan.ApplicationSourceProperty(
                cloud_formation_stack_arn="cloudFormationStackArn",
                tag_filters=[autoscalingplans.CfnScalingPlan.TagFilterProperty(
                    key="key",
        
                    # the properties below are optional
                    values=["values"]
                )]
            ),
            scaling_instructions=[autoscalingplans.CfnScalingPlan.ScalingInstructionProperty(
                max_capacity=123,
                min_capacity=123,
                resource_id="resourceId",
                scalable_dimension="scalableDimension",
                service_namespace="serviceNamespace",
                target_tracking_configurations=[autoscalingplans.CfnScalingPlan.TargetTrackingConfigurationProperty(
                    target_value=123,
        
                    # the properties below are optional
                    customized_scaling_metric_specification=autoscalingplans.CfnScalingPlan.CustomizedScalingMetricSpecificationProperty(
                        metric_name="metricName",
                        namespace="namespace",
                        statistic="statistic",
        
                        # the properties below are optional
                        dimensions=[autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        unit="unit"
                    ),
                    disable_scale_in=False,
                    estimated_instance_warmup=123,
                    predefined_scaling_metric_specification=autoscalingplans.CfnScalingPlan.PredefinedScalingMetricSpecificationProperty(
                        predefined_scaling_metric_type="predefinedScalingMetricType",
        
                        # the properties below are optional
                        resource_label="resourceLabel"
                    ),
                    scale_in_cooldown=123,
                    scale_out_cooldown=123
                )],
        
                # the properties below are optional
                customized_load_metric_specification=autoscalingplans.CfnScalingPlan.CustomizedLoadMetricSpecificationProperty(
                    metric_name="metricName",
                    namespace="namespace",
                    statistic="statistic",
        
                    # the properties below are optional
                    dimensions=[autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    unit="unit"
                ),
                disable_dynamic_scaling=False,
                predefined_load_metric_specification=autoscalingplans.CfnScalingPlan.PredefinedLoadMetricSpecificationProperty(
                    predefined_load_metric_type="predefinedLoadMetricType",
        
                    # the properties below are optional
                    resource_label="resourceLabel"
                ),
                predictive_scaling_max_capacity_behavior="predictiveScalingMaxCapacityBehavior",
                predictive_scaling_max_capacity_buffer=123,
                predictive_scaling_mode="predictiveScalingMode",
                scaling_policy_update_behavior="scalingPolicyUpdateBehavior",
                scheduled_action_buffer_time=123
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        application_source: typing.Union["CfnScalingPlan.ApplicationSourceProperty", _IResolvable_da3f097b],
        scaling_instructions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnScalingPlan.ScalingInstructionProperty", _IResolvable_da3f097b]]],
    ) -> None:
        '''Create a new ``AWS::AutoScalingPlans::ScalingPlan``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_source: A CloudFormation stack or a set of tags. You can create one scaling plan per application source. The ``ApplicationSource`` property must be present to ensure interoperability with the AWS Auto Scaling console.
        :param scaling_instructions: The scaling instructions.
        '''
        props = CfnScalingPlanProps(
            application_source=application_source,
            scaling_instructions=scaling_instructions,
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
    @jsii.member(jsii_name="attrScalingPlanName")
    def attr_scaling_plan_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ScalingPlanName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScalingPlanName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrScalingPlanVersion")
    def attr_scaling_plan_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: ScalingPlanVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScalingPlanVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationSource")
    def application_source(
        self,
    ) -> typing.Union["CfnScalingPlan.ApplicationSourceProperty", _IResolvable_da3f097b]:
        '''A CloudFormation stack or a set of tags.

        You can create one scaling plan per application source. The ``ApplicationSource`` property must be present to ensure interoperability with the AWS Auto Scaling console.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-applicationsource
        '''
        return typing.cast(typing.Union["CfnScalingPlan.ApplicationSourceProperty", _IResolvable_da3f097b], jsii.get(self, "applicationSource"))

    @application_source.setter
    def application_source(
        self,
        value: typing.Union["CfnScalingPlan.ApplicationSourceProperty", _IResolvable_da3f097b],
    ) -> None:
        jsii.set(self, "applicationSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalingInstructions")
    def scaling_instructions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.ScalingInstructionProperty", _IResolvable_da3f097b]]]:
        '''The scaling instructions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-scalinginstructions
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.ScalingInstructionProperty", _IResolvable_da3f097b]]], jsii.get(self, "scalingInstructions"))

    @scaling_instructions.setter
    def scaling_instructions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.ScalingInstructionProperty", _IResolvable_da3f097b]]],
    ) -> None:
        jsii.set(self, "scalingInstructions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan.ApplicationSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_formation_stack_arn": "cloudFormationStackArn",
            "tag_filters": "tagFilters",
        },
    )
    class ApplicationSourceProperty:
        def __init__(
            self,
            *,
            cloud_formation_stack_arn: typing.Optional[builtins.str] = None,
            tag_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnScalingPlan.TagFilterProperty", _IResolvable_da3f097b]]]] = None,
        ) -> None:
            '''``ApplicationSource`` is a property of `ScalingPlan <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html>`_ that specifies the application source to use with AWS Auto Scaling ( Auto Scaling Plans ). You can create one scaling plan per application source.

            :param cloud_formation_stack_arn: The Amazon Resource Name (ARN) of a CloudFormation stack. You must specify either a ``CloudFormationStackARN`` or ``TagFilters`` .
            :param tag_filters: A set of tag filters (keys and values). Each tag filter specified must contain a key with values as optional. Each scaling plan can include up to 50 keys, and each key can include up to 20 values. Tags are part of the syntax that you use to specify the resources you want returned when configuring a scaling plan from the AWS Auto Scaling console. You do not need to specify valid tag filter values when you create a scaling plan with CloudFormation. The ``Key`` and ``Values`` properties can accept any value as long as the combination of values is unique across scaling plans. However, if you also want to use the AWS Auto Scaling console to edit the scaling plan, then you must specify valid values. You must specify either a ``CloudFormationStackARN`` or ``TagFilters`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_autoscalingplans as autoscalingplans
                
                application_source_property = autoscalingplans.CfnScalingPlan.ApplicationSourceProperty(
                    cloud_formation_stack_arn="cloudFormationStackArn",
                    tag_filters=[autoscalingplans.CfnScalingPlan.TagFilterProperty(
                        key="key",
                
                        # the properties below are optional
                        values=["values"]
                    )]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_formation_stack_arn is not None:
                self._values["cloud_formation_stack_arn"] = cloud_formation_stack_arn
            if tag_filters is not None:
                self._values["tag_filters"] = tag_filters

        @builtins.property
        def cloud_formation_stack_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of a CloudFormation stack.

            You must specify either a ``CloudFormationStackARN`` or ``TagFilters`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html#cfn-autoscalingplans-scalingplan-applicationsource-cloudformationstackarn
            '''
            result = self._values.get("cloud_formation_stack_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.TagFilterProperty", _IResolvable_da3f097b]]]]:
            '''A set of tag filters (keys and values).

            Each tag filter specified must contain a key with values as optional. Each scaling plan can include up to 50 keys, and each key can include up to 20 values.

            Tags are part of the syntax that you use to specify the resources you want returned when configuring a scaling plan from the AWS Auto Scaling console. You do not need to specify valid tag filter values when you create a scaling plan with CloudFormation. The ``Key`` and ``Values`` properties can accept any value as long as the combination of values is unique across scaling plans. However, if you also want to use the AWS Auto Scaling console to edit the scaling plan, then you must specify valid values.

            You must specify either a ``CloudFormationStackARN`` or ``TagFilters`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html#cfn-autoscalingplans-scalingplan-applicationsource-tagfilters
            '''
            result = self._values.get("tag_filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.TagFilterProperty", _IResolvable_da3f097b]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan.CustomizedLoadMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "namespace": "namespace",
            "statistic": "statistic",
            "dimensions": "dimensions",
            "unit": "unit",
        },
    )
    class CustomizedLoadMetricSpecificationProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            namespace: builtins.str,
            statistic: builtins.str,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnScalingPlan.MetricDimensionProperty", _IResolvable_da3f097b]]]] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``CustomizedLoadMetricSpecification`` is a subproperty of `ScalingInstruction <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html>`_ that specifies a customized load metric for predictive scaling to use with AWS Auto Scaling ( Auto Scaling Plans ).

            For predictive scaling to work with a customized load metric specification, AWS Auto Scaling needs access to the ``Sum`` and ``Average`` statistics that CloudWatch computes from metric data.

            When you choose a load metric, make sure that the required ``Sum`` and ``Average`` statistics for your metric are available in CloudWatch and that they provide relevant data for predictive scaling. The ``Sum`` statistic must represent the total load on the resource, and the ``Average`` statistic must represent the average load per capacity unit of the resource. For example, there is a metric that counts the number of requests processed by your Auto Scaling group. If the ``Sum`` statistic represents the total request count processed by the group, then the ``Average`` statistic for the specified metric must represent the average request count processed by each instance of the group.

            If you publish your own metrics, you can aggregate the data points at a given interval and then publish the aggregated data points to CloudWatch. Before AWS Auto Scaling generates the forecast, it sums up all the metric data points that occurred within each hour to match the granularity period that is used in the forecast (60 minutes).

            For information about terminology, available metrics, or how to publish new metrics, see `Amazon CloudWatch Concepts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html>`_ in the *Amazon CloudWatch User Guide* .

            After creating your scaling plan, you can use the AWS Auto Scaling console to visualize forecasts for the specified metric. For more information, see `View Scaling Information for a Resource <https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-create-scaling-plan.html#gs-view-resource>`_ in the *AWS Auto Scaling User Guide* .

            :param metric_name: The name of the metric.
            :param namespace: The namespace of the metric.
            :param statistic: The statistic of the metric. *Allowed Values* : ``Sum``
            :param dimensions: The dimensions of the metric. Conditional: If you published your metric with dimensions, you must specify the same dimensions in your customized load metric specification.
            :param unit: The unit of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_autoscalingplans as autoscalingplans
                
                customized_load_metric_specification_property = autoscalingplans.CfnScalingPlan.CustomizedLoadMetricSpecificationProperty(
                    metric_name="metricName",
                    namespace="namespace",
                    statistic="statistic",
                
                    # the properties below are optional
                    dimensions=[autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    unit="unit"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "metric_name": metric_name,
                "namespace": namespace,
                "statistic": statistic,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespace of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def statistic(self) -> builtins.str:
            '''The statistic of the metric.

            *Allowed Values* : ``Sum``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-statistic
            '''
            result = self._values.get("statistic")
            assert result is not None, "Required property 'statistic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.MetricDimensionProperty", _IResolvable_da3f097b]]]]:
            '''The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the same dimensions in your customized load metric specification.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.MetricDimensionProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomizedLoadMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan.CustomizedScalingMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "namespace": "namespace",
            "statistic": "statistic",
            "dimensions": "dimensions",
            "unit": "unit",
        },
    )
    class CustomizedScalingMetricSpecificationProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            namespace: builtins.str,
            statistic: builtins.str,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnScalingPlan.MetricDimensionProperty", _IResolvable_da3f097b]]]] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``CustomizedScalingMetricSpecification`` is a subproperty of `TargetTrackingConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html>`_ that specifies a customized scaling metric for a target tracking configuration to use with AWS Auto Scaling ( Auto Scaling Plans ).

            To create your customized scaling metric specification:

            - Add values for each required property from CloudWatch. You can use an existing metric, or a new metric that you create. To use your own metric, you must first publish the metric to CloudWatch. For more information, see `Publish Custom Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`_ in the *Amazon CloudWatch User Guide* .
            - Choose a metric that changes proportionally with capacity. The value of the metric should increase or decrease in inverse proportion to the number of capacity units. That is, the value of the metric should decrease when capacity increases.

            For information about terminology, available metrics, or how to publish new metrics, see `Amazon CloudWatch Concepts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html>`_ in the *Amazon CloudWatch User Guide* .

            :param metric_name: The name of the metric.
            :param namespace: The namespace of the metric.
            :param statistic: The statistic of the metric.
            :param dimensions: The dimensions of the metric. Conditional: If you published your metric with dimensions, you must specify the same dimensions in your customized scaling metric specification.
            :param unit: The unit of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_autoscalingplans as autoscalingplans
                
                customized_scaling_metric_specification_property = autoscalingplans.CfnScalingPlan.CustomizedScalingMetricSpecificationProperty(
                    metric_name="metricName",
                    namespace="namespace",
                    statistic="statistic",
                
                    # the properties below are optional
                    dimensions=[autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    unit="unit"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "metric_name": metric_name,
                "namespace": namespace,
                "statistic": statistic,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespace of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def statistic(self) -> builtins.str:
            '''The statistic of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-statistic
            '''
            result = self._values.get("statistic")
            assert result is not None, "Required property 'statistic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.MetricDimensionProperty", _IResolvable_da3f097b]]]]:
            '''The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the same dimensions in your customized scaling metric specification.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.MetricDimensionProperty", _IResolvable_da3f097b]]]], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomizedScalingMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''``MetricDimension`` is a subproperty of `CustomizedScalingMetricSpecification <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html>`_ that specifies a dimension for a customized metric to use with AWS Auto Scaling ( Auto Scaling Plans ). Dimensions are arbitrary name/value pairs that can be associated with a CloudWatch metric. Duplicate dimensions are not allowed.

            :param name: The name of the dimension.
            :param value: The value of the dimension.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_autoscalingplans as autoscalingplans
                
                metric_dimension_property = autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                    name="name",
                    value="value"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the dimension.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html#cfn-autoscalingplans-scalingplan-metricdimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the dimension.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html#cfn-autoscalingplans-scalingplan-metricdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan.PredefinedLoadMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "predefined_load_metric_type": "predefinedLoadMetricType",
            "resource_label": "resourceLabel",
        },
    )
    class PredefinedLoadMetricSpecificationProperty:
        def __init__(
            self,
            *,
            predefined_load_metric_type: builtins.str,
            resource_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``PredefinedLoadMetricSpecification`` is a subproperty of `ScalingInstruction <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html>`_ that specifies a predefined load metric for predictive scaling to use with AWS Auto Scaling ( Auto Scaling Plans ).

            After creating your scaling plan, you can use the AWS Auto Scaling console to visualize forecasts for the specified metric. For more information, see `View Scaling Information for a Resource <https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-create-scaling-plan.html#gs-view-resource>`_ in the *AWS Auto Scaling User Guide* .

            :param predefined_load_metric_type: The metric type.
            :param resource_label: Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ``ALBTargetGroupRequestCount`` and there is a target group for an Application Load Balancer attached to the Auto Scaling group. You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format is app///targetgroup//, where: - app// is the final portion of the load balancer ARN - targetgroup// is the final portion of the target group ARN. This is an example: app/EC2Co-EcsEl-1TKLTMITMM0EO/f37c06a68c1748aa/targetgroup/EC2Co-Defau-LDNM7Q3ZH1ZN/6d4ea56ca2d6a18d. To find the ARN for an Application Load Balancer, use the `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ API operation. To find the ARN for the target group, use the `DescribeTargetGroups <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html>`_ API operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_autoscalingplans as autoscalingplans
                
                predefined_load_metric_specification_property = autoscalingplans.CfnScalingPlan.PredefinedLoadMetricSpecificationProperty(
                    predefined_load_metric_type="predefinedLoadMetricType",
                
                    # the properties below are optional
                    resource_label="resourceLabel"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "predefined_load_metric_type": predefined_load_metric_type,
            }
            if resource_label is not None:
                self._values["resource_label"] = resource_label

        @builtins.property
        def predefined_load_metric_type(self) -> builtins.str:
            '''The metric type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedloadmetricspecification-predefinedloadmetrictype
            '''
            result = self._values.get("predefined_load_metric_type")
            assert result is not None, "Required property 'predefined_load_metric_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_label(self) -> typing.Optional[builtins.str]:
            '''Identifies the resource associated with the metric type.

            You can't specify a resource label unless the metric type is ``ALBTargetGroupRequestCount`` and there is a target group for an Application Load Balancer attached to the Auto Scaling group.

            You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format is app///targetgroup//, where:

            - app// is the final portion of the load balancer ARN
            - targetgroup// is the final portion of the target group ARN.

            This is an example: app/EC2Co-EcsEl-1TKLTMITMM0EO/f37c06a68c1748aa/targetgroup/EC2Co-Defau-LDNM7Q3ZH1ZN/6d4ea56ca2d6a18d.

            To find the ARN for an Application Load Balancer, use the `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ API operation. To find the ARN for the target group, use the `DescribeTargetGroups <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html>`_ API operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedloadmetricspecification-resourcelabel
            '''
            result = self._values.get("resource_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredefinedLoadMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan.PredefinedScalingMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "predefined_scaling_metric_type": "predefinedScalingMetricType",
            "resource_label": "resourceLabel",
        },
    )
    class PredefinedScalingMetricSpecificationProperty:
        def __init__(
            self,
            *,
            predefined_scaling_metric_type: builtins.str,
            resource_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``PredefinedScalingMetricSpecification`` is a subproperty of `TargetTrackingConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html>`_ that specifies a customized scaling metric for a target tracking configuration to use with AWS Auto Scaling ( Auto Scaling Plans ).

            :param predefined_scaling_metric_type: The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Auto Scaling groups, Spot Fleet requests, and ECS services.
            :param resource_label: Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet request, or ECS service. You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format is app///targetgroup//, where: - app// is the final portion of the load balancer ARN - targetgroup// is the final portion of the target group ARN. This is an example: app/EC2Co-EcsEl-1TKLTMITMM0EO/f37c06a68c1748aa/targetgroup/EC2Co-Defau-LDNM7Q3ZH1ZN/6d4ea56ca2d6a18d. To find the ARN for an Application Load Balancer, use the `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ API operation. To find the ARN for the target group, use the `DescribeTargetGroups <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html>`_ API operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_autoscalingplans as autoscalingplans
                
                predefined_scaling_metric_specification_property = autoscalingplans.CfnScalingPlan.PredefinedScalingMetricSpecificationProperty(
                    predefined_scaling_metric_type="predefinedScalingMetricType",
                
                    # the properties below are optional
                    resource_label="resourceLabel"
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "predefined_scaling_metric_type": predefined_scaling_metric_type,
            }
            if resource_label is not None:
                self._values["resource_label"] = resource_label

        @builtins.property
        def predefined_scaling_metric_type(self) -> builtins.str:
            '''The metric type.

            The ``ALBRequestCountPerTarget`` metric type applies only to Auto Scaling groups, Spot Fleet requests, and ECS services.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedscalingmetricspecification-predefinedscalingmetrictype
            '''
            result = self._values.get("predefined_scaling_metric_type")
            assert result is not None, "Required property 'predefined_scaling_metric_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_label(self) -> typing.Optional[builtins.str]:
            '''Identifies the resource associated with the metric type.

            You can't specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet request, or ECS service.

            You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format is app///targetgroup//, where:

            - app// is the final portion of the load balancer ARN
            - targetgroup// is the final portion of the target group ARN.

            This is an example: app/EC2Co-EcsEl-1TKLTMITMM0EO/f37c06a68c1748aa/targetgroup/EC2Co-Defau-LDNM7Q3ZH1ZN/6d4ea56ca2d6a18d.

            To find the ARN for an Application Load Balancer, use the `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ API operation. To find the ARN for the target group, use the `DescribeTargetGroups <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html>`_ API operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedscalingmetricspecification-resourcelabel
            '''
            result = self._values.get("resource_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredefinedScalingMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan.ScalingInstructionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_capacity": "maxCapacity",
            "min_capacity": "minCapacity",
            "resource_id": "resourceId",
            "scalable_dimension": "scalableDimension",
            "service_namespace": "serviceNamespace",
            "target_tracking_configurations": "targetTrackingConfigurations",
            "customized_load_metric_specification": "customizedLoadMetricSpecification",
            "disable_dynamic_scaling": "disableDynamicScaling",
            "predefined_load_metric_specification": "predefinedLoadMetricSpecification",
            "predictive_scaling_max_capacity_behavior": "predictiveScalingMaxCapacityBehavior",
            "predictive_scaling_max_capacity_buffer": "predictiveScalingMaxCapacityBuffer",
            "predictive_scaling_mode": "predictiveScalingMode",
            "scaling_policy_update_behavior": "scalingPolicyUpdateBehavior",
            "scheduled_action_buffer_time": "scheduledActionBufferTime",
        },
    )
    class ScalingInstructionProperty:
        def __init__(
            self,
            *,
            max_capacity: jsii.Number,
            min_capacity: jsii.Number,
            resource_id: builtins.str,
            scalable_dimension: builtins.str,
            service_namespace: builtins.str,
            target_tracking_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union["CfnScalingPlan.TargetTrackingConfigurationProperty", _IResolvable_da3f097b]]],
            customized_load_metric_specification: typing.Optional[typing.Union["CfnScalingPlan.CustomizedLoadMetricSpecificationProperty", _IResolvable_da3f097b]] = None,
            disable_dynamic_scaling: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            predefined_load_metric_specification: typing.Optional[typing.Union["CfnScalingPlan.PredefinedLoadMetricSpecificationProperty", _IResolvable_da3f097b]] = None,
            predictive_scaling_max_capacity_behavior: typing.Optional[builtins.str] = None,
            predictive_scaling_max_capacity_buffer: typing.Optional[jsii.Number] = None,
            predictive_scaling_mode: typing.Optional[builtins.str] = None,
            scaling_policy_update_behavior: typing.Optional[builtins.str] = None,
            scheduled_action_buffer_time: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``ScalingInstruction`` is a property of `ScalingPlan <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html>`_ that specifies the scaling instruction for a scalable resource in a scaling plan. Each scaling instruction applies to one resource.

            AWS Auto Scaling creates target tracking scaling policies based on the scaling instructions. Target tracking scaling policies adjust the capacity of your scalable resource as required to maintain resource utilization at the target value that you specified.

            AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling groups using a subset of properties, including the load metric, the scaling metric, the target value for the scaling metric, the predictive scaling mode (forecast and scale or forecast only), and the desired behavior when the forecast capacity exceeds the maximum capacity of the resource. With predictive scaling, AWS Auto Scaling generates forecasts with traffic predictions for the two days ahead and schedules scaling actions that proactively add and remove resource capacity to match the forecast.
            .. epigraph::

               We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to configure predictive scaling. At minimum, there must be 24 hours of historical data to generate a forecast. For more information, see `Best Practices for AWS Auto Scaling <https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-best-practices.html>`_ in the *AWS Auto Scaling User Guide* .

            :param max_capacity: The maximum capacity of the resource. The exception to this upper limit is if you specify a non-default setting for *PredictiveScalingMaxCapacityBehavior* .
            :param min_capacity: The minimum capacity of the resource.
            :param resource_id: The ID of the resource. This string consists of the resource type and unique identifier. - Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique identifier is the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` . - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` . - Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . - DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` . - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` . - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` .
            :param scalable_dimension: The scalable dimension associated with the resource. - ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto Scaling group. - ``ecs:service:DesiredCount`` - The desired task count of an ECS service. - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request. - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
            :param service_namespace: The namespace of the AWS service.
            :param target_tracking_configurations: The target tracking configurations (up to 10). Each of these structures must specify a unique scaling metric and a target value for the metric.
            :param customized_load_metric_specification: The customized load metric to use for predictive scaling. This property or a *PredefinedLoadMetricSpecification* is required when configuring predictive scaling, and cannot be used otherwise.
            :param disable_dynamic_scaling: Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based on the specified target tracking configurations. The default is enabled ( ``false`` ).
            :param predefined_load_metric_specification: The predefined load metric to use for predictive scaling. This property or a *CustomizedLoadMetricSpecification* is required when configuring predictive scaling, and cannot be used otherwise.
            :param predictive_scaling_max_capacity_behavior: Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity specified for the resource. The default value is ``SetForecastCapacityToMaxCapacity`` . The following are possible values: - ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource capacity higher than the maximum capacity. The maximum capacity is enforced as a hard limit. - ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling can scale resource capacity higher than the maximum capacity to equal but not exceed forecast capacity. - ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling can scale resource capacity higher than the maximum capacity by a specified buffer value. The intention is to give the target tracking scaling policy extra capacity if unexpected traffic occurs. Valid only when configuring predictive scaling.
            :param predictive_scaling_max_capacity_buffer: The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer. With a 10 percent buffer, if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55. Valid only when configuring predictive scaling. Required if *PredictiveScalingMaxCapacityBehavior* is set to ``SetMaxCapacityAboveForecastCapacity`` , and cannot be used otherwise. The range is 1-100.
            :param predictive_scaling_mode: The predictive scaling mode. The default value is ``ForecastAndScale`` . Otherwise, AWS Auto Scaling forecasts capacity but does not apply any scheduled scaling actions based on the capacity forecast.
            :param scaling_policy_update_behavior: Controls whether your scaling policies that are external to AWS Auto Scaling are deleted and new target tracking scaling policies created. The default value is ``KeepExternalPolicies`` . Valid only when configuring dynamic scaling.
            :param scheduled_action_buffer_time: The amount of time, in seconds, to buffer the run time of scheduled scaling actions when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and the buffer time is 5 minutes, then the run time of the corresponding scheduled scaling action will be 9:55 AM. The intention is to give resources time to be provisioned. For example, it can take a few minutes to launch an EC2 instance. The actual amount of time required depends on several factors, such as the size of the instance and whether there are startup scripts to complete. The value must be less than the forecast interval duration of 3600 seconds (60 minutes). The default is 300 seconds. Valid only when configuring predictive scaling.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_autoscalingplans as autoscalingplans
                
                scaling_instruction_property = autoscalingplans.CfnScalingPlan.ScalingInstructionProperty(
                    max_capacity=123,
                    min_capacity=123,
                    resource_id="resourceId",
                    scalable_dimension="scalableDimension",
                    service_namespace="serviceNamespace",
                    target_tracking_configurations=[autoscalingplans.CfnScalingPlan.TargetTrackingConfigurationProperty(
                        target_value=123,
                
                        # the properties below are optional
                        customized_scaling_metric_specification=autoscalingplans.CfnScalingPlan.CustomizedScalingMetricSpecificationProperty(
                            metric_name="metricName",
                            namespace="namespace",
                            statistic="statistic",
                
                            # the properties below are optional
                            dimensions=[autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            unit="unit"
                        ),
                        disable_scale_in=False,
                        estimated_instance_warmup=123,
                        predefined_scaling_metric_specification=autoscalingplans.CfnScalingPlan.PredefinedScalingMetricSpecificationProperty(
                            predefined_scaling_metric_type="predefinedScalingMetricType",
                
                            # the properties below are optional
                            resource_label="resourceLabel"
                        ),
                        scale_in_cooldown=123,
                        scale_out_cooldown=123
                    )],
                
                    # the properties below are optional
                    customized_load_metric_specification=autoscalingplans.CfnScalingPlan.CustomizedLoadMetricSpecificationProperty(
                        metric_name="metricName",
                        namespace="namespace",
                        statistic="statistic",
                
                        # the properties below are optional
                        dimensions=[autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        unit="unit"
                    ),
                    disable_dynamic_scaling=False,
                    predefined_load_metric_specification=autoscalingplans.CfnScalingPlan.PredefinedLoadMetricSpecificationProperty(
                        predefined_load_metric_type="predefinedLoadMetricType",
                
                        # the properties below are optional
                        resource_label="resourceLabel"
                    ),
                    predictive_scaling_max_capacity_behavior="predictiveScalingMaxCapacityBehavior",
                    predictive_scaling_max_capacity_buffer=123,
                    predictive_scaling_mode="predictiveScalingMode",
                    scaling_policy_update_behavior="scalingPolicyUpdateBehavior",
                    scheduled_action_buffer_time=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_capacity": max_capacity,
                "min_capacity": min_capacity,
                "resource_id": resource_id,
                "scalable_dimension": scalable_dimension,
                "service_namespace": service_namespace,
                "target_tracking_configurations": target_tracking_configurations,
            }
            if customized_load_metric_specification is not None:
                self._values["customized_load_metric_specification"] = customized_load_metric_specification
            if disable_dynamic_scaling is not None:
                self._values["disable_dynamic_scaling"] = disable_dynamic_scaling
            if predefined_load_metric_specification is not None:
                self._values["predefined_load_metric_specification"] = predefined_load_metric_specification
            if predictive_scaling_max_capacity_behavior is not None:
                self._values["predictive_scaling_max_capacity_behavior"] = predictive_scaling_max_capacity_behavior
            if predictive_scaling_max_capacity_buffer is not None:
                self._values["predictive_scaling_max_capacity_buffer"] = predictive_scaling_max_capacity_buffer
            if predictive_scaling_mode is not None:
                self._values["predictive_scaling_mode"] = predictive_scaling_mode
            if scaling_policy_update_behavior is not None:
                self._values["scaling_policy_update_behavior"] = scaling_policy_update_behavior
            if scheduled_action_buffer_time is not None:
                self._values["scheduled_action_buffer_time"] = scheduled_action_buffer_time

        @builtins.property
        def max_capacity(self) -> jsii.Number:
            '''The maximum capacity of the resource.

            The exception to this upper limit is if you specify a non-default setting for *PredictiveScalingMaxCapacityBehavior* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-maxcapacity
            '''
            result = self._values.get("max_capacity")
            assert result is not None, "Required property 'max_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_capacity(self) -> jsii.Number:
            '''The minimum capacity of the resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-mincapacity
            '''
            result = self._values.get("min_capacity")
            assert result is not None, "Required property 'min_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def resource_id(self) -> builtins.str:
            '''The ID of the resource. This string consists of the resource type and unique identifier.

            - Auto Scaling group - The resource type is ``autoScalingGroup`` and the unique identifier is the name of the Auto Scaling group. Example: ``autoScalingGroup/my-asg`` .
            - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/default/sample-webapp`` .
            - Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .
            - DynamoDB table - The resource type is ``table`` and the unique identifier is the resource ID. Example: ``table/my-table`` .
            - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the resource ID. Example: ``table/my-table/index/my-table-index`` .
            - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-resourceid
            '''
            result = self._values.get("resource_id")
            assert result is not None, "Required property 'resource_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scalable_dimension(self) -> builtins.str:
            '''The scalable dimension associated with the resource.

            - ``autoscaling:autoScalingGroup:DesiredCapacity`` - The desired capacity of an Auto Scaling group.
            - ``ecs:service:DesiredCount`` - The desired task count of an ECS service.
            - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.
            - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
            - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
            - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
            - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
            - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-scalabledimension
            '''
            result = self._values.get("scalable_dimension")
            assert result is not None, "Required property 'scalable_dimension' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_namespace(self) -> builtins.str:
            '''The namespace of the AWS service.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-servicenamespace
            '''
            result = self._values.get("service_namespace")
            assert result is not None, "Required property 'service_namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_tracking_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.TargetTrackingConfigurationProperty", _IResolvable_da3f097b]]]:
            '''The target tracking configurations (up to 10).

            Each of these structures must specify a unique scaling metric and a target value for the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-targettrackingconfigurations
            '''
            result = self._values.get("target_tracking_configurations")
            assert result is not None, "Required property 'target_tracking_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnScalingPlan.TargetTrackingConfigurationProperty", _IResolvable_da3f097b]]], result)

        @builtins.property
        def customized_load_metric_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnScalingPlan.CustomizedLoadMetricSpecificationProperty", _IResolvable_da3f097b]]:
            '''The customized load metric to use for predictive scaling.

            This property or a *PredefinedLoadMetricSpecification* is required when configuring predictive scaling, and cannot be used otherwise.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-customizedloadmetricspecification
            '''
            result = self._values.get("customized_load_metric_specification")
            return typing.cast(typing.Optional[typing.Union["CfnScalingPlan.CustomizedLoadMetricSpecificationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def disable_dynamic_scaling(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Controls whether dynamic scaling by AWS Auto Scaling is disabled.

            When dynamic scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based on the specified target tracking configurations.

            The default is enabled ( ``false`` ).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-disabledynamicscaling
            '''
            result = self._values.get("disable_dynamic_scaling")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def predefined_load_metric_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnScalingPlan.PredefinedLoadMetricSpecificationProperty", _IResolvable_da3f097b]]:
            '''The predefined load metric to use for predictive scaling.

            This property or a *CustomizedLoadMetricSpecification* is required when configuring predictive scaling, and cannot be used otherwise.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predefinedloadmetricspecification
            '''
            result = self._values.get("predefined_load_metric_specification")
            return typing.cast(typing.Optional[typing.Union["CfnScalingPlan.PredefinedLoadMetricSpecificationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def predictive_scaling_max_capacity_behavior(
            self,
        ) -> typing.Optional[builtins.str]:
            '''Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity specified for the resource.

            The default value is ``SetForecastCapacityToMaxCapacity`` .

            The following are possible values:

            - ``SetForecastCapacityToMaxCapacity`` - AWS Auto Scaling cannot scale resource capacity higher than the maximum capacity. The maximum capacity is enforced as a hard limit.
            - ``SetMaxCapacityToForecastCapacity`` - AWS Auto Scaling can scale resource capacity higher than the maximum capacity to equal but not exceed forecast capacity.
            - ``SetMaxCapacityAboveForecastCapacity`` - AWS Auto Scaling can scale resource capacity higher than the maximum capacity by a specified buffer value. The intention is to give the target tracking scaling policy extra capacity if unexpected traffic occurs.

            Valid only when configuring predictive scaling.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predictivescalingmaxcapacitybehavior
            '''
            result = self._values.get("predictive_scaling_max_capacity_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def predictive_scaling_max_capacity_buffer(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity.

            The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer. With a 10 percent buffer, if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.

            Valid only when configuring predictive scaling. Required if *PredictiveScalingMaxCapacityBehavior* is set to ``SetMaxCapacityAboveForecastCapacity`` , and cannot be used otherwise.

            The range is 1-100.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predictivescalingmaxcapacitybuffer
            '''
            result = self._values.get("predictive_scaling_max_capacity_buffer")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def predictive_scaling_mode(self) -> typing.Optional[builtins.str]:
            '''The predictive scaling mode.

            The default value is ``ForecastAndScale`` . Otherwise, AWS Auto Scaling forecasts capacity but does not apply any scheduled scaling actions based on the capacity forecast.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predictivescalingmode
            '''
            result = self._values.get("predictive_scaling_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scaling_policy_update_behavior(self) -> typing.Optional[builtins.str]:
            '''Controls whether your scaling policies that are external to AWS Auto Scaling are deleted and new target tracking scaling policies created.

            The default value is ``KeepExternalPolicies`` .

            Valid only when configuring dynamic scaling.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-scalingpolicyupdatebehavior
            '''
            result = self._values.get("scaling_policy_update_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scheduled_action_buffer_time(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, to buffer the run time of scheduled scaling actions when scaling out.

            For example, if the forecast says to add capacity at 10:00 AM, and the buffer time is 5 minutes, then the run time of the corresponding scheduled scaling action will be 9:55 AM. The intention is to give resources time to be provisioned. For example, it can take a few minutes to launch an EC2 instance. The actual amount of time required depends on several factors, such as the size of the instance and whether there are startup scripts to complete.

            The value must be less than the forecast interval duration of 3600 seconds (60 minutes). The default is 300 seconds.

            Valid only when configuring predictive scaling.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-scheduledactionbuffertime
            '''
            result = self._values.get("scheduled_action_buffer_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingInstructionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan.TagFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TagFilterProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''``TagFilter`` is a subproperty of `ApplicationSource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html>`_ that specifies a tag for an application source to use with AWS Auto Scaling ( Auto Scaling Plans ).

            :param key: The tag key.
            :param values: The tag values (0 to 20).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_autoscalingplans as autoscalingplans
                
                tag_filter_property = autoscalingplans.CfnScalingPlan.TagFilterProperty(
                    key="key",
                
                    # the properties below are optional
                    values=["values"]
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
            }
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def key(self) -> builtins.str:
            '''The tag key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html#cfn-autoscalingplans-scalingplan-tagfilter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The tag values (0 to 20).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html#cfn-autoscalingplans-scalingplan-tagfilter-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlan.TargetTrackingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_value": "targetValue",
            "customized_scaling_metric_specification": "customizedScalingMetricSpecification",
            "disable_scale_in": "disableScaleIn",
            "estimated_instance_warmup": "estimatedInstanceWarmup",
            "predefined_scaling_metric_specification": "predefinedScalingMetricSpecification",
            "scale_in_cooldown": "scaleInCooldown",
            "scale_out_cooldown": "scaleOutCooldown",
        },
    )
    class TargetTrackingConfigurationProperty:
        def __init__(
            self,
            *,
            target_value: jsii.Number,
            customized_scaling_metric_specification: typing.Optional[typing.Union["CfnScalingPlan.CustomizedScalingMetricSpecificationProperty", _IResolvable_da3f097b]] = None,
            disable_scale_in: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            estimated_instance_warmup: typing.Optional[jsii.Number] = None,
            predefined_scaling_metric_specification: typing.Optional[typing.Union["CfnScalingPlan.PredefinedScalingMetricSpecificationProperty", _IResolvable_da3f097b]] = None,
            scale_in_cooldown: typing.Optional[jsii.Number] = None,
            scale_out_cooldown: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``TargetTrackingConfiguration`` is a subproperty of `ScalingInstruction <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html>`_ that specifies a target tracking configuration to use with AWS Auto Scaling ( Auto Scaling Plans ).

            :param target_value: The target value for the metric. Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360.
            :param customized_scaling_metric_specification: A customized metric. You can specify either a predefined metric or a customized metric.
            :param disable_scale_in: Indicates whether scale in by the target tracking scaling policy is disabled. If the value is ``true`` , scale in is disabled and the target tracking scaling policy doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable resource. The default value is ``false`` .
            :param estimated_instance_warmup: The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.
            :param predefined_scaling_metric_specification: A predefined metric. You can specify either a predefined metric or a customized metric.
            :param scale_in_cooldown: The amount of time, in seconds, after a scale-in activity completes before another scale in activity can start. This value is not used if the scalable resource is an Auto Scaling group.
            :param scale_out_cooldown: The amount of time, in seconds, after a scale-out activity completes before another scale-out activity can start. This value is not used if the scalable resource is an Auto Scaling group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_autoscalingplans as autoscalingplans
                
                target_tracking_configuration_property = autoscalingplans.CfnScalingPlan.TargetTrackingConfigurationProperty(
                    target_value=123,
                
                    # the properties below are optional
                    customized_scaling_metric_specification=autoscalingplans.CfnScalingPlan.CustomizedScalingMetricSpecificationProperty(
                        metric_name="metricName",
                        namespace="namespace",
                        statistic="statistic",
                
                        # the properties below are optional
                        dimensions=[autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        unit="unit"
                    ),
                    disable_scale_in=False,
                    estimated_instance_warmup=123,
                    predefined_scaling_metric_specification=autoscalingplans.CfnScalingPlan.PredefinedScalingMetricSpecificationProperty(
                        predefined_scaling_metric_type="predefinedScalingMetricType",
                
                        # the properties below are optional
                        resource_label="resourceLabel"
                    ),
                    scale_in_cooldown=123,
                    scale_out_cooldown=123
                )
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "target_value": target_value,
            }
            if customized_scaling_metric_specification is not None:
                self._values["customized_scaling_metric_specification"] = customized_scaling_metric_specification
            if disable_scale_in is not None:
                self._values["disable_scale_in"] = disable_scale_in
            if estimated_instance_warmup is not None:
                self._values["estimated_instance_warmup"] = estimated_instance_warmup
            if predefined_scaling_metric_specification is not None:
                self._values["predefined_scaling_metric_specification"] = predefined_scaling_metric_specification
            if scale_in_cooldown is not None:
                self._values["scale_in_cooldown"] = scale_in_cooldown
            if scale_out_cooldown is not None:
                self._values["scale_out_cooldown"] = scale_out_cooldown

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''The target value for the metric.

            Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def customized_scaling_metric_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnScalingPlan.CustomizedScalingMetricSpecificationProperty", _IResolvable_da3f097b]]:
            '''A customized metric.

            You can specify either a predefined metric or a customized metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-customizedscalingmetricspecification
            '''
            result = self._values.get("customized_scaling_metric_specification")
            return typing.cast(typing.Optional[typing.Union["CfnScalingPlan.CustomizedScalingMetricSpecificationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def disable_scale_in(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether scale in by the target tracking scaling policy is disabled.

            If the value is ``true`` , scale in is disabled and the target tracking scaling policy doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable resource.

            The default value is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-disablescalein
            '''
            result = self._values.get("disable_scale_in")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def estimated_instance_warmup(self) -> typing.Optional[jsii.Number]:
            '''The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics.

            This value is used only if the resource is an Auto Scaling group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-estimatedinstancewarmup
            '''
            result = self._values.get("estimated_instance_warmup")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def predefined_scaling_metric_specification(
            self,
        ) -> typing.Optional[typing.Union["CfnScalingPlan.PredefinedScalingMetricSpecificationProperty", _IResolvable_da3f097b]]:
            '''A predefined metric.

            You can specify either a predefined metric or a customized metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-predefinedscalingmetricspecification
            '''
            result = self._values.get("predefined_scaling_metric_specification")
            return typing.cast(typing.Optional[typing.Union["CfnScalingPlan.PredefinedScalingMetricSpecificationProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def scale_in_cooldown(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, after a scale-in activity completes before another scale in activity can start.

            This value is not used if the scalable resource is an Auto Scaling group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-scaleincooldown
            '''
            result = self._values.get("scale_in_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scale_out_cooldown(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, after a scale-out activity completes before another scale-out activity can start.

            This value is not used if the scalable resource is an Auto Scaling group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-scaleoutcooldown
            '''
            result = self._values.get("scale_out_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_autoscalingplans.CfnScalingPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_source": "applicationSource",
        "scaling_instructions": "scalingInstructions",
    },
)
class CfnScalingPlanProps:
    def __init__(
        self,
        *,
        application_source: typing.Union[CfnScalingPlan.ApplicationSourceProperty, _IResolvable_da3f097b],
        scaling_instructions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[CfnScalingPlan.ScalingInstructionProperty, _IResolvable_da3f097b]]],
    ) -> None:
        '''Properties for defining a ``CfnScalingPlan``.

        :param application_source: A CloudFormation stack or a set of tags. You can create one scaling plan per application source. The ``ApplicationSource`` property must be present to ensure interoperability with the AWS Auto Scaling console.
        :param scaling_instructions: The scaling instructions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_autoscalingplans as autoscalingplans
            
            cfn_scaling_plan_props = autoscalingplans.CfnScalingPlanProps(
                application_source=autoscalingplans.CfnScalingPlan.ApplicationSourceProperty(
                    cloud_formation_stack_arn="cloudFormationStackArn",
                    tag_filters=[autoscalingplans.CfnScalingPlan.TagFilterProperty(
                        key="key",
            
                        # the properties below are optional
                        values=["values"]
                    )]
                ),
                scaling_instructions=[autoscalingplans.CfnScalingPlan.ScalingInstructionProperty(
                    max_capacity=123,
                    min_capacity=123,
                    resource_id="resourceId",
                    scalable_dimension="scalableDimension",
                    service_namespace="serviceNamespace",
                    target_tracking_configurations=[autoscalingplans.CfnScalingPlan.TargetTrackingConfigurationProperty(
                        target_value=123,
            
                        # the properties below are optional
                        customized_scaling_metric_specification=autoscalingplans.CfnScalingPlan.CustomizedScalingMetricSpecificationProperty(
                            metric_name="metricName",
                            namespace="namespace",
                            statistic="statistic",
            
                            # the properties below are optional
                            dimensions=[autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            unit="unit"
                        ),
                        disable_scale_in=False,
                        estimated_instance_warmup=123,
                        predefined_scaling_metric_specification=autoscalingplans.CfnScalingPlan.PredefinedScalingMetricSpecificationProperty(
                            predefined_scaling_metric_type="predefinedScalingMetricType",
            
                            # the properties below are optional
                            resource_label="resourceLabel"
                        ),
                        scale_in_cooldown=123,
                        scale_out_cooldown=123
                    )],
            
                    # the properties below are optional
                    customized_load_metric_specification=autoscalingplans.CfnScalingPlan.CustomizedLoadMetricSpecificationProperty(
                        metric_name="metricName",
                        namespace="namespace",
                        statistic="statistic",
            
                        # the properties below are optional
                        dimensions=[autoscalingplans.CfnScalingPlan.MetricDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        unit="unit"
                    ),
                    disable_dynamic_scaling=False,
                    predefined_load_metric_specification=autoscalingplans.CfnScalingPlan.PredefinedLoadMetricSpecificationProperty(
                        predefined_load_metric_type="predefinedLoadMetricType",
            
                        # the properties below are optional
                        resource_label="resourceLabel"
                    ),
                    predictive_scaling_max_capacity_behavior="predictiveScalingMaxCapacityBehavior",
                    predictive_scaling_max_capacity_buffer=123,
                    predictive_scaling_mode="predictiveScalingMode",
                    scaling_policy_update_behavior="scalingPolicyUpdateBehavior",
                    scheduled_action_buffer_time=123
                )]
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_source": application_source,
            "scaling_instructions": scaling_instructions,
        }

    @builtins.property
    def application_source(
        self,
    ) -> typing.Union[CfnScalingPlan.ApplicationSourceProperty, _IResolvable_da3f097b]:
        '''A CloudFormation stack or a set of tags.

        You can create one scaling plan per application source. The ``ApplicationSource`` property must be present to ensure interoperability with the AWS Auto Scaling console.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-applicationsource
        '''
        result = self._values.get("application_source")
        assert result is not None, "Required property 'application_source' is missing"
        return typing.cast(typing.Union[CfnScalingPlan.ApplicationSourceProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def scaling_instructions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnScalingPlan.ScalingInstructionProperty, _IResolvable_da3f097b]]]:
        '''The scaling instructions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-scalinginstructions
        '''
        result = self._values.get("scaling_instructions")
        assert result is not None, "Required property 'scaling_instructions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnScalingPlan.ScalingInstructionProperty, _IResolvable_da3f097b]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScalingPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnScalingPlan",
    "CfnScalingPlanProps",
]

publication.publish()
