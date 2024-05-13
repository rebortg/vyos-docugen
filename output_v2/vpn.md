.. cfg_cmd:: vpn

help: Virtual Private Network (VPN)

.. cfg_cmd:: vpn ipsec

help: VPN IP security (IPsec) parameters

.. cfg_cmd:: vpn ipsec authentication

help: Authentication

.. cfg_cmd:: vpn ipsec authentication psk <tag>

help: Pre-shared key name

.. cfg_cmd:: vpn ipsec authentication psk <tag> dhcp-interface

help: DHCP interface supplying next-hop IP address

.. cfg_cmd:: vpn ipsec authentication psk <tag> id

help: ID for authentication

.. cfg_cmd:: vpn ipsec authentication psk <tag> secret

help: IKE pre-shared secret key

.. cfg_cmd:: vpn ipsec disable-uniqreqids

help: Disable requirement for unique IDs in the Security Database

.. cfg_cmd:: vpn ipsec esp-group <tag>

help: Encapsulating Security Payload (ESP) group name

.. cfg_cmd:: vpn ipsec esp-group <tag> compression

help: Enable ESP compression

.. cfg_cmd:: vpn ipsec esp-group <tag> life-bytes

help: Security Association byte count to expire

.. cfg_cmd:: vpn ipsec esp-group <tag> life-packets

help: Security Association packet count to expire

.. cfg_cmd:: vpn ipsec esp-group <tag> lifetime

help: Security Association time to expire
3600


.. cfg_cmd:: vpn ipsec esp-group <tag> mode

help: ESP mode
tunnel


.. cfg_cmd:: vpn ipsec esp-group <tag> pfs

help: ESP Perfect Forward Secrecy
enable


.. cfg_cmd:: vpn ipsec esp-group <tag> proposal <tag>

help: ESP group proposal

.. cfg_cmd:: vpn ipsec esp-group <tag> proposal <tag> encryption

help: Encryption algorithm
aes128


.. cfg_cmd:: vpn ipsec esp-group <tag> proposal <tag> hash

help: Hash algorithm
sha1


.. cfg_cmd:: vpn ipsec ike-group <tag>

help: Internet Key Exchange (IKE) group name

.. cfg_cmd:: vpn ipsec ike-group <tag> close-action

help: Action to take if a child SA is unexpectedly closed
none


.. cfg_cmd:: vpn ipsec ike-group <tag> dead-peer-detection

help: Dead Peer Detection (DPD)

.. cfg_cmd:: vpn ipsec ike-group <tag> dead-peer-detection action

help: Keep-alive failure action
clear


.. cfg_cmd:: vpn ipsec ike-group <tag> dead-peer-detection interval

help: Keep-alive interval
30


.. cfg_cmd:: vpn ipsec ike-group <tag> dead-peer-detection timeout

help: Dead Peer Detection keep-alive timeout (IKEv1 only)
120


.. cfg_cmd:: vpn ipsec ike-group <tag> disable-mobike

help: Disable MOBIKE Support (IKEv2 only)

.. cfg_cmd:: vpn ipsec ike-group <tag> ikev2-reauth

help: Re-authentication of the remote peer during an IKE re-key (IKEv2 only)

.. cfg_cmd:: vpn ipsec ike-group <tag> key-exchange

help: IKE version

.. cfg_cmd:: vpn ipsec ike-group <tag> lifetime

help: IKE lifetime
28800


.. cfg_cmd:: vpn ipsec ike-group <tag> mode

help: IKEv1 phase 1 mode
main


.. cfg_cmd:: vpn ipsec ike-group <tag> proposal <tag>

help: IKE proposal

.. cfg_cmd:: vpn ipsec ike-group <tag> proposal <tag> dh-group

help: dh-grouphelp
2


.. cfg_cmd:: vpn ipsec ike-group <tag> proposal <tag> encryption

help: Encryption algorithm
aes128


.. cfg_cmd:: vpn ipsec ike-group <tag> proposal <tag> hash

help: Hash algorithm
sha1


.. cfg_cmd:: vpn ipsec ike-group <tag> proposal <tag> prf

help: Pseudo-Random Functions

.. cfg_cmd:: vpn ipsec interface

help: Interface to use

.. cfg_cmd:: vpn ipsec log

help: IPsec logging

.. cfg_cmd:: vpn ipsec log level

help: Global IPsec logging Level
0


.. cfg_cmd:: vpn ipsec log subsystem

help: Subsystem logging levels

.. cfg_cmd:: vpn ipsec options

help: Global IPsec settings

.. cfg_cmd:: vpn ipsec options disable-route-autoinstall

help: Do not automatically install routes to remote networks

.. cfg_cmd:: vpn ipsec options flexvpn

help: Allow FlexVPN vendor ID payload (IKEv2 only)

.. cfg_cmd:: vpn ipsec options interface

help: Interface to use

.. cfg_cmd:: vpn ipsec options virtual-ip

help: Allow install virtual-ip addresses

.. cfg_cmd:: vpn ipsec profile <tag>

help: VPN IPsec profile

.. cfg_cmd:: vpn ipsec profile <tag> authentication

help: Authentication

