# coding=utf-8

# Copyright 2017 JOSE JOAQUIN ESCOBAR GOMEZ
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

from six.moves import urllib

from keystoneauth_oidc_refreshtoken import plugin as oidc
from keystoneauth_oidc_refreshtoken.tests.unit import oidc_fixtures

KEYSTONE_TOKEN_VALUE = uuid.uuid4().hex


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

        last_req = self.requests_mock.last_request
        self.assertEqual(self.ACCESS_TOKEN_ENDPOINT, last_req.url)
        self.assertEqual('POST', last_req.method)
        encoded_payload = urllib.parse.urlencode(payload)
        self.assertEqual(encoded_payload, last_req.body)

    def test_second_call_to_protected_url(self):
        self.requests_mock.post(
            self.FEDERATION_AUTH_URL,
            json=oidc_fixtures.UNSCOPED_TOKEN,
            headers={'X-Subject-Token': KEYSTONE_TOKEN_VALUE})

        response = self.plugin._get_keystone_token(self.session,
                                                   self.ACCESS_TOKEN)

        self.assertEqual(self.FEDERATION_AUTH_URL, response.request.url)
        self.assertEqual('POST', response.request.method)
        headers = {'Authorization': 'Bearer ' + self.ACCESS_TOKEN}
        self.assertEqual(headers['Authorization'],
                         response.request.headers['Authorization'])

    def test_end_to_end_workflow(self):
        self.requests_mock.post(
            self.ACCESS_TOKEN_ENDPOINT,
            json=oidc_fixtures.ACCESS_TOKEN_VIA_REFRESH_TOKEN_RESP)

        self.requests_mock.post(
            self.FEDERATION_AUTH_URL,
            json=oidc_fixtures.UNSCOPED_TOKEN,
            headers={'X-Subject-Token': KEYSTONE_TOKEN_VALUE})

        response = self.plugin.get_unscoped_auth_ref(self.session)
        self.assertEqual(KEYSTONE_TOKEN_VALUE, response.auth_token)
