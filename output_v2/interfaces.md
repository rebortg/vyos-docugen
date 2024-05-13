.. cfg_cmd:: interfaces

help: Network interfaces

.. cfg_cmd:: interfaces bonding <tag>

help: Bonding Interface/Link Aggregation

.. cfg_cmd:: interfaces bonding <tag> address

help: IP address

.. cfg_cmd:: interfaces bonding <tag> arp-monitor

help: ARP link monitoring parameters

.. cfg_cmd:: interfaces bonding <tag> arp-monitor interval

help: ARP link monitoring interval

.. cfg_cmd:: interfaces bonding <tag> arp-monitor target

help: IP address used for ARP monitoring

.. cfg_cmd:: interfaces bonding <tag> description

help: Description

.. cfg_cmd:: interfaces bonding <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces bonding <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces bonding <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces bonding <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces bonding <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces bonding <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces bonding <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces bonding <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces bonding <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces bonding <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces bonding <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces bonding <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces bonding <tag> evpn

help: EVPN Multihoming

.. cfg_cmd:: interfaces bonding <tag> evpn es-df-pref

help: Preference value used for designated forwarder (DF) election

.. cfg_cmd:: interfaces bonding <tag> evpn es-id

help: Ethernet segment identifier

.. cfg_cmd:: interfaces bonding <tag> evpn es-sys-mac

help: Ethernet segment system MAC

.. cfg_cmd:: interfaces bonding <tag> evpn uplink

help: Uplink to the VXLAN core

.. cfg_cmd:: interfaces bonding <tag> hash-policy

help: Bonding transmit hash policy
layer2


.. cfg_cmd:: interfaces bonding <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces bonding <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bonding <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces bonding <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces bonding <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces bonding <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces bonding <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces bonding <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces bonding <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces bonding <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bonding <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces bonding <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces bonding <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces bonding <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces bonding <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces bonding <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces bonding <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bonding <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces bonding <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bonding <tag> lacp-rate

help: Rate in which we will ask our link partner to transmit LACPDU packets
slow


.. cfg_cmd:: interfaces bonding <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces bonding <tag> member

help: Bridge member interfaces

.. cfg_cmd:: interfaces bonding <tag> member interface

help: Member interface name

.. cfg_cmd:: interfaces bonding <tag> mii-mon-interval

help: Specifies the MII link monitoring frequency in milliseconds
100


.. cfg_cmd:: interfaces bonding <tag> min-links

help: Minimum number of member interfaces required up before enabling bond
0


.. cfg_cmd:: interfaces bonding <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces bonding <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces bonding <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces bonding <tag> mode

help: Bonding mode
802.3ad


.. cfg_cmd:: interfaces bonding <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces bonding <tag> primary

help: Primary device interface

.. cfg_cmd:: interfaces bonding <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces bonding <tag> vif <tag>

help: Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces bonding <tag> vif <tag> address

help: IP address

.. cfg_cmd:: interfaces bonding <tag> vif <tag> description

help: Description

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces bonding <tag> vif <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces bonding <tag> vif <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces bonding <tag> vif <tag> egress-qos

help: VLAN egress QoS

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ingress-qos

help: VLAN ingress QoS

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces bonding <tag> vif <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bonding <tag> vif <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces bonding <tag> vif <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces bonding <tag> vif <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces bonding <tag> vif <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces bonding <tag> vif <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces bonding <tag> vif <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag>

help: QinQ TAG-S Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> address

help: IP address

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> description

help: Description

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> protocol

help: Protocol used for service VLAN (default: 802.1ad)
802.1ad


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag>

help: QinQ TAG-C Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> address

help: IP address

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> description

help: Description

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vif-c <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces bonding <tag> vif-s <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces bonding <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces bridge <tag>

help: Bridge Interface

.. cfg_cmd:: interfaces bridge <tag> address

help: IP address

.. cfg_cmd:: interfaces bridge <tag> aging

help: MAC address aging interval
300


.. cfg_cmd:: interfaces bridge <tag> description

help: Description

.. cfg_cmd:: interfaces bridge <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces bridge <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces bridge <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces bridge <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces bridge <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces bridge <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces bridge <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces bridge <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces bridge <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces bridge <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces bridge <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces bridge <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces bridge <tag> enable-vlan

help: Enable VLAN aware bridge

.. cfg_cmd:: interfaces bridge <tag> forwarding-delay

help: Forwarding delay
14


.. cfg_cmd:: interfaces bridge <tag> hello-time

help: Hello packet advertisement interval
2


.. cfg_cmd:: interfaces bridge <tag> igmp

help: Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) settings