.. cfg_cmd:: vpn ipsec profile <tag> authentication mode

help: Authentication mode

.. cfg_cmd:: vpn ipsec profile <tag> authentication pre-shared-secret

help: Pre-shared secret key

.. cfg_cmd:: vpn ipsec profile <tag> bind

help: DMVPN tunnel configuration

.. cfg_cmd:: vpn ipsec profile <tag> bind tunnel

help: Tunnel interface associated with this profile

.. cfg_cmd:: vpn ipsec profile <tag> disable

help: Disable instance

.. cfg_cmd:: vpn ipsec profile <tag> esp-group

help: Encapsulating Security Payloads (ESP) group name

.. cfg_cmd:: vpn ipsec profile <tag> ike-group

help: Internet Key Exchange (IKE) group name

.. cfg_cmd:: vpn ipsec remote-access

help: IKEv2 remote access VPN

.. cfg_cmd:: vpn ipsec remote-access connection <tag>

help: IKEv2 VPN connection name

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication

help: Authentication for remote access

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication client-mode

help: Client authentication mode
eap-mschapv2


.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication local-id

help: Local ID for peer authentication

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication local-users

help: Local user authentication

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication local-users username <tag>

help: Username used for authentication

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication local-users username <tag> disable

help: Disable instance

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication local-users username <tag> password

help: Password used for authentication

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication pre-shared-secret

help: Pre-shared secret key

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication server-mode

help: Server authentication mode
x509


.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication x509

help: X.509 certificate

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication x509 ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication x509 certificate

help: Certificate in PKI configuration

.. cfg_cmd:: vpn ipsec remote-access connection <tag> authentication x509 passphrase

help: Private key passphrase

.. cfg_cmd:: vpn ipsec remote-access connection <tag> description

help: Description

.. cfg_cmd:: vpn ipsec remote-access connection <tag> disable

help: Disable instance

.. cfg_cmd:: vpn ipsec remote-access connection <tag> esp-group

help: Encapsulating Security Payloads (ESP) group name

.. cfg_cmd:: vpn ipsec remote-access connection <tag> ike-group

help: Internet Key Exchange (IKE) group name

.. cfg_cmd:: vpn ipsec remote-access connection <tag> local

help: Local parameters for interesting traffic

.. cfg_cmd:: vpn ipsec remote-access connection <tag> local port

help: Port number used by connection

.. cfg_cmd:: vpn ipsec remote-access connection <tag> local prefix

help: Local IPv4 or IPv6 prefix

.. cfg_cmd:: vpn ipsec remote-access connection <tag> local-address

help: IPv4 or IPv6 address of a local interface to use for VPN

.. cfg_cmd:: vpn ipsec remote-access connection <tag> pool

help: IP address pool

.. cfg_cmd:: vpn ipsec remote-access connection <tag> replay-window

help: IPsec replay window to configure for this CHILD_SA
32


.. cfg_cmd:: vpn ipsec remote-access connection <tag> timeout

help: Timeout to close connection if no data is transmitted
28800


.. cfg_cmd:: vpn ipsec remote-access connection <tag> unique

help: Connection uniqueness enforcement policy

.. cfg_cmd:: vpn ipsec remote-access dhcp

help: DHCP pool options for remote access

.. cfg_cmd:: vpn ipsec remote-access dhcp interface

help: Interface to use

.. cfg_cmd:: vpn ipsec remote-access dhcp server

help: DHCP server address

.. cfg_cmd:: vpn ipsec remote-access pool <tag>

help: IP address pool for remote access users

.. cfg_cmd:: vpn ipsec remote-access pool <tag> exclude

help: Local IPv4 or IPv6 pool prefix exclusions

.. cfg_cmd:: vpn ipsec remote-access pool <tag> name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: vpn ipsec remote-access pool <tag> prefix

help: Local IPv4 or IPv6 pool prefix

.. cfg_cmd:: vpn ipsec remote-access radius

help: RADIUS based user authentication

.. cfg_cmd:: vpn ipsec remote-access radius nas-identifier

help: NAS-Identifier attribute sent to RADIUS

.. cfg_cmd:: vpn ipsec remote-access radius server <tag>

help: No help available

.. cfg_cmd:: vpn ipsec remote-access radius server <tag> disable

help: Disable instance

.. cfg_cmd:: vpn ipsec remote-access radius server <tag> disable-accounting

help: Disable accounting

.. cfg_cmd:: vpn ipsec remote-access radius server <tag> key

help: Shared secret key

.. cfg_cmd:: vpn ipsec remote-access radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: vpn ipsec remote-access radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: vpn ipsec remote-access radius timeout

help: Session timeout
2


.. cfg_cmd:: vpn ipsec site-to-site

help: Site-to-site VPN

.. cfg_cmd:: vpn ipsec site-to-site peer <tag>

help: Connection name of the peer

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication

help: Peer authentication

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication local-id

help: Local ID for peer authentication

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication mode

help: Authentication mode

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication remote-id

help: ID for remote authentication
%any


.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication rsa

help: RSA keys

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication rsa local-key

help: Name of PKI key-pair with local private key

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication rsa passphrase

