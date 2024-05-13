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

