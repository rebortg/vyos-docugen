.. cfg_cmd:: interfaces macsec <tag>

help: MACsec Interface (802.1ae)

.. cfg_cmd:: interfaces macsec <tag> address

help: IP address

.. cfg_cmd:: interfaces macsec <tag> description

help: Description

.. cfg_cmd:: interfaces macsec <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces macsec <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces macsec <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces macsec <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces macsec <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces macsec <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces macsec <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces macsec <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces macsec <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces macsec <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces macsec <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces macsec <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces macsec <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces macsec <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces macsec <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces macsec <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces macsec <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces macsec <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces macsec <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces macsec <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces macsec <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces macsec <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces macsec <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces macsec <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces macsec <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces macsec <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces macsec <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces macsec <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces macsec <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces macsec <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces macsec <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces macsec <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces macsec <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces macsec <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces macsec <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces macsec <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces macsec <tag> mtu

help: Maximum Transmission Unit (MTU)
1460


.. cfg_cmd:: interfaces macsec <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces macsec <tag> security

help: Security/Encryption Settings

.. cfg_cmd:: interfaces macsec <tag> security cipher

help: Cipher suite used

.. cfg_cmd:: interfaces macsec <tag> security encrypt

help: Enable optional MACsec encryption

.. cfg_cmd:: interfaces macsec <tag> security mka

help: MACsec Key Agreement protocol (MKA)

.. cfg_cmd:: interfaces macsec <tag> security mka cak

help: Secure Connectivity Association Key

.. cfg_cmd:: interfaces macsec <tag> security mka ckn

help: Secure Connectivity Association Key Name

.. cfg_cmd:: interfaces macsec <tag> security mka priority

help: Priority of MACsec Key Agreement protocol (MKA) actor
255


.. cfg_cmd:: interfaces macsec <tag> security replay-window

help: IEEE 802.1X/MACsec replay protection window

.. cfg_cmd:: interfaces macsec <tag> security static

help: Use static keys for MACsec [static Secure Authentication Key (SAK) mode]

.. cfg_cmd:: interfaces macsec <tag> security static key

help: MACsec static key

.. cfg_cmd:: interfaces macsec <tag> security static peer <tag>

help: MACsec peer name

.. cfg_cmd:: interfaces macsec <tag> security static peer <tag> disable

help: Disable instance

.. cfg_cmd:: interfaces macsec <tag> security static peer <tag> key

help: MACsec static key

.. cfg_cmd:: interfaces macsec <tag> security static peer <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces macsec <tag> source-interface

help: Physical interface the traffic will go through

.. cfg_cmd:: interfaces macsec <tag> vrf

help: VRF instance name

