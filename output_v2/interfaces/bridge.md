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

