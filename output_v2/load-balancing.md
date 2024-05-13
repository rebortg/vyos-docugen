.. cfg_cmd:: load-balancing

help: Configure load-balancing

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

.. cfg_cmd:: load-balancing wan

help: Configure Wide Area Network (WAN) load-balancing

.. cfg_cmd:: load-balancing wan disable-source-nat

help: Disable source NAT rules from being configured for WAN load balancing

.. cfg_cmd:: load-balancing wan enable-local-traffic

help: Enable WAN load balancing for locally sourced traffic

.. cfg_cmd:: load-balancing wan flush-connections

help: Flush connection tracking tables on connection state change

.. cfg_cmd:: load-balancing wan hook

help: Script to be executed on interface status change

.. cfg_cmd:: load-balancing wan interface-health <tag>

help: Interface name

.. cfg_cmd:: load-balancing wan interface-health <tag> failure-count

help: Failure count
1


.. cfg_cmd:: load-balancing wan interface-health <tag> nexthop

help: Outbound interface nexthop address. Can be 'DHCP or IPv4 address' [REQUIRED]

.. cfg_cmd:: load-balancing wan interface-health <tag> success-count

help: Success count
1


.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag>

help: Rule number

.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> resp-time

help: Ping response time (seconds)
5


.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> target

help: Health target address

.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> test-script

help: Path to user-defined script

.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> ttl-limit

help: TTL limit (hop count)
1


.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> type

help: WLB test type
ping


.. cfg_cmd:: load-balancing wan rule <tag>

help: Rule number (1-9999)

.. cfg_cmd:: load-balancing wan rule <tag> description

help: Description

.. cfg_cmd:: load-balancing wan rule <tag> destination

help: Destination

.. cfg_cmd:: load-balancing wan rule <tag> destination address

help: IP address, subnet, or range

.. cfg_cmd:: load-balancing wan rule <tag> destination port

help: Port number

.. cfg_cmd:: load-balancing wan rule <tag> exclude

help: Exclude packets matching this rule from WAN load balance

.. cfg_cmd:: load-balancing wan rule <tag> failover

help: Enable failover for packets matching this rule from WAN load balance

.. cfg_cmd:: load-balancing wan rule <tag> inbound-interface

help: Inbound interface name (e.g., "eth0") [REQUIRED]

.. cfg_cmd:: load-balancing wan rule <tag> interface <tag>

help: Interface name [REQUIRED]

.. cfg_cmd:: load-balancing wan rule <tag> interface <tag> weight

help: Load-balance weight
1


.. cfg_cmd:: load-balancing wan rule <tag> limit

help: Enable packet limit for this rule

.. cfg_cmd:: load-balancing wan rule <tag> limit burst

help: Burst limit for matching packets
5


.. cfg_cmd:: load-balancing wan rule <tag> limit period

help: Time window for rate calculation
second


.. cfg_cmd:: load-balancing wan rule <tag> limit rate

help: Number of packets used for rate limit
5


.. cfg_cmd:: load-balancing wan rule <tag> limit threshold

help: Threshold behavior for limit
below


.. cfg_cmd:: load-balancing wan rule <tag> per-packet-balancing

help: Option to match traffic per-packet instead of the default, per-flow

.. cfg_cmd:: load-balancing wan rule <tag> protocol

help: Protocol to match (protocol name, number, or "all")
all


.. cfg_cmd:: load-balancing wan rule <tag> source

help: Source information

.. cfg_cmd:: load-balancing wan rule <tag> source address

help: IP address, subnet, or range

.. cfg_cmd:: load-balancing wan rule <tag> source port

help: Port number

.. cfg_cmd:: load-balancing wan sticky-connections

help: Configure sticky connections

.. cfg_cmd:: load-balancing wan sticky-connections inbound

help: Enable sticky incoming WAN connections