help: Local private key passphrase

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication rsa remote-key

help: Name of PKI key-pair with remote public key

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication use-x509-id

help: Use certificate common name as ID

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication x509

help: X.509 certificate

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication x509 ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication x509 certificate

help: Certificate in PKI configuration

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> authentication x509 passphrase

help: Private key passphrase

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> connection-type

help: Connection type

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> default-esp-group

help: Defult ESP group name

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> description

help: Description

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> dhcp-interface

help: DHCP interface supplying next-hop IP address

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> disable

help: Disable instance

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> force-udp-encapsulation

help: Force UDP encapsulation

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> ike-group

help: Internet Key Exchange (IKE) group name

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> ikev2-reauth

help: Re-authentication of the remote peer during an IKE re-key (IKEv2 only)

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> local-address

help: IPv4 or IPv6 address of a local interface to use for VPN

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> remote-address

help: IPv4 or IPv6 address of the remote peer

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> replay-window

help: IPsec replay window to configure for this CHILD_SA
32


.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag>

help: Peer tunnel

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> disable

help: Disable instance

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> esp-group

help: Encapsulating Security Payloads (ESP) group name

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> local

help: Local parameters for interesting traffic

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> local port

help: Port number used by connection

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> local prefix

help: Local IPv4 or IPv6 prefix

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> priority

help: Priority for IPsec policy (lowest value more preferable)

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> protocol

help: Protocol

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> remote

help: Match remote addresses

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> remote port

help: Port number used by connection

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> tunnel <tag> remote prefix

help: Remote IPv4 or IPv6 prefix

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> virtual-address

help: Initiator request virtual-address from peer

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> vti

help: Virtual tunnel interface

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> vti bind

help: VTI tunnel interface associated with this configuration

.. cfg_cmd:: vpn ipsec site-to-site peer <tag> vti esp-group

help: Encapsulating Security Payloads (ESP) group name

.. cfg_cmd:: vpn l2tp

help: L2TP Virtual Private Network (VPN)

.. cfg_cmd:: vpn l2tp remote-access

help: Remote access L2TP VPN

.. cfg_cmd:: vpn l2tp remote-access authentication

help: Authentication for remote access L2TP VPN

.. cfg_cmd:: vpn l2tp remote-access authentication local-users

help: Local user authentication for PPPoE server

.. cfg_cmd:: vpn l2tp remote-access authentication local-users username <tag>

help: User name for authentication

.. cfg_cmd:: vpn l2tp remote-access authentication local-users username <tag> disable

help: Disable instance

.. cfg_cmd:: vpn l2tp remote-access authentication local-users username <tag> password

help: Password for authentication

.. cfg_cmd:: vpn l2tp remote-access authentication local-users username <tag> rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: vpn l2tp remote-access authentication local-users username <tag> rate-limit download

help: Download bandwidth limit in kbits/sec

.. cfg_cmd:: vpn l2tp remote-access authentication local-users username <tag> rate-limit upload

help: Upload bandwidth limit in kbits/sec

.. cfg_cmd:: vpn l2tp remote-access authentication local-users username <tag> static-ip

help: Static client IP address
*


.. cfg_cmd:: vpn l2tp remote-access authentication mode

help: Authentication mode used by this server
local


.. cfg_cmd:: vpn l2tp remote-access authentication protocols

help: Authentication protocol for remote access peer
pap chap mschap mschap-v2


.. cfg_cmd:: vpn l2tp remote-access authentication radius

help: RADIUS based user authentication

.. cfg_cmd:: vpn l2tp remote-access authentication radius accounting-interim-interval

help: Interval in seconds to send accounting information

.. cfg_cmd:: vpn l2tp remote-access authentication radius acct-interim-jitter

help: Maximum jitter value in seconds to be applied to accounting information interval

.. cfg_cmd:: vpn l2tp remote-access authentication radius acct-timeout

help: Timeout for Interim-Update packets, terminate session afterwards
3


.. cfg_cmd:: vpn l2tp remote-access authentication radius dynamic-author

help: Dynamic Authorization Extension/Change of Authorization server

.. cfg_cmd:: vpn l2tp remote-access authentication radius dynamic-author key

help: Shared secret for Dynamic Authorization Extension server

.. cfg_cmd:: vpn l2tp remote-access authentication radius dynamic-author port

help: Port for Dynamic Authorization Extension server (DM/CoA)
1700


.. cfg_cmd:: vpn l2tp remote-access authentication radius dynamic-author server

help: IP address for Dynamic Authorization Extension server (DM/CoA)

.. cfg_cmd:: vpn l2tp remote-access authentication radius max-try

help: Number of tries to send Access-Request/Accounting-Request queries
3


.. cfg_cmd:: vpn l2tp remote-access authentication radius nas-identifier

help: NAS-Identifier attribute sent to RADIUS

.. cfg_cmd:: vpn l2tp remote-access authentication radius nas-ip-address

help: NAS-IP-Address attribute sent to RADIUS

.. cfg_cmd:: vpn l2tp remote-access authentication radius preallocate-vif

help: Enable attribute NAS-Port-Id in Access-Request

