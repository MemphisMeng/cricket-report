'''
# Actions for AWS Elastic Load Balancing V2

This package contains integration actions for ELBv2. See the README of the `@aws-cdk/aws-elasticloadbalancingv2` library.

## Cognito

ELB allows for requests to be authenticated against a Cognito user pool using
the `AuthenticateCognitoAction`. For details on the setup's requirements,
read [Prepare to use Amazon
Cognito](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html#cognito-requirements).
Here's an example:

[Example of using AuthenticateCognitoAction](test/integ.cognito.lit.ts)

> NOTE: this example seems incomplete, I was not able to get the redirect back to the
> Load Balancer after authentication working. Would love some pointers on what a full working
> setup actually looks like!
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

from .. import Duration as _Duration_4839e8c3
from ..aws_cognito import (
    IUserPool as _IUserPool_1f1029e2,
    IUserPoolClient as _IUserPoolClient_75623ba4,
    IUserPoolDomain as _IUserPoolDomain_72b6a019,
)
from ..aws_elasticloadbalancingv2 import (
    ListenerAction as _ListenerAction_1aa94a29,
    UnauthenticatedAction as _UnauthenticatedAction_161c1c21,
)


class AuthenticateCognitoAction(
    _ListenerAction_1aa94a29,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_actions.AuthenticateCognitoAction",
):
    '''A Listener Action to authenticate with Cognito.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_elasticloadbalancingv2 as elbv2
        from aws_cdk import aws_elasticloadbalancingv2_actions as elasticloadbalancingv2_actions
        
        # listener_action: elbv2.ListenerAction
        # secret_value: cdk.SecretValue
        
        authenticate_cognito_action = elasticloadbalancingv2_actions.AuthenticateCognitoAction.authenticate_oidc(
            authorization_endpoint="authorizationEndpoint",
            client_id="clientId",
            client_secret=secret_value,
            issuer="issuer",
            next=listener_action,
            token_endpoint="tokenEndpoint",
            user_info_endpoint="userInfoEndpoint",
        
            # the properties below are optional
            authentication_request_extra_params={
                "authentication_request_extra_params_key": "authenticationRequestExtraParams"
            },
            on_unauthenticated_request=elbv2.UnauthenticatedAction.DENY,
            scope="scope",
            session_cookie_name="sessionCookieName",
            session_timeout=cdk.Duration.minutes(30)
        )
    '''

    def __init__(
        self,
        *,
        next: _ListenerAction_1aa94a29,
        user_pool: _IUserPool_1f1029e2,
        user_pool_client: _IUserPoolClient_75623ba4,
        user_pool_domain: _IUserPoolDomain_72b6a019,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[_UnauthenticatedAction_161c1c21] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Authenticate using an identity provide (IdP) that is compliant with OpenID Connect (OIDC).

        :param next: What action to execute next. Multiple actions form a linked chain; the chain must always terminate in a (weighted)forward, fixedResponse or redirect action.
        :param user_pool: The Amazon Cognito user pool.
        :param user_pool_client: The Amazon Cognito user pool client.
        :param user_pool_domain: The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        :param authentication_request_extra_params: The query parameters (up to 10) to include in the redirect request to the authorization endpoint. Default: - No extra parameters
        :param on_unauthenticated_request: The behavior if the user is not authenticated. Default: UnauthenticatedAction.AUTHENTICATE
        :param scope: The set of user claims to be requested from the IdP. To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP. Default: "openid"
        :param session_cookie_name: The name of the cookie used to maintain session information. Default: "AWSELBAuthSessionCookie"
        :param session_timeout: The maximum duration of the authentication session. Default: Duration.days(7)
        '''
        options = AuthenticateCognitoActionProps(
            next=next,
            user_pool=user_pool,
            user_pool_client=user_pool_client,
            user_pool_domain=user_pool_domain,
            authentication_request_extra_params=authentication_request_extra_params,
            on_unauthenticated_request=on_unauthenticated_request,
            scope=scope,
            session_cookie_name=session_cookie_name,
            session_timeout=session_timeout,
        )

        jsii.create(self.__class__, self, [options])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_actions.AuthenticateCognitoActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "next": "next",
        "user_pool": "userPool",
        "user_pool_client": "userPoolClient",
        "user_pool_domain": "userPoolDomain",
        "authentication_request_extra_params": "authenticationRequestExtraParams",
        "on_unauthenticated_request": "onUnauthenticatedRequest",
        "scope": "scope",
        "session_cookie_name": "sessionCookieName",
        "session_timeout": "sessionTimeout",
    },
)
class AuthenticateCognitoActionProps:
    def __init__(
        self,
        *,
        next: _ListenerAction_1aa94a29,
        user_pool: _IUserPool_1f1029e2,
        user_pool_client: _IUserPoolClient_75623ba4,
        user_pool_domain: _IUserPoolDomain_72b6a019,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[_UnauthenticatedAction_161c1c21] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for AuthenticateCognitoAction.

        :param next: What action to execute next. Multiple actions form a linked chain; the chain must always terminate in a (weighted)forward, fixedResponse or redirect action.
        :param user_pool: The Amazon Cognito user pool.
        :param user_pool_client: The Amazon Cognito user pool client.
        :param user_pool_domain: The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        :param authentication_request_extra_params: The query parameters (up to 10) to include in the redirect request to the authorization endpoint. Default: - No extra parameters
        :param on_unauthenticated_request: The behavior if the user is not authenticated. Default: UnauthenticatedAction.AUTHENTICATE
        :param scope: The set of user claims to be requested from the IdP. To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP. Default: "openid"
        :param session_cookie_name: The name of the cookie used to maintain session information. Default: "AWSELBAuthSessionCookie"
        :param session_timeout: The maximum duration of the authentication session. Default: Duration.days(7)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cognito as cognito
            from aws_cdk import aws_elasticloadbalancingv2 as elbv2
            from aws_cdk import aws_elasticloadbalancingv2_actions as elasticloadbalancingv2_actions
            
            # listener_action: elbv2.ListenerAction
            # user_pool: cognito.UserPool
            # user_pool_client: cognito.UserPoolClient
            # user_pool_domain: cognito.UserPoolDomain
            
            authenticate_cognito_action_props = elasticloadbalancingv2_actions.AuthenticateCognitoActionProps(
                next=listener_action,
                user_pool=user_pool,
                user_pool_client=user_pool_client,
                user_pool_domain=user_pool_domain,
            
                # the properties below are optional
                authentication_request_extra_params={
                    "authentication_request_extra_params_key": "authenticationRequestExtraParams"
                },
                on_unauthenticated_request=elbv2.UnauthenticatedAction.DENY,
                scope="scope",
                session_cookie_name="sessionCookieName",
                session_timeout=cdk.Duration.minutes(30)
            )
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "next": next,
            "user_pool": user_pool,
            "user_pool_client": user_pool_client,
            "user_pool_domain": user_pool_domain,
        }
        if authentication_request_extra_params is not None:
            self._values["authentication_request_extra_params"] = authentication_request_extra_params
        if on_unauthenticated_request is not None:
            self._values["on_unauthenticated_request"] = on_unauthenticated_request
        if scope is not None:
            self._values["scope"] = scope
        if session_cookie_name is not None:
            self._values["session_cookie_name"] = session_cookie_name
        if session_timeout is not None:
            self._values["session_timeout"] = session_timeout

    @builtins.property
    def next(self) -> _ListenerAction_1aa94a29:
        '''What action to execute next.

        Multiple actions form a linked chain; the chain must always terminate in a
        (weighted)forward, fixedResponse or redirect action.
        '''
        result = self._values.get("next")
        assert result is not None, "Required property 'next' is missing"
        return typing.cast(_ListenerAction_1aa94a29, result)

    @builtins.property
    def user_pool(self) -> _IUserPool_1f1029e2:
        '''The Amazon Cognito user pool.'''
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_IUserPool_1f1029e2, result)

    @builtins.property
    def user_pool_client(self) -> _IUserPoolClient_75623ba4:
        '''The Amazon Cognito user pool client.'''
        result = self._values.get("user_pool_client")
        assert result is not None, "Required property 'user_pool_client' is missing"
        return typing.cast(_IUserPoolClient_75623ba4, result)

    @builtins.property
    def user_pool_domain(self) -> _IUserPoolDomain_72b6a019:
        '''The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.'''
        result = self._values.get("user_pool_domain")
        assert result is not None, "Required property 'user_pool_domain' is missing"
        return typing.cast(_IUserPoolDomain_72b6a019, result)

    @builtins.property
    def authentication_request_extra_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

        :default: - No extra parameters
        '''
        result = self._values.get("authentication_request_extra_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def on_unauthenticated_request(
        self,
    ) -> typing.Optional[_UnauthenticatedAction_161c1c21]:
        '''The behavior if the user is not authenticated.

        :default: UnauthenticatedAction.AUTHENTICATE
        '''
        result = self._values.get("on_unauthenticated_request")
        return typing.cast(typing.Optional[_UnauthenticatedAction_161c1c21], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''The set of user claims to be requested from the IdP.

        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

        :default: "openid"
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_cookie_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cookie used to maintain session information.

        :default: "AWSELBAuthSessionCookie"
        '''
        result = self._values.get("session_cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum duration of the authentication session.

        :default: Duration.days(7)
        '''
        result = self._values.get("session_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthenticateCognitoActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthenticateCognitoAction",
    "AuthenticateCognitoActionProps",
]

publication.publish()