.. cfg_cmd:: interfaces bridge <tag> igmp querier

help: Enable IGMP/MLD querier

.. cfg_cmd:: interfaces bridge <tag> igmp snooping

help: Enable IGMP/MLD snooping

.. cfg_cmd:: interfaces bridge <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces bridge <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bridge <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces bridge <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces bridge <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bridge <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces bridge <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces bridge <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces bridge <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces bridge <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces bridge <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces bridge <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bridge <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces bridge <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces bridge <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces bridge <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces bridge <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces bridge <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces bridge <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bridge <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bridge <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces bridge <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bridge <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces bridge <tag> max-age

help: Interval at which neighbor bridges are removed
20


.. cfg_cmd:: interfaces bridge <tag> member

help: Bridge member interfaces

.. cfg_cmd:: interfaces bridge <tag> member interface <tag>

help: Member interface name

.. cfg_cmd:: interfaces bridge <tag> member interface <tag> allowed-vlan

help: Specify VLAN id which is allowed in this trunk interface

.. cfg_cmd:: interfaces bridge <tag> member interface <tag> cost

help: Bridge port cost
100


.. cfg_cmd:: interfaces bridge <tag> member interface <tag> isolated

help: Port is isolated (also known as Private-VLAN)

.. cfg_cmd:: interfaces bridge <tag> member interface <tag> native-vlan

help: Specify VLAN id which should natively be present on the link

.. cfg_cmd:: interfaces bridge <tag> member interface <tag> priority

help: Bridge port priority
32


.. cfg_cmd:: interfaces bridge <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces bridge <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces bridge <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces bridge <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces bridge <tag> priority

help: Priority for this bridge
32768


.. cfg_cmd:: interfaces bridge <tag> protocol

help: Protocol used for service VLAN (default: 802.1ad)
802.1q


.. cfg_cmd:: interfaces bridge <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces bridge <tag> stp

help: Enable spanning tree protocol

.. cfg_cmd:: interfaces bridge <tag> vif <tag>

help: Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces bridge <tag> vif <tag> address

help: IP address

.. cfg_cmd:: interfaces bridge <tag> vif <tag> description

help: Description

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces bridge <tag> vif <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces bridge <tag> vif <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces bridge <tag> vif <tag> egress-qos

help: VLAN egress QoS

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ingress-qos

help: VLAN ingress QoS

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces bridge <tag> vif <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces bridge <tag> vif <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces bridge <tag> vif <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces bridge <tag> vif <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces bridge <tag> vif <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces bridge <tag> vif <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces bridge <tag> vif <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces bridge <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces dummy <tag>

help: Dummy Interface

.. cfg_cmd:: interfaces dummy <tag> address

help: IP address

.. cfg_cmd:: interfaces dummy <tag> description

help: Description

.. cfg_cmd:: interfaces dummy <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces dummy <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces dummy <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces dummy <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces dummy <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces dummy <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces dummy <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces dummy <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces dummy <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces dummy <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces dummy <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces dummy <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces dummy <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces dummy <tag> netns

help: Network namespace name

.. cfg_cmd:: interfaces dummy <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces dummy <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces ethernet <tag>

help: Ethernet Interface

.. cfg_cmd:: interfaces ethernet <tag> address

help: IP address

.. cfg_cmd:: interfaces ethernet <tag> description

help: Description

.. cfg_cmd:: interfaces ethernet <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces ethernet <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces ethernet <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces ethernet <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces ethernet <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces ethernet <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces ethernet <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces ethernet <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces ethernet <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces ethernet <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces ethernet <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces ethernet <tag> disable-flow-control

help: Disable Ethernet flow control (pause frames)

.. cfg_cmd:: interfaces ethernet <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces ethernet <tag> duplex

help: Duplex mode
auto


.. cfg_cmd:: interfaces ethernet <tag> eapol

help: Extensible Authentication Protocol over Local Area Network

.. cfg_cmd:: interfaces ethernet <tag> eapol ca-certificate

help: Certificate Authority chain in PKI configuration

.. cfg_cmd:: interfaces ethernet <tag> eapol certificate

help: Certificate in PKI configuration

.. cfg_cmd:: interfaces ethernet <tag> eapol passphrase

help: Private key passphrase

.. cfg_cmd:: interfaces ethernet <tag> hw-id

help: Associate Ethernet Interface with given Media Access Control (MAC) address

