.. cfg_cmd:: load-balancing reverse-proxy

help: Configure reverse-proxy

.. cfg_cmd:: load-balancing reverse-proxy backend <tag>

help: Backend server name

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> balance

help: Load-balancing algorithm
round-robin


.. cfg_cmd:: load-balancing reverse-proxy backend <tag> description

help: Description

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> mode

help: Proxy mode

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> parameters

help: Backend parameters

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> parameters http-check

help: HTTP health check

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag>

help: Proxy rule number

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag> domain-name

help: Domain name to match

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag> set

help: Proxy modifications

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag> set redirect-location

help: Set URL location

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag> set server

help: Server name

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag> ssl

help: SSL match options

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag> url-path

help: URL path match

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag> url-path begin

help: Begin URL match

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag> url-path end

help: End URL match

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> rule <tag> url-path exact

help: Exactly URL match

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> server <tag>

help: Backend server name

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> server <tag> address

help: Backend server address

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> server <tag> backup

help: Use backup server if other servers are not available

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> server <tag> check

help: Active health check backend server

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> server <tag> port

help: Port number used by connection

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> server <tag> send-proxy

help: Send a Proxy Protocol version 1 header (text format)

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> server <tag> send-proxy-v2

help: Send a Proxy Protocol version 2 header (binary format)

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> ssl

help: SSL Certificate, SSL Key and CA

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> ssl ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> timeout

help: Tiemout options

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> timeout check

help: Timeout in seconds for established connections

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> timeout connect

help: Set the maximum time to wait for a connection attempt to a server to succeed

.. cfg_cmd:: load-balancing reverse-proxy backend <tag> timeout server

help: Set the maximum inactivity time on the server side

.. cfg_cmd:: load-balancing reverse-proxy global-parameters

help: Global perfomance parameters and limits

.. cfg_cmd:: load-balancing reverse-proxy global-parameters max-connections

help: Maximum allowed connections

.. cfg_cmd:: load-balancing reverse-proxy global-parameters ssl-bind-ciphers

help: Cipher algorithms ("cipher suite") used during SSL/TLS handshake for all frontend servers
ecdhe-ecdsa-aes128-gcm-sha256 ecdhe-rsa-aes128-gcm-sha256 ecdhe-ecdsa-aes256-gcm-sha384 ecdhe-rsa-aes256-gcm-sha384 ecdhe-ecdsa-chacha20-poly1305 ecdhe-rsa-chacha20-poly1305 dhe-rsa-aes128-gcm-sha256 dhe-rsa-aes256-gcm-sha384


.. cfg_cmd:: load-balancing reverse-proxy global-parameters tls-version-min

help: Specify the minimum required TLS version
1.3


.. cfg_cmd:: load-balancing reverse-proxy service <tag>

help: Frontend service name

.. cfg_cmd:: load-balancing reverse-proxy service <tag> backend

help: Backend member

.. cfg_cmd:: load-balancing reverse-proxy service <tag> description

help: Description

.. cfg_cmd:: load-balancing reverse-proxy service <tag> listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: load-balancing reverse-proxy service <tag> mode

help: Proxy mode

.. cfg_cmd:: load-balancing reverse-proxy service <tag> port

help: Port number used by connection

.. cfg_cmd:: load-balancing reverse-proxy service <tag> redirect-http-to-https

help: Redirect HTTP to HTTPS

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag>

help: Proxy rule number

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag> domain-name

help: Domain name to match

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag> set

help: Proxy modifications

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag> set backend

help: Backend name

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag> set redirect-location

help: Set URL location

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag> ssl

help: SSL match options

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag> url-path

help: URL path match

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag> url-path begin

help: Begin URL match

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag> url-path end

help: End URL match

.. cfg_cmd:: load-balancing reverse-proxy service <tag> rule <tag> url-path exact

help: Exactly URL match

.. cfg_cmd:: load-balancing reverse-proxy service <tag> ssl

help: SSL Certificate, SSL Key and CA

.. cfg_cmd:: load-balancing reverse-proxy service <tag> ssl certificate

help: Certificate in PKI configuration

.. cfg_cmd:: load-balancing reverse-proxy vrf

help: VRF instance name