.. cfg_cmd:: vpn l2tp remote-access authentication radius rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: vpn l2tp remote-access authentication radius rate-limit attribute

help: RADIUS attribute that contains rate information
Filter-Id


.. cfg_cmd:: vpn l2tp remote-access authentication radius rate-limit enable

help: Enable bandwidth shaping via RADIUS

.. cfg_cmd:: vpn l2tp remote-access authentication radius rate-limit multiplier

help: Shaper multiplier
1


.. cfg_cmd:: vpn l2tp remote-access authentication radius rate-limit vendor

help: Vendor dictionary

.. cfg_cmd:: vpn l2tp remote-access authentication radius server <tag>

help: No help available

.. cfg_cmd:: vpn l2tp remote-access authentication radius server <tag> acct-port

help: Accounting port
1813


.. cfg_cmd:: vpn l2tp remote-access authentication radius server <tag> disable

help: Disable instance

.. cfg_cmd:: vpn l2tp remote-access authentication radius server <tag> disable-accounting

help: Disable accounting

.. cfg_cmd:: vpn l2tp remote-access authentication radius server <tag> fail-time

help: Mark server unavailable for <n> seconds on failure
0


.. cfg_cmd:: vpn l2tp remote-access authentication radius server <tag> key

help: Shared secret key

.. cfg_cmd:: vpn l2tp remote-access authentication radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: vpn l2tp remote-access authentication radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: vpn l2tp remote-access authentication radius timeout

help: Timeout in seconds to wait response from RADIUS server
3


.. cfg_cmd:: vpn l2tp remote-access client-ip-pool <tag>

help: Client IP pool

.. cfg_cmd:: vpn l2tp remote-access client-ip-pool <tag> next-pool

help: Next pool name

.. cfg_cmd:: vpn l2tp remote-access client-ip-pool <tag> range

help: Range of IP addresses

.. cfg_cmd:: vpn l2tp remote-access client-ipv6-pool <tag>

help: Pool of client IPv6 addresses

.. cfg_cmd:: vpn l2tp remote-access client-ipv6-pool <tag> delegate <tag>

help: Subnet used to delegate prefix through DHCPv6-PD (RFC3633)

.. cfg_cmd:: vpn l2tp remote-access client-ipv6-pool <tag> delegate <tag> delegation-prefix

help: Prefix length delegated to client

.. cfg_cmd:: vpn l2tp remote-access client-ipv6-pool <tag> prefix <tag>

help: Pool of addresses used to assign to clients

.. cfg_cmd:: vpn l2tp remote-access client-ipv6-pool <tag> prefix <tag> mask

help: Prefix length used for individual client
64


.. cfg_cmd:: vpn l2tp remote-access default-ipv6-pool

help: Default client IPv6 pool name

.. cfg_cmd:: vpn l2tp remote-access default-pool

help: Default client IP pool name

.. cfg_cmd:: vpn l2tp remote-access description

help: Description

.. cfg_cmd:: vpn l2tp remote-access extended-scripts

help: Extended script execution

.. cfg_cmd:: vpn l2tp remote-access extended-scripts on-change

help: Script to run when session interface changed by RADIUS CoA handling

.. cfg_cmd:: vpn l2tp remote-access extended-scripts on-down

help: Script to run when session interface going to terminate

.. cfg_cmd:: vpn l2tp remote-access extended-scripts on-pre-up

help: Script to run before session interface comes up

.. cfg_cmd:: vpn l2tp remote-access extended-scripts on-up

help: Script to run when session interface is completely configured and started

.. cfg_cmd:: vpn l2tp remote-access gateway-address

help: Gateway IP address

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings

help: Internet Protocol Security (IPsec) for remote access L2TP VPN

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings authentication

help: IPsec authentication settings

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings authentication mode

help: Authentication mode for IPsec

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings authentication pre-shared-secret

help: Pre-shared secret key

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings authentication x509

help: X.509 certificate

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings authentication x509 ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings authentication x509 certificate

help: Certificate in PKI configuration

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings authentication x509 passphrase

help: Private key passphrase

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings esp-group

help: Encapsulating Security Payloads (ESP) group name

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings ike-group

help: Internet Key Exchange (IKE) group name

.. cfg_cmd:: vpn l2tp remote-access ipsec-settings ike-lifetime

help: IKE lifetime
3600


.. cfg_cmd:: vpn l2tp remote-access ipsec-settings lifetime

help: ESP lifetime
3600


.. cfg_cmd:: vpn l2tp remote-access limits

help: Limits the connection rate from a single source

.. cfg_cmd:: vpn l2tp remote-access limits burst

help: Burst count

.. cfg_cmd:: vpn l2tp remote-access limits connection-limit

help: Acceptable rate of connections (e.g. 1/min, 60/sec)

.. cfg_cmd:: vpn l2tp remote-access limits timeout

help: Timeout in seconds

.. cfg_cmd:: vpn l2tp remote-access lns

help: L2TP Network Server (LNS)

.. cfg_cmd:: vpn l2tp remote-access lns host-name

help: Sent to the client (LAC) in the Host-Name attribute