.. cfg_cmd:: interfaces ethernet <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces ethernet <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces ethernet <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces ethernet <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces ethernet <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces ethernet <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces ethernet <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces ethernet <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces ethernet <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces ethernet <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces ethernet <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces ethernet <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces ethernet <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces ethernet <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces ethernet <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces ethernet <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces ethernet <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces ethernet <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces ethernet <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces ethernet <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces ethernet <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces ethernet <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces ethernet <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces ethernet <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces ethernet <tag> offload

help: Configurable offload options

.. cfg_cmd:: interfaces ethernet <tag> offload gro

help: Enable Generic Receive Offload

.. cfg_cmd:: interfaces ethernet <tag> offload gso

help: Enable Generic Segmentation Offload

.. cfg_cmd:: interfaces ethernet <tag> offload hw-tc-offload

help: Enable Hardware Flow Offload

.. cfg_cmd:: interfaces ethernet <tag> offload lro

help: Enable Large Receive Offload

.. cfg_cmd:: interfaces ethernet <tag> offload rfs

help: Enable Receive Flow Steering

.. cfg_cmd:: interfaces ethernet <tag> offload rps

help: Enable Receive Packet Steering

.. cfg_cmd:: interfaces ethernet <tag> offload sg

help: Enable Scatter-Gather

.. cfg_cmd:: interfaces ethernet <tag> offload tso

help: Enable TCP Segmentation Offloading

.. cfg_cmd:: interfaces ethernet <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces ethernet <tag> ring-buffer

help: Shared buffer between the device driver and NIC

.. cfg_cmd:: interfaces ethernet <tag> ring-buffer rx

help: RX ring buffer

.. cfg_cmd:: interfaces ethernet <tag> ring-buffer tx

help: TX ring buffer

.. cfg_cmd:: interfaces ethernet <tag> speed

help: Link speed
auto


.. cfg_cmd:: interfaces ethernet <tag> vif <tag>

help: Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> address

help: IP address

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> description

help: Description

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> egress-qos

help: VLAN egress QoS

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ingress-qos

help: VLAN ingress QoS

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces ethernet <tag> vif <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces ethernet <tag> vif <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces ethernet <tag> vif <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag>

help: QinQ TAG-S Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> address

help: IP address

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> description

help: Description

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> protocol

help: Protocol used for service VLAN (default: 802.1ad)
802.1ad


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag>

help: QinQ TAG-C Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> address

help: IP address

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> description

help: Description

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vif-c <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces ethernet <tag> vif-s <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces ethernet <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces geneve <tag>

help: Generic Network Virtualization Encapsulation (GENEVE) Interface

.. cfg_cmd:: interfaces geneve <tag> address

help: IP address

.. cfg_cmd:: interfaces geneve <tag> description

help: Description

.. cfg_cmd:: interfaces geneve <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces geneve <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces geneve <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces geneve <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces geneve <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces geneve <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces geneve <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces geneve <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces geneve <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces geneve <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces geneve <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces geneve <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces geneve <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces geneve <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces geneve <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces geneve <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces geneve <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces geneve <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces geneve <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces geneve <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces geneve <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces geneve <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces geneve <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces geneve <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces geneve <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces geneve <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces geneve <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces geneve <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces geneve <tag> parameters

help: GENEVE tunnel parameters

.. cfg_cmd:: interfaces geneve <tag> parameters ip

help: IPv4 specific tunnel parameters

.. cfg_cmd:: interfaces geneve <tag> parameters ip df

