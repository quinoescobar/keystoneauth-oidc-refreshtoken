   # Copyright 2017 JOSÉ JOAQUÍN ESCOBAR GÓMEZ
   # File: setup.py
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

from setuptools import setup, find_packges

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='keystoneauth-oidc-refreshtoken',

    version='0.1.0',

    author='José Joaquín Escobar Gómez',
    author_email='alu0100837094@ull.edu.es',

    packages=['keystoneauth_oidc_refreshtoken'],
    url='https://github.com/quinoescobar/keystoneauth-oidc-refreshtoken',

    license='Apache Software License',

    description='Implementation for OpenID Connect for access token procurement through refresh token',
    long_description=long_description,

    install_require=['',''],

    classifiers=[

        'Development Status :: 3 - Alpha',

        'Environment :: OpenStack'
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
