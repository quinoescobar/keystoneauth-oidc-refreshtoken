   # Copyright 2017 JOSÉ JOAQUÍN ESCOBAR GÓMEZ
   # File: loading.py
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

from keystoneauth1 import exceptions
from keystoneauth1 import loading
from keystoneauth1.loading._plugins.identity import v3
from keystoneauth-oidc-refreshtoken import plugin

class OpenIDConnectRefreshToken(v3._OpenIDConnectBase):

    @property
    def plugin_class(self):
        return identity.V3OidcRefreshToken

    def get_options(self):
        options = super(OpenIDConnectRefreshToken, self).get_options()

        options.extend([
            loading.Opt('refresh_token', required=True,
                        help='OAuth 2.0 Refresh Token')
        ])
        return options