.. cfg_cmd:: vpn l2tp remote-access lns shared-secret

help: Tunnel password used to authenticate the client (LAC)

.. cfg_cmd:: vpn l2tp remote-access max-concurrent-sessions

help: Maximum number of concurrent session start attempts

.. cfg_cmd:: vpn l2tp remote-access mtu

help: Maximum Transmission Unit (MTU)
1436


.. cfg_cmd:: vpn l2tp remote-access name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: vpn l2tp remote-access outside-address

help: External IP address to which VPN clients will connect

.. cfg_cmd:: vpn l2tp remote-access ppp-options

help: Advanced protocol options

.. cfg_cmd:: vpn l2tp remote-access ppp-options disable-ccp

help: Disable Compression Control Protocol (CCP)

.. cfg_cmd:: vpn l2tp remote-access ppp-options interface-cache

help: PPP interface cache

.. cfg_cmd:: vpn l2tp remote-access ppp-options ipv4

help: IPv4 (IPCP) negotiation algorithm

.. cfg_cmd:: vpn l2tp remote-access ppp-options ipv6

help: IPv6 (IPCP6) negotiation algorithm
deny


.. cfg_cmd:: vpn l2tp remote-access ppp-options ipv6-accept-peer-interface-id

help: Accept peer interface identifier

.. cfg_cmd:: vpn l2tp remote-access ppp-options ipv6-interface-id

help: Fixed or random interface identifier for IPv6

.. cfg_cmd:: vpn l2tp remote-access ppp-options ipv6-peer-interface-id

help: Peer interface identifier for IPv6

.. cfg_cmd:: vpn l2tp remote-access ppp-options lcp-echo-failure

help: Maximum number of Echo-Requests may be sent without valid reply
3


.. cfg_cmd:: vpn l2tp remote-access ppp-options lcp-echo-interval

help: LCP echo-requests/sec
30


.. cfg_cmd:: vpn l2tp remote-access ppp-options lcp-echo-timeout

help: Timeout in seconds to wait for any peer activity. If this option specified it turns on adaptive lcp echo functionality and "lcp-echo-failure" is not used.
0


.. cfg_cmd:: vpn l2tp remote-access ppp-options min-mtu

help: Minimum acceptable MTU (68-65535)

.. cfg_cmd:: vpn l2tp remote-access ppp-options mppe

help: Specifies mppe negotiation preferences
prefer


.. cfg_cmd:: vpn l2tp remote-access ppp-options mru

help: Preferred MRU (68-65535)

.. cfg_cmd:: vpn l2tp remote-access shaper

help: Traffic shaper bandwidth parameters

.. cfg_cmd:: vpn l2tp remote-access shaper fwmark

help: Firewall mark value for traffic that excludes from shaping

.. cfg_cmd:: vpn l2tp remote-access snmp

help: Enable SNMP

.. cfg_cmd:: vpn l2tp remote-access snmp master-agent

help: Enable SNMP master agent mode

.. cfg_cmd:: vpn l2tp remote-access wins-server

help: Windows Internet Name Service (WINS) servers propagated to client

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

.. cfg_cmd:: vpn pptp

help: Point to Point Tunneling Protocol (PPTP) Virtual Private Network (VPN)

.. cfg_cmd:: vpn pptp remote-access

help: Remote access PPTP VPN

.. cfg_cmd:: vpn pptp remote-access authentication

help: Authentication for remote access PPTP VPN

.. cfg_cmd:: vpn pptp remote-access authentication local-users

help: Local user authentication for PPPoE server

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag>

help: User name for authentication

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> disable

help: Disable instance

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> password

help: Password for authentication

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> rate-limit download

help: Download bandwidth limit in kbits/sec

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> rate-limit upload

help: Upload bandwidth limit in kbits/sec

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> static-ip

help: Static client IP address
*


.. cfg_cmd:: vpn pptp remote-access authentication mode

help: Authentication mode used by this server
local


.. cfg_cmd:: vpn pptp remote-access authentication protocols

help: Authentication protocol for remote access peer
pap chap mschap mschap-v2


.. cfg_cmd:: vpn pptp remote-access authentication radius

help: RADIUS based user authentication

.. cfg_cmd:: vpn pptp remote-access authentication radius accounting-interim-interval

help: Interval in seconds to send accounting information

.. cfg_cmd:: vpn pptp remote-access authentication radius acct-interim-jitter

help: Maximum jitter value in seconds to be applied to accounting information interval

.. cfg_cmd:: vpn pptp remote-access authentication radius acct-timeout

help: Timeout for Interim-Update packets, terminate session afterwards
3


.. cfg_cmd:: vpn pptp remote-access authentication radius dynamic-author

help: Dynamic Authorization Extension/Change of Authorization server

.. cfg_cmd:: vpn pptp remote-access authentication radius dynamic-author key

help: Shared secret for Dynamic Authorization Extension server

.. cfg_cmd:: vpn pptp remote-access authentication radius dynamic-author port

help: Port for Dynamic Authorization Extension server (DM/CoA)
1700


.. cfg_cmd:: vpn pptp remote-access authentication radius dynamic-author server

help: IP address for Dynamic Authorization Extension server (DM/CoA)

