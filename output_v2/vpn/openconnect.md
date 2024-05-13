.. cfg_cmd:: vpn openconnect

help: SSL VPN OpenConnect, AnyConnect compatible server

.. cfg_cmd:: vpn openconnect accounting

help: Accounting for users OpenConnect VPN Sessions

.. cfg_cmd:: vpn openconnect accounting mode

help: Accounting mode used by this server

.. cfg_cmd:: vpn openconnect accounting mode radius

help: Use RADIUS server for accounting

.. cfg_cmd:: vpn openconnect accounting radius

help: RADIUS accounting for users OpenConnect VPN sessions OpenConnect authentication mode radius

.. cfg_cmd:: vpn openconnect accounting radius server <tag>

help: RADIUS server configuration

.. cfg_cmd:: vpn openconnect accounting radius server <tag> disable

help: Disable instance

.. cfg_cmd:: vpn openconnect accounting radius server <tag> key

help: Shared secret key

.. cfg_cmd:: vpn openconnect accounting radius server <tag> port

help: Accounting port
1813


.. cfg_cmd:: vpn openconnect authentication

help: Authentication for remote access SSL VPN Server

.. cfg_cmd:: vpn openconnect authentication group

help: Group that a client is allowed to select (from a list). Maps to RADIUS Class attribute.

.. cfg_cmd:: vpn openconnect authentication identity-based-config

help: Include configuration file by username or RADIUS group attribute

.. cfg_cmd:: vpn openconnect authentication identity-based-config default-config

help: Default configuration if discrete config could not be found

.. cfg_cmd:: vpn openconnect authentication identity-based-config directory

help: Directory to containing configuration files

.. cfg_cmd:: vpn openconnect authentication identity-based-config disable

help: Disable instance

.. cfg_cmd:: vpn openconnect authentication identity-based-config mode

help: Select per user or per group configuration file - ignored if authentication group is configured

.. cfg_cmd:: vpn openconnect authentication local-users

help: Local user authentication

.. cfg_cmd:: vpn openconnect authentication local-users username <tag>

help: No help available

.. cfg_cmd:: vpn openconnect authentication local-users username <tag> disable

help: Disable instance

.. cfg_cmd:: vpn openconnect authentication local-users username <tag> otp

help: 2FA OTP authentication parameters

.. cfg_cmd:: vpn openconnect authentication local-users username <tag> otp interval

help: Time tokens interval in seconds
30


.. cfg_cmd:: vpn openconnect authentication local-users username <tag> otp key

help: Token Key Secret key for the token algorithm (see RFC 4226)

.. cfg_cmd:: vpn openconnect authentication local-users username <tag> otp otp-length

help: Number of digits in OTP code
6


.. cfg_cmd:: vpn openconnect authentication local-users username <tag> otp token-type

help: Token type
hotp-time


.. cfg_cmd:: vpn openconnect authentication local-users username <tag> password

help: Password used for authentication

.. cfg_cmd:: vpn openconnect authentication mode

help: Authentication mode used by this server

.. cfg_cmd:: vpn openconnect authentication mode local

help: Use local username/password configuration (OTP supported)

.. cfg_cmd:: vpn openconnect authentication mode radius

help: Use RADIUS server for user autentication

.. cfg_cmd:: vpn openconnect authentication radius

help: RADIUS based user authentication

.. cfg_cmd:: vpn openconnect authentication radius groupconfig

help: If the groupconfig option is set, then config-per-user will be overriden, and all configuration will be read from RADIUS.

.. cfg_cmd:: vpn openconnect authentication radius server <tag>

help: RADIUS server configuration

.. cfg_cmd:: vpn openconnect authentication radius server <tag> disable

help: Disable instance

.. cfg_cmd:: vpn openconnect authentication radius server <tag> key

help: Shared secret key

.. cfg_cmd:: vpn openconnect authentication radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: vpn openconnect authentication radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: vpn openconnect authentication radius timeout

help: Session timeout
2


.. cfg_cmd:: vpn openconnect http-security-headers

help: Enable HTTP security headers

.. cfg_cmd:: vpn openconnect listen-address

help: Local IPv4 addresses to listen on
0.0.0.0


.. cfg_cmd:: vpn openconnect listen-ports

help: Specify custom ports to use for client connections

.. cfg_cmd:: vpn openconnect listen-ports tcp

help: tcp port number to accept connections
443


.. cfg_cmd:: vpn openconnect listen-ports udp

help: udp port number to accept connections
443


.. cfg_cmd:: vpn openconnect network-settings

help: Network settings

.. cfg_cmd:: vpn openconnect network-settings client-ip-settings

help: Client IP pools settings

.. cfg_cmd:: vpn openconnect network-settings client-ip-settings subnet

help: Client IP subnet (CIDR notation)

.. cfg_cmd:: vpn openconnect network-settings client-ipv6-pool

help: Pool of client IPv6 addresses

.. cfg_cmd:: vpn openconnect network-settings client-ipv6-pool mask

help: Prefix length used for individual client
64


.. cfg_cmd:: vpn openconnect network-settings client-ipv6-pool prefix

help: Pool of addresses used to assign to clients

.. cfg_cmd:: vpn openconnect network-settings name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: vpn openconnect network-settings push-route

help: Route to be pushed to the client

.. cfg_cmd:: vpn openconnect network-settings split-dns

help: Domains over which the provided DNS should be used

.. cfg_cmd:: vpn openconnect network-settings tunnel-all-dns

help: If the tunnel-all-dns option is set to yes, tunnel all DNS queries via the VPN. This is the default when a default route is set.
no


.. cfg_cmd:: vpn openconnect ssl

help: SSL Certificate, SSL Key and CA

.. cfg_cmd:: vpn openconnect ssl ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: vpn openconnect ssl certificate

help: Certificate in PKI configuration

.. cfg_cmd:: vpn openconnect ssl passphrase

help: Private key passphrase

