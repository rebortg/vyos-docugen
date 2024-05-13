.. cfg_cmd:: interfaces openvpn <tag>

help: OpenVPN Tunnel Interface

.. cfg_cmd:: interfaces openvpn <tag> authentication

help: Authentication settings

.. cfg_cmd:: interfaces openvpn <tag> authentication password

help: Password used for authentication

.. cfg_cmd:: interfaces openvpn <tag> authentication username

help: Username used for authentication

.. cfg_cmd:: interfaces openvpn <tag> description

help: Description

.. cfg_cmd:: interfaces openvpn <tag> device-type

help: OpenVPN interface device-type
tun


.. cfg_cmd:: interfaces openvpn <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces openvpn <tag> encryption

help: Data Encryption settings

.. cfg_cmd:: interfaces openvpn <tag> encryption cipher

help: Standard Data Encryption Algorithm

.. cfg_cmd:: interfaces openvpn <tag> encryption ncp-ciphers

help: Cipher negotiation list for use in server or client mode

.. cfg_cmd:: interfaces openvpn <tag> hash

help: Hashing Algorithm

.. cfg_cmd:: interfaces openvpn <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces openvpn <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces openvpn <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces openvpn <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces openvpn <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces openvpn <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces openvpn <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces openvpn <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces openvpn <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces openvpn <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces openvpn <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces openvpn <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces openvpn <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces openvpn <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces openvpn <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces openvpn <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces openvpn <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces openvpn <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces openvpn <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces openvpn <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces openvpn <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces openvpn <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces openvpn <tag> keep-alive

help: Keepalive helper options

.. cfg_cmd:: interfaces openvpn <tag> keep-alive failure-count

help: Maximum number of keepalive packet failures
60


.. cfg_cmd:: interfaces openvpn <tag> keep-alive interval

help: Keepalive packet interval in seconds
10


.. cfg_cmd:: interfaces openvpn <tag> local-address <tag>

help: Local IP address of tunnel (IPv4 or IPv6)

.. cfg_cmd:: interfaces openvpn <tag> local-address <tag> subnet-mask

help: Subnet-mask for local IP address of tunnel (IPv4 only)

.. cfg_cmd:: interfaces openvpn <tag> local-host

help: Local IP address to accept connections (all if not set)

.. cfg_cmd:: interfaces openvpn <tag> local-port

help: Local port number to accept connections

.. cfg_cmd:: interfaces openvpn <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces openvpn <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces openvpn <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces openvpn <tag> mode

help: OpenVPN mode of operation

.. cfg_cmd:: interfaces openvpn <tag> offload

help: Configurable offload options

.. cfg_cmd:: interfaces openvpn <tag> offload dco

help: Enable data channel offload on this interface

.. cfg_cmd:: interfaces openvpn <tag> openvpn-option

help: Additional OpenVPN options. You must use the syntax of openvpn.conf in this text-field. Using this without proper knowledge may result in a crashed OpenVPN server. Check system log to look for errors.

.. cfg_cmd:: interfaces openvpn <tag> persistent-tunnel

help: Do not close and reopen interface (TUN/TAP device) on client restarts

.. cfg_cmd:: interfaces openvpn <tag> protocol

help: OpenVPN communication protocol
udp


.. cfg_cmd:: interfaces openvpn <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces openvpn <tag> remote-address

help: IP address of remote end of tunnel

.. cfg_cmd:: interfaces openvpn <tag> remote-host

help: Remote host to connect to (dynamic if not set)

.. cfg_cmd:: interfaces openvpn <tag> remote-port

help: Remote port number to connect to

.. cfg_cmd:: interfaces openvpn <tag> replace-default-route

help: OpenVPN tunnel to be used as the default route

.. cfg_cmd:: interfaces openvpn <tag> replace-default-route local

help: Tunnel endpoints are on the same subnet

.. cfg_cmd:: interfaces openvpn <tag> server

help: Server-mode options

.. cfg_cmd:: interfaces openvpn <tag> server client <tag>

help: Client-specific settings

.. cfg_cmd:: interfaces openvpn <tag> server client <tag> disable

help: Disable instance

.. cfg_cmd:: interfaces openvpn <tag> server client <tag> ip

help: IP address of the client

.. cfg_cmd:: interfaces openvpn <tag> server client <tag> push-route