.. cfg_cmd:: vpn pptp remote-access authentication radius max-try

help: Number of tries to send Access-Request/Accounting-Request queries
3


.. cfg_cmd:: vpn pptp remote-access authentication radius nas-identifier

help: NAS-Identifier attribute sent to RADIUS

.. cfg_cmd:: vpn pptp remote-access authentication radius nas-ip-address

help: NAS-IP-Address attribute sent to RADIUS

.. cfg_cmd:: vpn pptp remote-access authentication radius preallocate-vif

help: Enable attribute NAS-Port-Id in Access-Request

.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit attribute

help: RADIUS attribute that contains rate information
Filter-Id


.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit enable

help: Enable bandwidth shaping via RADIUS

.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit multiplier

help: Shaper multiplier
1


.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit vendor

help: Vendor dictionary

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag>

help: No help available

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> acct-port

help: Accounting port
1813


.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> disable

help: Disable instance

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> disable-accounting

help: Disable accounting

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> fail-time

help: Mark server unavailable for <n> seconds on failure
0


.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> key

help: Shared secret key

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: vpn pptp remote-access authentication radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: vpn pptp remote-access authentication radius timeout

help: Timeout in seconds to wait response from RADIUS server
3


.. cfg_cmd:: vpn pptp remote-access client-ip-pool <tag>

help: Client IP pool

.. cfg_cmd:: vpn pptp remote-access client-ip-pool <tag> next-pool

help: Next pool name

.. cfg_cmd:: vpn pptp remote-access client-ip-pool <tag> range

help: Range of IP addresses

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag>

help: Pool of client IPv6 addresses

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag> delegate <tag>

help: Subnet used to delegate prefix through DHCPv6-PD (RFC3633)

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag> delegate <tag> delegation-prefix

help: Prefix length delegated to client

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag> prefix <tag>

help: Pool of addresses used to assign to clients

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag> prefix <tag> mask

help: Prefix length used for individual client
64


.. cfg_cmd:: vpn pptp remote-access default-ipv6-pool

help: Default client IPv6 pool name

.. cfg_cmd:: vpn pptp remote-access default-pool

help: Default client IP pool name

.. cfg_cmd:: vpn pptp remote-access description

help: Description

.. cfg_cmd:: vpn pptp remote-access extended-scripts

help: Extended script execution

.. cfg_cmd:: vpn pptp remote-access extended-scripts on-change

help: Script to run when session interface changed by RADIUS CoA handling

.. cfg_cmd:: vpn pptp remote-access extended-scripts on-down

help: Script to run when session interface going to terminate

.. cfg_cmd:: vpn pptp remote-access extended-scripts on-pre-up

help: Script to run before session interface comes up

.. cfg_cmd:: vpn pptp remote-access extended-scripts on-up

help: Script to run when session interface is completely configured and started

.. cfg_cmd:: vpn pptp remote-access gateway-address

help: Gateway IP address

.. cfg_cmd:: vpn pptp remote-access limits

help: Limits the connection rate from a single source

.. cfg_cmd:: vpn pptp remote-access limits burst

help: Burst count

.. cfg_cmd:: vpn pptp remote-access limits connection-limit

help: Acceptable rate of connections (e.g. 1/min, 60/sec)

.. cfg_cmd:: vpn pptp remote-access limits timeout

help: Timeout in seconds

.. cfg_cmd:: vpn pptp remote-access max-concurrent-sessions

help: Maximum number of concurrent session start attempts

.. cfg_cmd:: vpn pptp remote-access mtu

help: Maximum Transmission Unit (MTU)
1436


.. cfg_cmd:: vpn pptp remote-access name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: vpn pptp remote-access outside-address

help: External IP address to which VPN clients will connect

.. cfg_cmd:: vpn pptp remote-access ppp-options

help: Advanced protocol options

.. cfg_cmd:: vpn pptp remote-access ppp-options disable-ccp

help: Disable Compression Control Protocol (CCP)

.. cfg_cmd:: vpn pptp remote-access ppp-options interface-cache

help: PPP interface cache

.. cfg_cmd:: vpn pptp remote-access ppp-options ipv4

help: IPv4 (IPCP) negotiation algorithm

.. cfg_cmd:: vpn pptp remote-access ppp-options ipv6

help: IPv6 (IPCP6) negotiation algorithm
deny


.. cfg_cmd:: vpn pptp remote-access ppp-options ipv6-accept-peer-interface-id

help: Accept peer interface identifier

.. cfg_cmd:: vpn pptp remote-access ppp-options ipv6-interface-id

help: Fixed or random interface identifier for IPv6

.. cfg_cmd:: vpn pptp remote-access ppp-options ipv6-peer-interface-id

help: Peer interface identifier for IPv6

.. cfg_cmd:: vpn pptp remote-access ppp-options lcp-echo-failure

help: Maximum number of Echo-Requests may be sent without valid reply
3


.. cfg_cmd:: vpn pptp remote-access ppp-options lcp-echo-interval

help: LCP echo-requests/sec
30


.. cfg_cmd:: vpn pptp remote-access ppp-options lcp-echo-timeout

