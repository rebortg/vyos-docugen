.. cfg_cmd:: interfaces pseudo-ethernet <tag>

help: Pseudo Ethernet Interface (Macvlan)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> address

help: IP address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> description

help: Description

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces pseudo-ethernet <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces pseudo-ethernet <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces pseudo-ethernet <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> mode

help: Receive mode (default: private)
private


.. cfg_cmd:: interfaces pseudo-ethernet <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces pseudo-ethernet <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces pseudo-ethernet <tag> source-interface

help: Physical interface the traffic will go through

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag>

help: Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> address

help: IP address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> description

help: Description

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> egress-qos

help: VLAN egress QoS

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ingress-qos

help: VLAN ingress QoS

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag>

help: QinQ TAG-S Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> address

help: IP address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> description

help: Description

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> protocol

help: Protocol used for service VLAN (default: 802.1ad)
802.1ad


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag>

help: QinQ TAG-C Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> address

help: IP address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> description

help: Description

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vif-c <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vif-s <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces pseudo-ethernet <tag> vrf

help: VRF instance name

