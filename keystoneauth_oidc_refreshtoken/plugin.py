# coding=utf-8

# Copyright 2017 JOSE JOAQUIN ESCOBAR GOMEZ
# File: plugin.py
# Description:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from keystoneauth1 import _utils as utils
from keystoneauth1 import access
from keystoneauth1.exceptions import oidc as exceptions
from keystoneauth1.identity.v3 import oidc
from positional import positional

# from keystoneauth_oidc_refreshtoken import exceptions


_logger = utils.get_logger(__name__)


class OidcRefreshToken(oidc._OidcBase):
    """Access Token Procurement Through Refresh Token Implementation."""

    grant_type = "refresh_token"

    @positional(4)
    def __init__(self, auth_url, identity_provider, protocol,
                 client_id, client_secret,
                 access_token_endpoint=None,
                 discovery_endpoint=None,
                 access_token_type='access_token',
                 refresh_token=None,
                 **kwargs):
        """The OpenID Refresh Token plugin, It expects the following.

        :param auth_url: URL of the Identity Service
        :type auth_url: string

        :param identity_provider: Name of the Identity Provider the client
                                  will authenticate against
        :type identity_provider: string

        :param protocol: Protocol name as configured at keystone
        :type protocol: string

        :param client_id: OAuth 2.0 Client ID
        :type client_id: string

        :param client_secret: OAuth 2.0 Client Secret
        :type client_secret: string

        :param access_token_endpoint: OpenID Connect Provider Token Endpoint,
                                      for example:
                                      https://localhost:8020/oidc/OP/token
                                      Note that if a discovery document is
                                      provided this value will override
                                      the discovered one.
        :type access_token_endpoint: string

        :param refresh_token: OpenID Connect Refresh Token
        :type refresh_token: string
        """
        super(OidcRefreshToken, self).__init__(
            auth_url=auth_url,
            identity_provider=identity_provider,
            protocol=protocol,
            client_id=client_id,
            client_secret=client_secret,
            access_token_endpoint=access_token_endpoint,
            discovery_endpoint=discovery_endpoint,
            access_token_type=access_token_type,
            **kwargs)
        self.refresh_token = refresh_token

    def get_payload(self, session):
        """Get an authorization grant for "refresh_token" grant type.

        :param session: a session object to send out HTTP requests.
        :type session: keystoneauth1.session.Session

        :returns: A dictionary containing the payload to be exchanged
        :rtype: dict
        """
        payload = {'refresh_token': self.refresh_token,
                   'grant_type': self.grant_type}
        return payload

    def get_unscoped_auth_ref(self, session):
        """Authenticate with OpenID Connect and get back the access token.

        Exchange the refresh token to get a new access token issued by the
        authentication server.

        :param session: a session object to send out HTTP requests.
        :type session: keystoneclient.session.Session

        :returns: a token data representation
        :rtype: :py:class:`keystoneauth1.access.AccessInfoV3`
        """
        discovery = self._get_discovery_document(session)
        grant_types = discovery.get("grant_types_supported")
        if (grant_types and
                self.grant_type is not None and
                self.grant_type not in grant_types):
            raise exceptions.OidcPluginNotSupported()

        payload = self.get_payload(session)
        access_token = self._get_access_token(session, payload)
        response = self._get_keystone_token(session, access_token)
        return access.create(resp=response)
