.. cfg_cmd:: service https

help: HTTPS configuration

.. cfg_cmd:: service https allow-client

help: Restrict to allowed IP client addresses

.. cfg_cmd:: service https allow-client address

help: Allowed IP client addresses

.. cfg_cmd:: service https api

help: VyOS HTTP API configuration

.. cfg_cmd:: service https api cors

help: Set CORS options

.. cfg_cmd:: service https api cors allow-origin

help: Allow resource request from origin

.. cfg_cmd:: service https api debug

help: Debug

.. cfg_cmd:: service https api graphql

help: GraphQL support

.. cfg_cmd:: service https api graphql authentication

help: GraphQL authentication

.. cfg_cmd:: service https api graphql authentication expiration

help: Token time to expire in seconds
3600


.. cfg_cmd:: service https api graphql authentication secret-length

help: Length of shared secret in bytes
32


.. cfg_cmd:: service https api graphql authentication type

help: Authentication type
key


.. cfg_cmd:: service https api graphql introspection

help: Schema introspection

.. cfg_cmd:: service https api keys

help: HTTP API keys

.. cfg_cmd:: service https api keys id <tag>

help: HTTP API id

.. cfg_cmd:: service https api keys id <tag> key

help: HTTP API plaintext key

.. cfg_cmd:: service https api strict

help: Enforce strict path checking

.. cfg_cmd:: service https certificates

help: TLS certificates

.. cfg_cmd:: service https certificates ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: service https certificates certificate

help: Certificate in PKI configuration

.. cfg_cmd:: service https certificates dh-params

help: Diffie Hellman parameters (server only)

.. cfg_cmd:: service https enable-http-redirect

help: Enable HTTP to HTTPS redirect

.. cfg_cmd:: service https listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: service https port

help: Port number used by connection
443


.. cfg_cmd:: service https request-body-size-limit

help: Maximum request body size in megabytes
1


.. cfg_cmd:: service https tls-version

help: Specify available TLS version(s)
1.2 1.3


.. cfg_cmd:: service https vrf

help: VRF instance name

