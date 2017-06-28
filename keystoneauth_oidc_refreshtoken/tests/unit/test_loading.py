# coding=utf-8

# Copyright 2017 JOSE JOAQUIN ESCOBAR GOMEZ
# File: test_loading.py
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

from keystoneauth1 import loading
from keystoneauth1.tests.unit.loading import test_v3
from keystoneauth1.tests.unit import utils


class OpenIDConnectRefreshToken(test_v3.OpenIDConnectBaseTests,
                                utils.TestCase):

    plugin_name = "v3oidcrefreshtoken"

    def setUp(self):
        super(OpenIDConnectRefreshToken, self).setUp()
        self.auth_url = uuid.uuid4().hex

    def create(self, **kwargs):
        kwargs.setdefault('auth_url', self.auth_url)
        loader = loading.get_plugin_loader(self.plugin_name)
        return loader.load_from_options(**kwargs)

    def test_options(self):
        options = loading.get_plugin_loader(self.plugin_name).get_options()
        self.assertTrue(
            set(['refresh_token']).issubset(
                set([o.name for o in options]))
        )

    def test_basic(self):
        identity_provider = uuid.uuid4().hex
        protocol = uuid.uuid4().hex
        client_id = uuid.uuid4().hex
        client_secret = uuid.uuid4().hex
        access_token_endpoint = uuid.uuid4().hex
        refresh_token = uuid.uuid4().hex

        oidc = self.create(identity_provider=identity_provider,
                           protocol=protocol,
                           client_id=client_id,
                           client_secret=client_secret,
                           access_token_endpoint=access_token_endpoint,
                           refresh_token=refresh_token)

        self.assertEqual(identity_provider, oidc.identity_provider)
        self.assertEqual(protocol, oidc.protocol)
        self.assertEqual(client_id, oidc.client_id)
        self.assertEqual(client_secret, oidc.client_secret)
        self.assertEqual(access_token_endpoint, oidc.access_token_endpoint)
        self.assertEqual(refresh_token, oidc.refresh_token)
