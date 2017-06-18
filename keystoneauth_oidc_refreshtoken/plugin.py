   # Copyright 2017 JOSÉ JOAQUÍN ESCOBAR GÓMEZ
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

from keystoneauth1.identity.v3 import oidc
from keystoneauth1 import access
from positional import positional

from keystoneauth_oidc_refreshtoken import exceptions


class OidcRefreshToken(oidc_OidcBase):
    """ SOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXT """

    grant_type = "refresh_token"

    @positional(4)
    def __init__(self, auth_url, identity_provider, protocol,
                 client_id,client_secret,
                 access_token_endpoint,
                 refresh_token=None,**kwargs):
        """ SOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXT """
        super(OidcRefreshToken, self).__init__(
        auth_url,
        identity_provider,
        protocol,
        client_id=client_id,
        client_secret=client_secret,
        access_token_endpoint=access_token_endpoint,
        access_token_type='access_token',
        **kwargs)
        self.refresh_token = refresh_token

    def get_payload(self, session):
        """ SOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXT """
        payload = {
                   'refresh_token': self.refresh_token,
                   'grant_type': self.grant_type
                   }
        return payload

    def get_unscoped_auth_ref(self, session):
        """ SOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXTSOME TEXT """

        payload = self.get_payload(session)

        access_token = self._get_access_token(session,payload)

        response = self._get_keystone_token(session, access_token)

        return access.create(resp=response)