help: Route to be pushed to the client

.. cfg_cmd:: interfaces openvpn <tag> server client <tag> subnet

help: Subnet belonging to the client (iroute)

.. cfg_cmd:: interfaces openvpn <tag> server client-ip-pool

help: Pool of client IPv4 addresses

.. cfg_cmd:: interfaces openvpn <tag> server client-ip-pool disable

help: Disable instance

.. cfg_cmd:: interfaces openvpn <tag> server client-ip-pool start

help: First IP address in the pool

.. cfg_cmd:: interfaces openvpn <tag> server client-ip-pool stop

help: Last IP address in the pool

.. cfg_cmd:: interfaces openvpn <tag> server client-ip-pool subnet-mask

help: Subnet mask pushed to dynamic clients. If not set the server subnet mask will be used. Only used with topology subnet or device type tap. Not used with bridged interfaces.

.. cfg_cmd:: interfaces openvpn <tag> server client-ipv6-pool

help: Pool of client IPv6 addresses

.. cfg_cmd:: interfaces openvpn <tag> server client-ipv6-pool base

help: Client IPv6 pool base address with optional prefix length

.. cfg_cmd:: interfaces openvpn <tag> server client-ipv6-pool disable

help: Disable instance

.. cfg_cmd:: interfaces openvpn <tag> server domain-name

help: DNS suffix to be pushed to all clients

.. cfg_cmd:: interfaces openvpn <tag> server max-connections

help: Number of maximum client connections

.. cfg_cmd:: interfaces openvpn <tag> server mfa

help: multi-factor authentication

.. cfg_cmd:: interfaces openvpn <tag> server mfa totp

help: Time-based one-time passwords

.. cfg_cmd:: interfaces openvpn <tag> server mfa totp challenge

help: Expect password as result of a challenge response protocol
enable


.. cfg_cmd:: interfaces openvpn <tag> server mfa totp digits

help: Number of digits to use for totp hash
6


.. cfg_cmd:: interfaces openvpn <tag> server mfa totp drift

help: Time drift in seconds
0


.. cfg_cmd:: interfaces openvpn <tag> server mfa totp slop

help: Maximum allowed clock slop in seconds
180


.. cfg_cmd:: interfaces openvpn <tag> server mfa totp step

help: Step value for totp in seconds
30


.. cfg_cmd:: interfaces openvpn <tag> server name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: interfaces openvpn <tag> server push-route <tag>

help: Route to be pushed to all clients

.. cfg_cmd:: interfaces openvpn <tag> server push-route <tag> metric

help: Set metric for this route
0


.. cfg_cmd:: interfaces openvpn <tag> server reject-unconfigured-clients

help: Reject connections from clients that are not explicitly configured

.. cfg_cmd:: interfaces openvpn <tag> server subnet

help: Server-mode subnet (from which client IPs are allocated)

.. cfg_cmd:: interfaces openvpn <tag> server topology

help: Topology for clients
net30


.. cfg_cmd:: interfaces openvpn <tag> shared-secret-key

help: Secret key shared with remote end of tunnel

.. cfg_cmd:: interfaces openvpn <tag> tls

help: Transport Layer Security (TLS) options

.. cfg_cmd:: interfaces openvpn <tag> tls auth-key

help: TLS shared secret key for tls-auth

.. cfg_cmd:: interfaces openvpn <tag> tls ca-certificate

help: Certificate Authority chain in PKI configuration

.. cfg_cmd:: interfaces openvpn <tag> tls certificate

help: Certificate in PKI configuration

.. cfg_cmd:: interfaces openvpn <tag> tls crypt-key

help: Static key to use to authenticate control channel

.. cfg_cmd:: interfaces openvpn <tag> tls dh-params

help: Diffie Hellman parameters (server only)

.. cfg_cmd:: interfaces openvpn <tag> tls peer-fingerprint

help: Peer certificate SHA256 fingerprint

.. cfg_cmd:: interfaces openvpn <tag> tls role

help: TLS negotiation role

.. cfg_cmd:: interfaces openvpn <tag> tls tls-version-min

help: Specify the minimum required TLS version

.. cfg_cmd:: interfaces openvpn <tag> use-lzo-compression

help: Use fast LZO compression on this TUN/TAP interface

.. cfg_cmd:: interfaces openvpn <tag> vrf

help: VRF instance name

