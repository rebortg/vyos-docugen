.. cfg_cmd:: interfaces wwan <tag>

help: Wireless Modem (WWAN) Interface

.. cfg_cmd:: interfaces wwan <tag> address

help: IP address

.. cfg_cmd:: interfaces wwan <tag> apn

help: Access Point Name (APN)

.. cfg_cmd:: interfaces wwan <tag> authentication

help: Authentication settings

.. cfg_cmd:: interfaces wwan <tag> authentication password

help: Password used for authentication

.. cfg_cmd:: interfaces wwan <tag> authentication username

help: Username used for authentication

.. cfg_cmd:: interfaces wwan <tag> connect-on-demand

help: Establishment connection automatically when traffic is sent

.. cfg_cmd:: interfaces wwan <tag> description

help: Description

.. cfg_cmd:: interfaces wwan <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces wwan <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces wwan <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces wwan <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces wwan <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces wwan <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces wwan <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces wwan <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces wwan <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces wwan <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces wwan <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wwan <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces wwan <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wwan <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wwan <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wwan <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wwan <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wwan <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wwan <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wwan <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wwan <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wwan <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wwan <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wwan <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wwan <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wwan <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wwan <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wwan <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wwan <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wwan <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wwan <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wwan <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wwan <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wwan <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wwan <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wwan <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wwan <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wwan <tag> mtu

help: Maximum Transmission Unit (MTU)
1430


.. cfg_cmd:: interfaces wwan <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wwan <tag> vrf

help: VRF instance name

