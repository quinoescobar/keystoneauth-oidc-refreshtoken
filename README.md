
# OpenID Connect Access Token Procurement Through Refresh Token for OpenStack Clients

[![Build Status](https://travis-ci.org/quinoescobar/keystoneauth-oidc-refreshtoken.svg?branch=master)](https://travis-ci.org/quinoescobar/keystoneauth-oidc-refreshtoken)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://raw.githubusercontent.com/quinoescobar/keystoneauth-oidc-refreshtoken/master/LICENSE)

Description
===========
This is a plugin for the OpenStack Clients,
[keystoneauth1](https://github.openstack/keystoneauth) library,
which provides client support Refresh Token for the procurement of the Access Token.

---------------
## Installation


#### PIP
* Install it via  pip:

      pip install keystoneauth-oidc-refreshtoken

#### Download
* Clone the repository and install it:

        git clone https://github.com/quinoescobar/keystoneauth-oidc-refreshtoken.git
        cd keystoneauth-oidc-refreshtoken
        pip install .

--------
## Usage

### CLI

You must specify the auth type `v3oidcrefreshtoken` in the `--os-auth-type` option and provide a valid Refresh Token with `--os-refresh-token` :



        openstack --os-auth-type v3oidcrefreshtoken \
        --os-auth-url https://keystone.example.org/v4/token \
        --os-refresh-token <refresh-token> \
        --os-client-id <client-id> \
        --os-client-secret <client-secret> \
        --os-protocol <protocol> \
        --os-identity-provider <identity-provider> \
        --os-access-token-endpoint <access-token-endpoint> \
        token issue

--------
[keystoneauth-oidc-refreshtoken](https://github.com/quinoescobar/keystoneauth-oidc-refreshtoken)