help: Timeout in seconds to wait for any peer activity. If this option specified it turns on adaptive lcp echo functionality and "lcp-echo-failure" is not used.
0


.. cfg_cmd:: vpn pptp remote-access ppp-options min-mtu

help: Minimum acceptable MTU (68-65535)

.. cfg_cmd:: vpn pptp remote-access ppp-options mppe

help: Specifies mppe negotiation preferences
prefer


.. cfg_cmd:: vpn pptp remote-access ppp-options mru

help: Preferred MRU (68-65535)

.. cfg_cmd:: vpn pptp remote-access shaper

help: Traffic shaper bandwidth parameters

.. cfg_cmd:: vpn pptp remote-access shaper fwmark

help: Firewall mark value for traffic that excludes from shaping

.. cfg_cmd:: vpn pptp remote-access snmp

help: Enable SNMP

.. cfg_cmd:: vpn pptp remote-access snmp master-agent

help: Enable SNMP master agent mode

.. cfg_cmd:: vpn pptp remote-access wins-server

help: Windows Internet Name Service (WINS) servers propagated to client

.. cfg_cmd:: vpn sstp

help: Secure Socket Tunneling Protocol (SSTP) server

.. cfg_cmd:: vpn sstp authentication

help: Authentication for remote access SSTP Server

.. cfg_cmd:: vpn sstp authentication local-users

help: Local user authentication for PPPoE server

.. cfg_cmd:: vpn sstp authentication local-users username <tag>

help: User name for authentication

.. cfg_cmd:: vpn sstp authentication local-users username <tag> disable

help: Disable instance

.. cfg_cmd:: vpn sstp authentication local-users username <tag> password

help: Password for authentication

.. cfg_cmd:: vpn sstp authentication local-users username <tag> rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: vpn sstp authentication local-users username <tag> rate-limit download

help: Download bandwidth limit in kbits/sec

.. cfg_cmd:: vpn sstp authentication local-users username <tag> rate-limit upload

help: Upload bandwidth limit in kbits/sec

.. cfg_cmd:: vpn sstp authentication local-users username <tag> static-ip

help: Static client IP address
*


.. cfg_cmd:: vpn sstp authentication mode

help: Authentication mode used by this server
local


.. cfg_cmd:: vpn sstp authentication protocols

help: Authentication protocol for remote access peer
pap chap mschap mschap-v2


.. cfg_cmd:: vpn sstp authentication radius

help: RADIUS based user authentication

.. cfg_cmd:: vpn sstp authentication radius accounting-interim-interval

help: Interval in seconds to send accounting information

.. cfg_cmd:: vpn sstp authentication radius acct-interim-jitter

help: Maximum jitter value in seconds to be applied to accounting information interval

.. cfg_cmd:: vpn sstp authentication radius acct-timeout

help: Timeout for Interim-Update packets, terminate session afterwards
3


.. cfg_cmd:: vpn sstp authentication radius dynamic-author

help: Dynamic Authorization Extension/Change of Authorization server

.. cfg_cmd:: vpn sstp authentication radius dynamic-author key

help: Shared secret for Dynamic Authorization Extension server

.. cfg_cmd:: vpn sstp authentication radius dynamic-author port

help: Port for Dynamic Authorization Extension server (DM/CoA)
1700


.. cfg_cmd:: vpn sstp authentication radius dynamic-author server

help: IP address for Dynamic Authorization Extension server (DM/CoA)

.. cfg_cmd:: vpn sstp authentication radius max-try

help: Number of tries to send Access-Request/Accounting-Request queries
3


.. cfg_cmd:: vpn sstp authentication radius nas-identifier

help: NAS-Identifier attribute sent to RADIUS

.. cfg_cmd:: vpn sstp authentication radius nas-ip-address

help: NAS-IP-Address attribute sent to RADIUS

.. cfg_cmd:: vpn sstp authentication radius preallocate-vif

help: Enable attribute NAS-Port-Id in Access-Request

.. cfg_cmd:: vpn sstp authentication radius rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: vpn sstp authentication radius rate-limit attribute

help: RADIUS attribute that contains rate information
Filter-Id


.. cfg_cmd:: vpn sstp authentication radius rate-limit enable

help: Enable bandwidth shaping via RADIUS

.. cfg_cmd:: vpn sstp authentication radius rate-limit multiplier

help: Shaper multiplier
1


.. cfg_cmd:: vpn sstp authentication radius rate-limit vendor

help: Vendor dictionary

.. cfg_cmd:: vpn sstp authentication radius server <tag>

help: No help available

.. cfg_cmd:: vpn sstp authentication radius server <tag> acct-port

help: Accounting port
1813


.. cfg_cmd:: vpn sstp authentication radius server <tag> disable

help: Disable instance

.. cfg_cmd:: vpn sstp authentication radius server <tag> disable-accounting

help: Disable accounting

.. cfg_cmd:: vpn sstp authentication radius server <tag> fail-time

help: Mark server unavailable for <n> seconds on failure
0


.. cfg_cmd:: vpn sstp authentication radius server <tag> key

help: Shared secret key

.. cfg_cmd:: vpn sstp authentication radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: vpn sstp authentication radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: vpn sstp authentication radius timeout

