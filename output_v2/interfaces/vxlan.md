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

