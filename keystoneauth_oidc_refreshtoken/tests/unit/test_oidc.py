# coding=utf-8

# Copyright 2017 JOSÉ JOAQUÍN ESCOBAR GÓMEZ
# File: test_oidc.py
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

import uuid
from keystoneauth1.tests.unit.identity import test_identity_v3_oidc
from keystoneauth1.tests.unit import utils

from keystoneauth_oidc_refreshtoken.tests.unit import oidc_fixtures
from keystoneauth_oidc_refreshtoken import plugin as oidc


class OIDCRefreshTokenTests(test_identity_v3_oidc.BaseOIDCTests,
                            utils.TestCase):
    def setUp(self):
        super(OIDCRefreshTokenTests, self).setUp()

        self.GRANT_TYPE = 'refresh_token'

        self.AUTHORIZATION_ENDPOINT = 'https://localhost:8020/oidc/authn'

        self.plugin = oidc.OidcRefreshToken(
            self.AUTH_URL,
            self.IDENTITY_PROVIDER,
            self.PROTOCOL,
            client_id=self.CLIENT_ID,
            client_secret=self.CLIENT_SECRET,
            access_token_endpoint=self.ACCESS_TOKEN_ENDPOINT,
            project_name = self.PROJECT_NAME)
