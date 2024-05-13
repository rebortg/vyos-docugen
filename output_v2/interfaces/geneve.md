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