help: Usage of the DF (don't Fragment) bit in outgoing packets
unset


.. cfg_cmd:: interfaces geneve <tag> parameters ip innerproto

help: Use IPv4 as inner protocol instead of Ethernet

.. cfg_cmd:: interfaces geneve <tag> parameters ip tos

help: Specifies TOS value to use in outgoing packets
inherit


.. cfg_cmd:: interfaces geneve <tag> parameters ip ttl

help: Specifies TTL value to use in outgoing packets
0


.. cfg_cmd:: interfaces geneve <tag> parameters ipv6

help: IPv6 specific tunnel parameters

.. cfg_cmd:: interfaces geneve <tag> parameters ipv6 flowlabel

help: Specifies the flow label to use in outgoing packets

.. cfg_cmd:: interfaces geneve <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces geneve <tag> remote

help: Tunnel remote address

.. cfg_cmd:: interfaces geneve <tag> vni

help: Virtual Network Identifier

.. cfg_cmd:: interfaces input <tag>

help: Input Functional Block (IFB) interface name

.. cfg_cmd:: interfaces input <tag> description

help: Description

.. cfg_cmd:: interfaces input <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces input <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces l2tpv3 <tag>

help: Layer 2 Tunnel Protocol Version 3 (L2TPv3) Interface

.. cfg_cmd:: interfaces l2tpv3 <tag> address

help: IP address

.. cfg_cmd:: interfaces l2tpv3 <tag> description

help: Description

.. cfg_cmd:: interfaces l2tpv3 <tag> destination-port

help: UDP destination port for L2TPv3 tunnel
5000


.. cfg_cmd:: interfaces l2tpv3 <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces l2tpv3 <tag> encapsulation

help: Encapsulation type
udp


.. cfg_cmd:: interfaces l2tpv3 <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces l2tpv3 <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces l2tpv3 <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces l2tpv3 <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces l2tpv3 <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces l2tpv3 <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces l2tpv3 <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces l2tpv3 <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces l2tpv3 <tag> mtu

help: Maximum Transmission Unit (MTU)
1488


.. cfg_cmd:: interfaces l2tpv3 <tag> peer-session-id

help: Peer session identifier

.. cfg_cmd:: interfaces l2tpv3 <tag> peer-tunnel-id

help: Peer tunnel identifier

.. cfg_cmd:: interfaces l2tpv3 <tag> remote

help: Tunnel remote address

.. cfg_cmd:: interfaces l2tpv3 <tag> session-id

help: Session identifier

.. cfg_cmd:: interfaces l2tpv3 <tag> source-address

help: Source IP address used to initiate connection

.. cfg_cmd:: interfaces l2tpv3 <tag> source-port

help: UDP source port for L2TPv3 tunnel
5000


.. cfg_cmd:: interfaces l2tpv3 <tag> tunnel-id

help: Local tunnel identifier

.. cfg_cmd:: interfaces l2tpv3 <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces loopback <tag>

help: Loopback Interface

.. cfg_cmd:: interfaces loopback <tag> address

help: IP address

.. cfg_cmd:: interfaces loopback <tag> description

help: Description

.. cfg_cmd:: interfaces loopback <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces loopback <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces loopback <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces loopback <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces loopback <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces loopback <tag> redirect

help: Redirect incoming packet to destination

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

.. cfg_cmd:: interfaces pppoe <tag>

help: Point-to-Point Protocol over Ethernet (PPPoE) Interface

.. cfg_cmd:: interfaces pppoe <tag> access-concentrator

help: Access concentrator name

.. cfg_cmd:: interfaces pppoe <tag> authentication

help: Authentication settings

.. cfg_cmd:: interfaces pppoe <tag> authentication password

help: Password used for authentication

.. cfg_cmd:: interfaces pppoe <tag> authentication username

help: Username used for authentication

.. cfg_cmd:: interfaces pppoe <tag> connect-on-demand

help: Establishment connection automatically when traffic is sent

.. cfg_cmd:: interfaces pppoe <tag> default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces pppoe <tag> description

help: Description

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces pppoe <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces pppoe <tag> holdoff

help: Delay before re-dial to the access concentrator when PPP session terminated by peer (in seconds)
30


.. cfg_cmd:: interfaces pppoe <tag> host-uniq

help: PPPoE RFC2516 host-uniq tag

.. cfg_cmd:: interfaces pppoe <tag> idle-timeout

help: Delay before disconnecting idle session (in seconds)

.. cfg_cmd:: interfaces pppoe <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces pppoe <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pppoe <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pppoe <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pppoe <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces pppoe <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces pppoe <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces pppoe <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pppoe <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pppoe <tag> local-address

help: IPv4 address of local end of the PPPoE link

.. cfg_cmd:: interfaces pppoe <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces pppoe <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces pppoe <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces pppoe <tag> mru

help: Maximum Receive Unit (MRU) (default: MTU value)

.. cfg_cmd:: interfaces pppoe <tag> mtu

help: Maximum Transmission Unit (MTU)
1492


.. cfg_cmd:: interfaces pppoe <tag> no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces pppoe <tag> no-peer-dns

help: Do not use DNS servers provided by the peer

.. cfg_cmd:: interfaces pppoe <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces pppoe <tag> remote-address

help: IPv4 address of remote end of the PPPoE link

.. cfg_cmd:: interfaces pppoe <tag> service-name

help: Service name, only connect to access concentrators advertising this

.. cfg_cmd:: interfaces pppoe <tag> source-interface

help: Interface used to establish connection

.. cfg_cmd:: interfaces pppoe <tag> vrf

help: VRF instance name

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

.. cfg_cmd:: interfaces sstpc <tag>

help: Secure Socket Tunneling Protocol (SSTP) client Interface

.. cfg_cmd:: interfaces sstpc <tag> authentication

help: Authentication settings

.. cfg_cmd:: interfaces sstpc <tag> authentication password

help: Password used for authentication

.. cfg_cmd:: interfaces sstpc <tag> authentication username

help: Username used for authentication

.. cfg_cmd:: interfaces sstpc <tag> default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces sstpc <tag> description

help: Description

.. cfg_cmd:: interfaces sstpc <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces sstpc <tag> mtu

help: Maximum Transmission Unit (MTU)
1452


.. cfg_cmd:: interfaces sstpc <tag> no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces sstpc <tag> no-peer-dns

help: Do not use DNS servers provided by the peer

.. cfg_cmd:: interfaces sstpc <tag> port

help: Port number used by connection
443


.. cfg_cmd:: interfaces sstpc <tag> server

help: Remote server to connect to

.. cfg_cmd:: interfaces sstpc <tag> ssl

help: Secure Sockets Layer (SSL) configuration

.. cfg_cmd:: interfaces sstpc <tag> ssl ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: interfaces sstpc <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces tunnel <tag>

help: Tunnel interface

.. cfg_cmd:: interfaces tunnel <tag> 6rd-prefix

help: 6rd network prefix

.. cfg_cmd:: interfaces tunnel <tag> 6rd-relay-prefix

help: 6rd relay prefix

.. cfg_cmd:: interfaces tunnel <tag> address

help: IP address

.. cfg_cmd:: interfaces tunnel <tag> description

help: Description

.. cfg_cmd:: interfaces tunnel <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces tunnel <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces tunnel <tag> enable-multicast

help: Enable multicast operation over tunnel

.. cfg_cmd:: interfaces tunnel <tag> encapsulation

help: Encapsulation of this tunnel interface

.. cfg_cmd:: interfaces tunnel <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces tunnel <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces tunnel <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces tunnel <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces tunnel <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces tunnel <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces tunnel <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces tunnel <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces tunnel <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces tunnel <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces tunnel <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces tunnel <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces tunnel <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces tunnel <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces tunnel <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces tunnel <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces tunnel <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces tunnel <tag> mtu

help: Maximum Transmission Unit (MTU)
1476


.. cfg_cmd:: interfaces tunnel <tag> parameters

help: Tunnel parameters

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan

help: ERSPAN tunnel parameters

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan direction

help: Mirrored traffic direction

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan hw-id

help: Unique identifier of an ERSPAN engine within a system

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan index

help: ERSPAN version 1 index field

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan version

help: Protocol version
1


.. cfg_cmd:: interfaces tunnel <tag> parameters ip

help: IPv4-specific tunnel parameters

.. cfg_cmd:: interfaces tunnel <tag> parameters ip ignore-df

help: Ignore the DF (don't fragment) bit

.. cfg_cmd:: interfaces tunnel <tag> parameters ip key

help: Tunnel key (only GRE tunnels)

.. cfg_cmd:: interfaces tunnel <tag> parameters ip no-pmtu-discovery

help: Disable path MTU discovery

.. cfg_cmd:: interfaces tunnel <tag> parameters ip tos

help: Specifies TOS value to use in outgoing packets
inherit


.. cfg_cmd:: interfaces tunnel <tag> parameters ip ttl

help: Specifies TTL value to use in outgoing packets
64


.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6

help: IPv6-specific tunnel parameters

.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6 encaplimit

help: Set fixed encapsulation limit
4


.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6 flowlabel

help: Specifies the flow label to use in outgoing packets

.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6 hoplimit

help: Hoplimit
64


.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6 tclass

help: Traffic class (Tclass)
inherit


.. cfg_cmd:: interfaces tunnel <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces tunnel <tag> remote

help: Tunnel remote address

.. cfg_cmd:: interfaces tunnel <tag> source-address

help: Source IP address used to initiate connection

.. cfg_cmd:: interfaces tunnel <tag> source-interface

help: Interface used to establish connection

.. cfg_cmd:: interfaces tunnel <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces virtual-ethernet <tag>

help: Virtual Ethernet (veth) Interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> address

help: IP address

.. cfg_cmd:: interfaces virtual-ethernet <tag> description

help: Description

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces virtual-ethernet <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces virtual-ethernet <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> netns

help: Network namespace name

.. cfg_cmd:: interfaces virtual-ethernet <tag> peer-name

help: Virtual ethernet peer interface name

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag>

help: Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> address

help: IP address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> description

help: Description

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> egress-qos

help: VLAN egress QoS

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ingress-qos

help: VLAN ingress QoS

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag>

help: QinQ TAG-S Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> address

help: IP address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> description

help: Description

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> protocol

help: Protocol used for service VLAN (default: 802.1ad)
802.1ad


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag>

help: QinQ TAG-C Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> address

help: IP address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> description

help: Description

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vif-c <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces virtual-ethernet <tag> vif-s <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces virtual-ethernet <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces vti <tag>

help: Virtual Tunnel Interface (XFRM)

.. cfg_cmd:: interfaces vti <tag> address

help: IP address

.. cfg_cmd:: interfaces vti <tag> description

help: Description

.. cfg_cmd:: interfaces vti <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces vti <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces vti <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces vti <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces vti <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces vti <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces vti <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces vti <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces vti <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces vti <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces vti <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces vti <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces vti <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces vti <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces vti <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces vti <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces vti <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces vti <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces vti <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces vti <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces vti <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces vti <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces vti <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces vti <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces vti <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces vti <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces vti <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces vti <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces vti <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces vxlan <tag>

help: Virtual Extensible LAN (VXLAN) Interface

.. cfg_cmd:: interfaces vxlan <tag> address

help: IP address

.. cfg_cmd:: interfaces vxlan <tag> description

help: Description

.. cfg_cmd:: interfaces vxlan <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces vxlan <tag> gpe

help: Enable Generic Protocol extension (VXLAN-GPE)

.. cfg_cmd:: interfaces vxlan <tag> group

help: Multicast group address for VXLAN interface

.. cfg_cmd:: interfaces vxlan <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces vxlan <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces vxlan <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces vxlan <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces vxlan <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces vxlan <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces vxlan <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces vxlan <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces vxlan <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces vxlan <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces vxlan <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces vxlan <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces vxlan <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces vxlan <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces vxlan <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces vxlan <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces vxlan <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces vxlan <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces vxlan <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces vxlan <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces vxlan <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces vxlan <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces vxlan <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces vxlan <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces vxlan <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces vxlan <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces vxlan <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces vxlan <tag> parameters

help: VXLAN tunnel parameters

.. cfg_cmd:: interfaces vxlan <tag> parameters external

help: Use external control plane

.. cfg_cmd:: interfaces vxlan <tag> parameters ip

help: IPv4 specific tunnel parameters

.. cfg_cmd:: interfaces vxlan <tag> parameters ip df

help: Usage of the DF (don't Fragment) bit in outgoing packets
unset


.. cfg_cmd:: interfaces vxlan <tag> parameters ip tos

help: Specifies TOS value to use in outgoing packets
inherit


.. cfg_cmd:: interfaces vxlan <tag> parameters ip ttl

help: Specifies TTL value to use in outgoing packets
16


.. cfg_cmd:: interfaces vxlan <tag> parameters ipv6

help: IPv6 specific tunnel parameters

.. cfg_cmd:: interfaces vxlan <tag> parameters ipv6 flowlabel

help: Specifies the flow label to use in outgoing packets

.. cfg_cmd:: interfaces vxlan <tag> parameters neighbor-suppress

help: Enable neighbor discovery (ARP and ND) suppression

.. cfg_cmd:: interfaces vxlan <tag> parameters nolearning

help: Do not add unknown addresses into forwarding database

.. cfg_cmd:: interfaces vxlan <tag> parameters vni-filter

help: Enable VNI filter support

.. cfg_cmd:: interfaces vxlan <tag> port

help: Port number used by connection
4789


.. cfg_cmd:: interfaces vxlan <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces vxlan <tag> remote

help: Tunnel remote address

.. cfg_cmd:: interfaces vxlan <tag> source-address

help: Source IP address used to initiate connection

.. cfg_cmd:: interfaces vxlan <tag> source-interface

help: Interface used to establish connection

.. cfg_cmd:: interfaces vxlan <tag> vlan-to-vni <tag>

help: Configuring VLAN-to-VNI mappings for EVPN-VXLAN

.. cfg_cmd:: interfaces vxlan <tag> vlan-to-vni <tag> vni

help: Virtual Network Identifier

.. cfg_cmd:: interfaces vxlan <tag> vni

help: Virtual Network Identifier

.. cfg_cmd:: interfaces vxlan <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces wireguard <tag>

help: WireGuard Interface

.. cfg_cmd:: interfaces wireguard <tag> address

help: IP address

.. cfg_cmd:: interfaces wireguard <tag> description

help: Description

.. cfg_cmd:: interfaces wireguard <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireguard <tag> fwmark

help: A 32-bit fwmark value set on all outgoing packets
0


.. cfg_cmd:: interfaces wireguard <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireguard <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireguard <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireguard <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireguard <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireguard <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireguard <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireguard <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireguard <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireguard <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireguard <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireguard <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireguard <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireguard <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireguard <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireguard <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireguard <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireguard <tag> mtu

help: Maximum Transmission Unit (MTU)
1420


.. cfg_cmd:: interfaces wireguard <tag> peer <tag>

help: peer alias

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> address

help: IP address of tunnel endpoint

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> allowed-ips

help: IP addresses allowed to traverse the peer

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> description

help: Description

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> disable

help: Disable instance

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> persistent-keepalive

help: Interval to send keepalive messages

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> port

help: Port number used by connection

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> preshared-key

help: base64 encoded preshared key

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> public-key

help: base64 encoded public key

.. cfg_cmd:: interfaces wireguard <tag> per-client-thread

help: Process traffic from each client in a dedicated thread

.. cfg_cmd:: interfaces wireguard <tag> port

help: Port number used by connection

.. cfg_cmd:: interfaces wireguard <tag> private-key

help: Base64 encoded private key

.. cfg_cmd:: interfaces wireguard <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireguard <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces wireless <tag>

help: Wireless (WiFi/WLAN) Network Interface

.. cfg_cmd:: interfaces wireless <tag> address

help: IP address

.. cfg_cmd:: interfaces wireless <tag> capabilities

help: HT and VHT capabilities for your card

.. cfg_cmd:: interfaces wireless <tag> capabilities ht

help: HT (High Throughput) settings

.. cfg_cmd:: interfaces wireless <tag> capabilities ht 40mhz-incapable

help: 40MHz intolerance, use 20MHz only!

.. cfg_cmd:: interfaces wireless <tag> capabilities ht auto-powersave

help: Enable WMM-PS unscheduled automatic power aave delivery [U-APSD]

.. cfg_cmd:: interfaces wireless <tag> capabilities ht channel-set-width

help: Supported channel set width

.. cfg_cmd:: interfaces wireless <tag> capabilities ht delayed-block-ack

help: Enable HT-delayed block ack

.. cfg_cmd:: interfaces wireless <tag> capabilities ht dsss-cck-40

help: Enable DSSS_CCK-40

.. cfg_cmd:: interfaces wireless <tag> capabilities ht greenfield

help: Enable HT-greenfield

.. cfg_cmd:: interfaces wireless <tag> capabilities ht ldpc

help: Enable LDPC coding capability

.. cfg_cmd:: interfaces wireless <tag> capabilities ht lsig-protection

help: Enable L-SIG TXOP protection capability

.. cfg_cmd:: interfaces wireless <tag> capabilities ht max-amsdu

help: Set maximum A-MSDU length

.. cfg_cmd:: interfaces wireless <tag> capabilities ht short-gi

help: Short GI capabilities

.. cfg_cmd:: interfaces wireless <tag> capabilities ht smps

help: Spatial Multiplexing Power Save (SMPS) settings

.. cfg_cmd:: interfaces wireless <tag> capabilities ht stbc

help: Support for sending and receiving PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities ht stbc rx

help: Enable receiving PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities ht stbc tx

help: Enable sending PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities require-ht

help: Require stations to support HT PHY (reject association if they do not)

.. cfg_cmd:: interfaces wireless <tag> capabilities require-vht

help: Require stations to support VHT PHY (reject association if they do not)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht

help: VHT (Very High Throughput) settings

.. cfg_cmd:: interfaces wireless <tag> capabilities vht antenna-count

help: Number of antennas on this card

.. cfg_cmd:: interfaces wireless <tag> capabilities vht antenna-pattern-fixed

help: Set if antenna pattern does not change during the lifetime of an association

.. cfg_cmd:: interfaces wireless <tag> capabilities vht beamform

help: Beamforming capabilities

.. cfg_cmd:: interfaces wireless <tag> capabilities vht center-channel-freq

help: VHT operating channel center frequency

.. cfg_cmd:: interfaces wireless <tag> capabilities vht center-channel-freq freq-1

help: VHT operating channel center frequency - center freq 1 (for use with 80, 80+80 and 160 modes)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht center-channel-freq freq-2

help: VHT operating channel center frequency - center freq 2 (for use with the 80+80 mode)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht channel-set-width

help: VHT operating Channel width

.. cfg_cmd:: interfaces wireless <tag> capabilities vht ldpc

help: Enable LDPC (Low Density Parity Check) coding capability

.. cfg_cmd:: interfaces wireless <tag> capabilities vht link-adaptation

help: VHT link adaptation capabilities

.. cfg_cmd:: interfaces wireless <tag> capabilities vht max-mpdu

help: Increase Maximum MPDU length to 7991 or 11454 octets (otherwise: 3895 octets)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht max-mpdu-exp

help: Set the maximum length of A-MPDU pre-EOF padding that the station can receive

.. cfg_cmd:: interfaces wireless <tag> capabilities vht short-gi

help: Short GI capabilities

.. cfg_cmd:: interfaces wireless <tag> capabilities vht stbc

help: Support for sending and receiving PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht stbc rx

help: Enable receiving PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht stbc tx

help: Enable sending PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht tx-powersave

help: Enable VHT TXOP Power Save Mode

.. cfg_cmd:: interfaces wireless <tag> capabilities vht vht-cf

help: Station supports receiving VHT variant HT Control field

.. cfg_cmd:: interfaces wireless <tag> channel

help: Wireless radio channel
0


.. cfg_cmd:: interfaces wireless <tag> country-code

help: Indicate country in which device is operating

.. cfg_cmd:: interfaces wireless <tag> description

help: Description

.. cfg_cmd:: interfaces wireless <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces wireless <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces wireless <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces wireless <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces wireless <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces wireless <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces wireless <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces wireless <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces wireless <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireless <tag> disable-broadcast-ssid

help: Disable broadcast of SSID from access-point

.. cfg_cmd:: interfaces wireless <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces wireless <tag> expunge-failing-stations

help: Disassociate stations based on excessive transmission failures

.. cfg_cmd:: interfaces wireless <tag> hw-id

help: Associate Ethernet Interface with given Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireless <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireless <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireless <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireless <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireless <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireless <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireless <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireless <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireless <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireless <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireless <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireless <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> isolate-stations

help: Isolate stations on the AP so they cannot see each other

.. cfg_cmd:: interfaces wireless <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> max-stations

help: Maximum number of wireless radio stations. Excess stations will be rejected upon authentication request.

.. cfg_cmd:: interfaces wireless <tag> mgmt-frame-protection

help: Management Frame Protection (MFP) according to IEEE 802.11w
disabled


.. cfg_cmd:: interfaces wireless <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireless <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> mode

help: Wireless radio mode
g


.. cfg_cmd:: interfaces wireless <tag> per-client-thread

help: Process traffic from each client in a dedicated thread

.. cfg_cmd:: interfaces wireless <tag> physical-device

help: Wireless physical device
phy0


.. cfg_cmd:: interfaces wireless <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireless <tag> reduce-transmit-power

help: Transmission power reduction in dBm

.. cfg_cmd:: interfaces wireless <tag> security

help: Wireless security settings

.. cfg_cmd:: interfaces wireless <tag> security station-address

help: Station MAC address based authentication

.. cfg_cmd:: interfaces wireless <tag> security station-address accept

help: Accept station MAC address

.. cfg_cmd:: interfaces wireless <tag> security station-address accept mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> security station-address deny

help: Deny station MAC address

.. cfg_cmd:: interfaces wireless <tag> security station-address deny mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> security station-address mode

help: Select security operation mode
accept


.. cfg_cmd:: interfaces wireless <tag> security wep

help: Wired Equivalent Privacy (WEP) parameters

.. cfg_cmd:: interfaces wireless <tag> security wep key

help: WEP encryption key

.. cfg_cmd:: interfaces wireless <tag> security wpa

help: Wifi Protected Access (WPA) parameters

.. cfg_cmd:: interfaces wireless <tag> security wpa cipher

help: Cipher suite for WPA unicast packets

.. cfg_cmd:: interfaces wireless <tag> security wpa group-cipher

help: Cipher suite for WPA multicast and broadcast packets

.. cfg_cmd:: interfaces wireless <tag> security wpa mode

help: WPA mode
wpa+wpa2


.. cfg_cmd:: interfaces wireless <tag> security wpa passphrase

help: WPA personal shared pass phrase. If you are using special characters in the WPA passphrase then single quotes are required.

.. cfg_cmd:: interfaces wireless <tag> security wpa radius

help: RADIUS based user authentication

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag>

help: No help available

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag> accounting

help: Enable RADIUS server to receive accounting info

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag> disable

help: Disable instance

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag> key

help: Shared secret key

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: interfaces wireless <tag> security wpa radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: interfaces wireless <tag> ssid

help: Wireless access-point service set identifier (SSID)

.. cfg_cmd:: interfaces wireless <tag> type

help: Wireless device type for this interface
monitor


.. cfg_cmd:: interfaces wireless <tag> vif <tag>

help: Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces wireless <tag> vif <tag> address

help: IP address

.. cfg_cmd:: interfaces wireless <tag> vif <tag> description

help: Description

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces wireless <tag> vif <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces wireless <tag> vif <tag> egress-qos

help: VLAN egress QoS

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ingress-qos

help: VLAN ingress QoS

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces wireless <tag> vif <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireless <tag> vif <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag>

help: QinQ TAG-S Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> address

help: IP address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> description

help: Description

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> protocol

help: Protocol used for service VLAN (default: 802.1ad)
802.1ad


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag>

help: QinQ TAG-C Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> address

help: IP address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> description

help: Description

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces wireless <tag> vrf

help: VRF instance name

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

