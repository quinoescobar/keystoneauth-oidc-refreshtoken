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
# import mock
from six.moves import urllib

from keystoneauth_oidc_refreshtoken import plugin as oidc
from keystoneauth_oidc_refreshtoken.tests.unit import oidc_fixtures


class OIDCRefreshTokenTests(test_identity_v3_oidc.BaseOIDCTests,
                            utils.TestCase):
    def setUp(self):
        super(OIDCRefreshTokenTests, self).setUp()

        self.GRANT_TYPE = 'refresh_token'
        self.REFRESH_TOKEN = uuid.uuid4().hex

        self.plugin = oidc.OidcRefreshToken(
            self.AUTH_URL,
            self.IDENTITY_PROVIDER,
            self.PROTOCOL,
            client_id=self.CLIENT_ID,
            client_secret=self.CLIENT_SECRET,
            access_token_endpoint=self.ACCESS_TOKEN_ENDPOINT,
            project_name=self.PROJECT_NAME,
            refresh_token=self.REFRESH_TOKEN)

    def test_initial_call_to_get_access_token(self):
        self.requests_mock.post(
            self.ACCESS_TOKEN_ENDPOINT,
            json=oidc_fixtures.ACCESS_TOKEN_VIA_REFRESH_TOKEN_RESP)
        payload = {'refresh_token': self.REFRESH_TOKEN,
                   'grant_type': self.GRANT_TYPE}
        self.plugin._get_access_token(self.session, payload)

        last_req = self.requests_mock_last_request
        self.assertEqual(self.ACCESS_TOKEN_ENDPOINT, last_req.url)
        self.assertEqual('POST', last_req.method)
        encoded_payload = urllib.parse.urlencode(payload)
        self.assertEqual(encoded_payload, last_req.body)