help: Timeout in seconds to wait response from RADIUS server
3


.. cfg_cmd:: vpn sstp client-ip-pool <tag>

help: Client IP pool

.. cfg_cmd:: vpn sstp client-ip-pool <tag> next-pool

help: Next pool name

.. cfg_cmd:: vpn sstp client-ip-pool <tag> range

help: Range of IP addresses

.. cfg_cmd:: vpn sstp client-ipv6-pool <tag>

help: Pool of client IPv6 addresses

.. cfg_cmd:: vpn sstp client-ipv6-pool <tag> delegate <tag>

help: Subnet used to delegate prefix through DHCPv6-PD (RFC3633)

.. cfg_cmd:: vpn sstp client-ipv6-pool <tag> delegate <tag> delegation-prefix

help: Prefix length delegated to client

.. cfg_cmd:: vpn sstp client-ipv6-pool <tag> prefix <tag>

help: Pool of addresses used to assign to clients

.. cfg_cmd:: vpn sstp client-ipv6-pool <tag> prefix <tag> mask

help: Prefix length used for individual client
64


.. cfg_cmd:: vpn sstp default-ipv6-pool

help: Default client IPv6 pool name

.. cfg_cmd:: vpn sstp default-pool

help: Default client IP pool name

.. cfg_cmd:: vpn sstp description

help: Description

.. cfg_cmd:: vpn sstp extended-scripts

help: Extended script execution

.. cfg_cmd:: vpn sstp extended-scripts on-change

help: Script to run when session interface changed by RADIUS CoA handling

.. cfg_cmd:: vpn sstp extended-scripts on-down

help: Script to run when session interface going to terminate

.. cfg_cmd:: vpn sstp extended-scripts on-pre-up

help: Script to run before session interface comes up

.. cfg_cmd:: vpn sstp extended-scripts on-up

help: Script to run when session interface is completely configured and started

.. cfg_cmd:: vpn sstp gateway-address

help: Gateway IP address

.. cfg_cmd:: vpn sstp limits

help: Limits the connection rate from a single source

.. cfg_cmd:: vpn sstp limits burst

help: Burst count

.. cfg_cmd:: vpn sstp limits connection-limit

help: Acceptable rate of connections (e.g. 1/min, 60/sec)

.. cfg_cmd:: vpn sstp limits timeout

help: Timeout in seconds

.. cfg_cmd:: vpn sstp max-concurrent-sessions

help: Maximum number of concurrent session start attempts

.. cfg_cmd:: vpn sstp mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: vpn sstp name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: vpn sstp port

help: Port number used by connection
443


.. cfg_cmd:: vpn sstp ppp-options

help: Advanced protocol options

.. cfg_cmd:: vpn sstp ppp-options disable-ccp

help: Disable Compression Control Protocol (CCP)

.. cfg_cmd:: vpn sstp ppp-options interface-cache

help: PPP interface cache

.. cfg_cmd:: vpn sstp ppp-options ipv4

help: IPv4 (IPCP) negotiation algorithm

.. cfg_cmd:: vpn sstp ppp-options ipv6

help: IPv6 (IPCP6) negotiation algorithm
deny


.. cfg_cmd:: vpn sstp ppp-options ipv6-accept-peer-interface-id

help: Accept peer interface identifier

.. cfg_cmd:: vpn sstp ppp-options ipv6-interface-id

help: Fixed or random interface identifier for IPv6

.. cfg_cmd:: vpn sstp ppp-options ipv6-peer-interface-id

help: Peer interface identifier for IPv6

.. cfg_cmd:: vpn sstp ppp-options lcp-echo-failure

help: Maximum number of Echo-Requests may be sent without valid reply
3


.. cfg_cmd:: vpn sstp ppp-options lcp-echo-interval

help: LCP echo-requests/sec
30


.. cfg_cmd:: vpn sstp ppp-options lcp-echo-timeout

help: Timeout in seconds to wait for any peer activity. If this option specified it turns on adaptive lcp echo functionality and "lcp-echo-failure" is not used.
0


.. cfg_cmd:: vpn sstp ppp-options min-mtu

help: Minimum acceptable MTU (68-65535)

.. cfg_cmd:: vpn sstp ppp-options mppe

help: Specifies mppe negotiation preferences
prefer


.. cfg_cmd:: vpn sstp ppp-options mru

help: Preferred MRU (68-65535)

.. cfg_cmd:: vpn sstp shaper

help: Traffic shaper bandwidth parameters

.. cfg_cmd:: vpn sstp shaper fwmark

help: Firewall mark value for traffic that excludes from shaping

.. cfg_cmd:: vpn sstp snmp

help: Enable SNMP

.. cfg_cmd:: vpn sstp snmp master-agent

help: Enable SNMP master agent mode

.. cfg_cmd:: vpn sstp ssl

help: SSL Certificate, SSL Key and CA

.. cfg_cmd:: vpn sstp ssl ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: vpn sstp ssl certificate

help: Certificate in PKI configuration

.. cfg_cmd:: vpn sstp wins-server

help: Windows Internet Name Service (WINS) servers propagated to client

